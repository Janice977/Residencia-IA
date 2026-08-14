"""
Reconstrói o results/summary.json a partir dos arquivos chunks_embeddings.json
já existentes em results/<document_id>/test_XX/. Útil caso o summary.json
tenha sido perdido/sobrescrito, sem precisar rodar o pipeline (e gerar
embeddings) de novo.

Uso:
    python reconstruir_summary.py --saida results
"""

import os
import json
import glob
import argparse
import statistics


def reconstruir(pasta_resultados: str = "results") -> None:
    summary = {}

    caminhos = sorted(glob.glob(os.path.join(pasta_resultados, "*", "test_*", "chunks_embeddings.json")))
    if not caminhos:
        print(f"Nenhum chunks_embeddings.json encontrado em '{pasta_resultados}/'.")
        return

    for caminho in caminhos:
        with open(caminho, "r", encoding="utf-8") as f:
            registros = json.load(f)
        if not registros:
            continue

        document_id = registros[0]["document_id"]
        document_name = registros[0]["document_name"]

        tamanhos = [len(r["text"]) for r in registros]
        stat = {
            "test_id": registros[0]["test_id"],
            "strategy": registros[0]["strategy"],
            "chunk_size": registros[0].get("chunk_size"),
            "chunk_overlap": registros[0].get("chunk_overlap"),
            "num_chunks": len(registros),
            "avg_chunk_size": round(statistics.mean(tamanhos), 2),
            "min_chunk_size": min(tamanhos),
            "max_chunk_size": max(tamanhos),
            "stdev_chunk_size": round(statistics.stdev(tamanhos), 2) if len(tamanhos) > 1 else 0.0,
            "embedding_dimension": len(registros[0]["embedding"]),
        }

        if document_id not in summary:
            summary[document_id] = {"document_id": document_id, "document_name": document_name, "experiments": []}
        summary[document_id]["experiments"].append(stat)

    resultado = list(summary.values())
    for doc in resultado:
        doc["experiments"].sort(key=lambda e: e["test_id"])

    caminho_saida = os.path.join(pasta_resultados, "summary.json")
    with open(caminho_saida, "w", encoding="utf-8") as f:
        json.dump(resultado, f, ensure_ascii=False, indent=2)

    print(f"summary.json reconstruído com {len(resultado)} documento(s) em {caminho_saida}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--saida", default="results", help="Pasta raiz de resultados")
    args = parser.parse_args()
    reconstruir(args.saida)
