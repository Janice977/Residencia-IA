"""
Gera uma análise textual comparando as 10 estratégias de chunking, a partir
do results/summary.json produzido pelo pipeline.py.

Uso:
    python analise_comparativa.py --saida results
"""

import os
import json
import argparse


def gerar_analise(pasta_resultados: str = "results") -> str:
    caminho_summary = os.path.join(pasta_resultados, "summary.json")
    with open(caminho_summary, "r", encoding="utf-8") as f:
        summary = json.load(f)

    linhas = ["# Análise Comparativa das Estratégias de Chunking\n"]

    for doc in summary:
        linhas.append(f"## Documento: {doc['document_name']} (`{doc['document_id']}`)\n")
        linhas.append("| Teste | Estratégia | Tamanho | Overlap | Nº Chunks | Média | Mín | Máx | Desvio Padrão |")
        linhas.append("|---|---|---|---|---|---|---|---|---|")

        experimentos = doc["experiments"]
        for e in experimentos:
            linhas.append(
                f"| {e['test_id']} | {e['strategy']} | {e.get('chunk_size', '-')} | "
                f"{e.get('chunk_overlap', '-')} | {e['num_chunks']} | {e['avg_chunk_size']} | "
                f"{e['min_chunk_size']} | {e['max_chunk_size']} | {e['stdev_chunk_size']} |"
            )

        mais_chunks = max(experimentos, key=lambda e: e["num_chunks"])
        menos_chunks = min(experimentos, key=lambda e: e["num_chunks"])
        maior_media = max(experimentos, key=lambda e: e["avg_chunk_size"])
        menor_media = min(experimentos, key=lambda e: e["avg_chunk_size"])

        linhas.append("")
        linhas.append(f"- **Estratégia que gerou MAIS chunks**: Teste {mais_chunks['test_id']} "
                       f"({mais_chunks['strategy']}, {mais_chunks['num_chunks']} chunks)")
        linhas.append(f"- **Estratégia que gerou MENOS chunks**: Teste {menos_chunks['test_id']} "
                       f"({menos_chunks['strategy']}, {menos_chunks['num_chunks']} chunks)")
        linhas.append(f"- **Maior tamanho médio de chunk**: Teste {maior_media['test_id']} "
                       f"({maior_media['strategy']}, {maior_media['avg_chunk_size']} caracteres)")
        linhas.append(f"- **Menor tamanho médio de chunk**: Teste {menor_media['test_id']} "
                       f"({menor_media['strategy']}, {menor_media['avg_chunk_size']} caracteres)")
        linhas.append("")

    texto = "\n".join(linhas)

    caminho_saida = os.path.join(pasta_resultados, "analise_comparativa.md")
    with open(caminho_saida, "w", encoding="utf-8") as f:
        f.write(texto)

    print(f"Análise salva em {caminho_saida}")
    return texto


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--saida", default="results", help="Pasta raiz de resultados")
    args = parser.parse_args()

    gerar_analise(args.saida)
