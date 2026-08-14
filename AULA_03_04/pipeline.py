"""
Pipeline principal da atividade:

    PDF -> Markdown -> 10 estratégias de chunking -> Embeddings -> JSON

Uso típico:

    # Fase 1: experimentar as 10 estratégias só nos 3 .md das aulas anteriores
    python pipeline.py --markdowns aula_2_markdowns --saida results

    # Fase 2: depois de escolher as melhores estratégias, rodar em todos os PDFs
    python pdf_to_markdown.py --pdfs pdfs --saida results
    python pipeline.py --usar-markdown-de-results --saida results
"""

import os
import re
import json
import glob
import argparse
import statistics

from chunking_strategies import rodar_teste, TESTES
from embeddings_utils import get_embeddings_batch, EMBEDDING_MODEL, EMBEDDING_PROVIDER
from utils import slugify


def processar_documento(document_id: str, pdf_name: str, texto_md: str, pasta_resultados: str) -> dict:
    """Roda os 10 testes de chunking + embeddings para um documento e salva os JSONs."""
    print(f"\n{'=' * 60}")
    print(f"Documento: {document_id}")
    print("=" * 60)

    stats_experimentos = []

    for test_id in range(1, 11):
        config = TESTES[test_id]
        chunks = rodar_teste(test_id, texto_md)

        if not chunks:
            print(f"  Teste {test_id:2d} ({config['strategy']}): nenhum chunk gerado, pulando.")
            continue

        textos = [c["text"] for c in chunks]
        embeddings = get_embeddings_batch(textos)

        registros = []
        for i, (chunk, emb) in enumerate(zip(chunks, embeddings), start=1):
            registros.append({
                "chunk_id": f"{document_id}_test{test_id:02d}_chunk{i:03d}",
                "document_id": document_id,
                "document_name": pdf_name,
                "test_id": test_id,
                "strategy": config["strategy"],
                "chunk_size": config.get("chunk_size"),
                "chunk_overlap": config.get("chunk_overlap"),
                "text": chunk["text"],
                "embedding": emb,
                "metadata": chunk.get("metadata", {}),
            })

        pasta_teste = os.path.join(pasta_resultados, document_id, f"test_{test_id:02d}")
        os.makedirs(pasta_teste, exist_ok=True)
        caminho_saida = os.path.join(pasta_teste, "chunks_embeddings.json")
        with open(caminho_saida, "w", encoding="utf-8") as f:
            json.dump(registros, f, ensure_ascii=False, indent=2)

        tamanhos = [len(t) for t in textos]
        stat = {
            "test_id": test_id,
            "strategy": config["strategy"],
            "chunk_size": config.get("chunk_size"),
            "chunk_overlap": config.get("chunk_overlap"),
            "num_chunks": len(chunks),
            "avg_chunk_size": round(statistics.mean(tamanhos), 2),
            "min_chunk_size": min(tamanhos),
            "max_chunk_size": max(tamanhos),
            "stdev_chunk_size": round(statistics.stdev(tamanhos), 2) if len(tamanhos) > 1 else 0.0,
            "embedding_dimension": len(embeddings[0]) if embeddings else 0,
            "embedding_model": EMBEDDING_MODEL,
        }
        stats_experimentos.append(stat)

        print(f"  Teste {test_id:2d} ({config['strategy']:16s}): "
              f"{stat['num_chunks']:4d} chunks | media={stat['avg_chunk_size']:7.1f} "
              f"| min={stat['min_chunk_size']:5d} | max={stat['max_chunk_size']:5d}")

    return {"document_id": document_id, "document_name": pdf_name, "experiments": stats_experimentos}


def carregar_markdowns_de_pasta(pasta: str) -> dict:
    """Lê todos os .md de uma pasta plana e retorna {document_id: {"pdf_name":..., "texto":...}}."""
    documentos = {}
    for caminho in sorted(glob.glob(os.path.join(pasta, "*.md"))):
        nome_arquivo = os.path.basename(caminho)
        document_id = slugify(nome_arquivo)
        with open(caminho, "r", encoding="utf-8") as f:
            texto = f.read()
        documentos[document_id] = {"pdf_name": nome_arquivo.replace(".md", ".pdf"), "texto": texto}
    return documentos


def carregar_markdowns_de_results(pasta_resultados: str) -> dict:
    """Lê os markdowns já convertidos em results/<doc>/markdown/<doc>.md."""
    documentos = {}
    for caminho in sorted(glob.glob(os.path.join(pasta_resultados, "*", "markdown", "*.md"))):
        document_id = os.path.basename(os.path.dirname(os.path.dirname(caminho)))
        with open(caminho, "r", encoding="utf-8") as f:
            texto = f.read()
        documentos[document_id] = {"pdf_name": f"{document_id}.pdf", "texto": texto}
    return documentos


def rodar_pipeline(markdowns: dict, pasta_resultados: str = "results") -> None:
    if not markdowns:
        print("Nenhum documento encontrado para processar — nada será alterado "
              "(o summary.json existente, se houver, foi preservado).")
        return

    print(f"Provedor de embeddings: {EMBEDDING_PROVIDER} | Modelo: {EMBEDDING_MODEL}")
    print(f"Documentos a processar: {list(markdowns.keys())}")

    caminho_summary = os.path.join(pasta_resultados, "summary.json")
    summary_existente = {}
    if os.path.exists(caminho_summary):
        with open(caminho_summary, "r", encoding="utf-8") as f:
            for doc in json.load(f):
                summary_existente[doc["document_id"]] = doc

    for document_id, info in markdowns.items():
        resumo_doc = processar_documento(document_id, info["pdf_name"], info["texto"], pasta_resultados)
        summary_existente[document_id] = resumo_doc  # atualiza/insere, preserva os demais

    summary_final = list(summary_existente.values())
    os.makedirs(pasta_resultados, exist_ok=True)
    with open(caminho_summary, "w", encoding="utf-8") as f:
        json.dump(summary_final, f, ensure_ascii=False, indent=2)

    print(f"\nResumo comparativo salvo em {caminho_summary} ({len(summary_final)} documento(s) no total)")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--markdowns", help="Pasta plana contendo arquivos .md prontos (ex: os 3 .md das aulas anteriores)")
    parser.add_argument("--usar-markdown-de-results", action="store_true",
                         help="Usa os markdowns já convertidos dentro de results/<doc>/markdown/")
    parser.add_argument("--saida", default="results", help="Pasta raiz de resultados")
    args = parser.parse_args()

    if args.usar_markdown_de_results:
        docs = carregar_markdowns_de_results(args.saida)
    elif args.markdowns:
        docs = carregar_markdowns_de_pasta(args.markdowns)
    else:
        raise SystemExit("Use --markdowns <pasta> ou --usar-markdown-de-results")

    rodar_pipeline(docs, args.saida)
