# ==============================================================================
# RESIDÊNCIA IA - AULA 05: Documents, Metadados e Busca Vetorial com LangChain
# ==============================================================================

import json
from typing import List
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

documentos: List[Document] = [
    Document(
        page_content="Embeddings são representações vetoriais densas de texto.",
        metadata={"fonte": "introducao_ia.md", "pagina": 1, "tipo": "teoria", "tema": "embeddings"}
    ),
    Document(
        page_content="O chunking divide textos extensos em blocos menores para o RAG.",
        metadata={"fonte": "chunking_guide.md", "pagina": 2, "tipo": "pratica", "tema": "chunking"}
    ),
    Document(
        page_content="A arquitetura RAG combina recuperação vetorial com LLMs.",
        metadata={"fonte": "rag_architecture.md", "pagina": 5, "tipo": "teoria", "tema": "RAG"}
    ),
    Document(
        page_content="A tokenização converte texto bruto em sequências numéricas.",
        metadata={"fonte": "tokenizacao.md", "pagina": 1, "tipo": "conceito", "tema": "tokenizacao"}
    ),
    Document(
        page_content="Busca vetorial utiliza similaridade de cosseno para ranquear chunks.",
        metadata={"fonte": "busca_vetorial.md", "pagina": 3, "tipo": "algoritmo", "tema": "embeddings"}
    )
]

for i, doc in enumerate(documentos, 1):
    print(f"\n[Documento {i}]\npage_content: \"{doc.page_content}\"\nmetadata: {doc.metadata}")

print(f"\nTotal de documentos: {len(documentos)}")
