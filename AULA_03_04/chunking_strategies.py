"""
Define as 10 estratégias de chunking exigidas pela atividade, usando os
splitters do LangChain sempre que existir um equivalente pronto na biblioteca.

Cada estratégia é uma função que recebe o texto (markdown) e retorna uma lista
de dicts: [{"text": str, "metadata": dict}, ...]
"""

import re
import logging

# O CharacterTextSplitter avisa (warning) sempre que um pedaço fica maior que
# o chunk_size configurado. Usamos chunk_size=1 de propósito em
# chunk_paragraph() para preservar cada parágrafo inteiro, então esse aviso é
# esperado e não indica um problema — silenciamos para não poluir a saída.
logging.getLogger("langchain_text_splitters.base").setLevel(logging.ERROR)

from langchain_text_splitters import (
    CharacterTextSplitter,
    RecursiveCharacterTextSplitter,
    MarkdownHeaderTextSplitter,
)

# ---------------------------------------------------------------------------
# Configuração dos 10 testes (conforme especificado na atividade)
# ---------------------------------------------------------------------------
TESTES = {
    1: {"strategy": "fixed", "chunk_size": 200, "chunk_overlap": 0},
    2: {"strategy": "fixed", "chunk_size": 500, "chunk_overlap": 0},
    3: {"strategy": "fixed", "chunk_size": 1000, "chunk_overlap": 0},
    4: {"strategy": "fixed", "chunk_size": 2000, "chunk_overlap": 0},
    5: {"strategy": "fixed_overlap", "chunk_size": 500, "chunk_overlap": 50},
    6: {"strategy": "fixed_overlap", "chunk_size": 500, "chunk_overlap": 200},
    7: {"strategy": "paragraph", "chunk_size": None, "chunk_overlap": 0},
    8: {"strategy": "sentence_group", "chunk_size": None, "chunk_overlap": 0, "sentencas_por_chunk": 3},
    9: {"strategy": "recursive", "chunk_size": 1000, "chunk_overlap": 100},
    10: {"strategy": "markdown_headers", "chunk_size": None, "chunk_overlap": 0},
}


def _docs_to_chunks(docs) -> list[dict]:
    """Converte a saída dos splitters do LangChain (Document) para nosso formato."""
    return [{"text": d.page_content, "metadata": dict(d.metadata)} for d in docs if d.page_content.strip()]


# ---------------------------------------------------------------------------
# Testes 1 a 4 — chunking fixo (sem overlap), variando tamanho
# Testes 5 e 6 — chunking fixo com overlap
# Usamos CharacterTextSplitter com separator="" para forçar corte puro por
# quantidade de caracteres (sem respeitar nenhuma estrutura do texto).
# ---------------------------------------------------------------------------
def chunk_fixed(texto: str, chunk_size: int, chunk_overlap: int = 0) -> list[dict]:
    splitter = CharacterTextSplitter(
        separator="",
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )
    return _docs_to_chunks(splitter.create_documents([texto]))


# ---------------------------------------------------------------------------
# Teste 7 — por parágrafo (separador "\n\n")
# ---------------------------------------------------------------------------
def chunk_paragraph(texto: str) -> list[dict]:
    # chunk_size=1 evita que o splitter remonte parágrafos adjacentes em um
    # único chunk (o CharacterTextSplitter junta pedaços até atingir
    # chunk_size); com o valor mínimo, cada parágrafo vira seu próprio chunk.
    splitter = CharacterTextSplitter(
        separator="\n\n",
        chunk_size=1,
        chunk_overlap=0,
    )
    return _docs_to_chunks(splitter.create_documents([texto]))


# ---------------------------------------------------------------------------
# Teste 8 — sentenças agrupadas de 3 em 3
# Não existe um splitter pronto no LangChain para "agrupar N sentenças", então
# implementamos manualmente: separamos por pontuação de fim de frase e
# agrupamos.
# ---------------------------------------------------------------------------
def chunk_sentence_group(texto: str, sentencas_por_chunk: int = 3) -> list[dict]:
    # Divide em sentenças (mantendo a pontuação final)
    sentencas = re.split(r"(?<=[.!?])\s+", texto.strip())
    sentencas = [s.strip() for s in sentencas if s.strip()]

    chunks = []
    for i in range(0, len(sentencas), sentencas_por_chunk):
        grupo = sentencas[i:i + sentencas_por_chunk]
        chunks.append({
            "text": " ".join(grupo),
            "metadata": {"sentencas_no_grupo": len(grupo)},
        })
    return chunks


# ---------------------------------------------------------------------------
# Teste 9 — Recursive Character Text Splitter (separadores hierárquicos)
# ---------------------------------------------------------------------------
def chunk_recursive(texto: str, chunk_size: int = 1000, chunk_overlap: int = 100) -> list[dict]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ". ", " ", ""],  # parágrafo -> linha -> frase -> espaço -> caractere
    )
    return _docs_to_chunks(splitter.create_documents([texto]))


# ---------------------------------------------------------------------------
# Teste 10 — Markdown Header Text Splitter (estrutura semântica por heading)
# ---------------------------------------------------------------------------
def chunk_markdown_headers(texto: str) -> list[dict]:
    headers_to_split_on = [
        ("#", "h1"),
        ("##", "h2"),
        ("###", "h3"),
    ]
    splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on, strip_headers=False)
    docs = splitter.split_text(texto)
    return _docs_to_chunks(docs)


# ---------------------------------------------------------------------------
# Função principal: roda um teste específico (1 a 10) sobre um texto
# ---------------------------------------------------------------------------
def rodar_teste(test_id: int, texto: str) -> list[dict]:
    config = TESTES[test_id]
    estrategia = config["strategy"]

    if estrategia == "fixed":
        return chunk_fixed(texto, config["chunk_size"], config["chunk_overlap"])
    if estrategia == "fixed_overlap":
        return chunk_fixed(texto, config["chunk_size"], config["chunk_overlap"])
    if estrategia == "paragraph":
        return chunk_paragraph(texto)
    if estrategia == "sentence_group":
        return chunk_sentence_group(texto, config["sentencas_por_chunk"])
    if estrategia == "recursive":
        return chunk_recursive(texto, config["chunk_size"], config["chunk_overlap"])
    if estrategia == "markdown_headers":
        return chunk_markdown_headers(texto)

    raise ValueError(f"Estratégia desconhecida: {estrategia}")
