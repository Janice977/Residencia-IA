"""
Busca Semântica Simples (manual, embedding por embedding).

Lê os arquivos .md gerados na Aula 02 (pasta aula_2/), divide o texto em
3 granularidades diferentes (linha, parágrafo, capítulo), gera embeddings
e retorna o TOP 3 trechos mais similares a uma pergunta, para cada nível.
"""

import os
import glob
import pandas as pd
from embeddings_utils import get_embedding, similaridade_cosseno

PASTA_DOCUMENTOS = "aula_2"


def carregar_arquivos_md(pasta: str = PASTA_DOCUMENTOS) -> dict:
    arquivos = {}
    for caminho in glob.glob(os.path.join(pasta, "*.md")):
        with open(caminho, "r", encoding="utf-8") as f:
            arquivos[os.path.basename(caminho)] = f.read()
    return arquivos


def dividir_por_linha(texto: str) -> list[str]:
    return [l.strip() for l in texto.split("\n") if l.strip()]


def dividir_por_paragrafo(texto: str) -> list[str]:
    return [p.strip() for p in texto.split("\n\n") if p.strip()]


def dividir_por_capitulo(texto: str) -> list[str]:
    capitulos, atual = [], []
    for linha in texto.split("\n"):
        if linha.startswith("#") and atual:
            capitulos.append("\n".join(atual).strip())
            atual = [linha]
        else:
            atual.append(linha)
    if atual:
        capitulos.append("\n".join(atual).strip())
    return [c for c in capitulos if c]


ESTRATEGIAS = {"linha": dividir_por_linha, "paragrafo": dividir_por_paragrafo, "capitulo": dividir_por_capitulo}


def montar_trechos(pasta: str = PASTA_DOCUMENTOS, estrategia: str = "linha") -> list[dict]:
    dividir = ESTRATEGIAS[estrategia]
    trechos = []
    for nome_arquivo, conteudo in carregar_arquivos_md(pasta).items():
        for trecho in dividir(conteudo):
            trechos.append({"arquivo": nome_arquivo, "texto": trecho})
    return trechos


def buscar(query: str, trechos: list[dict], top_k: int = 3) -> pd.DataFrame:
    if not trechos:
        raise ValueError("Nenhum trecho encontrado. Verifique a pasta 'aula_2/'.")

    vec_query = get_embedding(query)

    resultados = []
    for trecho in trechos:
        vec_trecho = get_embedding(trecho["texto"])
        score = similaridade_cosseno(vec_query, vec_trecho)
        resultados.append({
            "arquivo": trecho["arquivo"],
            "trecho": trecho["texto"][:200],
            "score": round(score, 4),
        })

    df = pd.DataFrame(resultados).sort_values("score", ascending=False)
    return df.head(top_k).reset_index(drop=True)


if __name__ == "__main__":
    perguntas = [
        "O que é Autonomia e opacidade algorítmica?",
        "O que é o diário de bordo da IA?",
    ]

    for estrategia in ["linha", "paragrafo", "capitulo"]:
        print(f"\n{'=' * 60}")
        print(f"Estratégia de divisão: {estrategia.upper()}")
        print("=" * 60)

        trechos = montar_trechos(estrategia=estrategia)
        print(f"Total de trechos gerados: {len(trechos)}")

        for pergunta in perguntas:
            print(f"\nPergunta: {pergunta}")
            top3 = buscar(pergunta, trechos, top_k=3)
            print(top3.to_string(index=False))
