"""
Geração de embeddings para os chunks.

Por padrão usa um modelo local do Hugging Face (sentence-transformers), que é
GRATUITO e roda sem precisar de API paga — evita o problema de créditos
esgotados da OpenAI que aconteceu nas aulas anteriores.

Para trocar de modelo, basta mudar a variável EMBEDDING_MODEL (ou a variável
de ambiente EMBEDDING_MODEL) e, se necessário, o EMBEDDING_PROVIDER.

Referência: https://huggingface.co/blog/getting-started-with-embeddings
"""

import os
from dotenv import load_dotenv

load_dotenv()

# "huggingface" (padrão, local e gratuito) ou "openai" (paga, precisa de créditos)
EMBEDDING_PROVIDER = os.getenv("EMBEDDING_PROVIDER", "huggingface")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2")

_model_cache = {}


def _get_hf_model():
    """Carrega (uma única vez) o modelo do sentence-transformers."""
    if "hf" not in _model_cache:
        from sentence_transformers import SentenceTransformer
        print(f"Carregando modelo de embeddings '{EMBEDDING_MODEL}' (Hugging Face, local)...")
        _model_cache["hf"] = SentenceTransformer(EMBEDDING_MODEL)
    return _model_cache["hf"]


def _get_openai_client():
    if "openai" not in _model_cache:
        from openai import OpenAI
        _model_cache["openai"] = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    return _model_cache["openai"]


def get_embedding(texto: str) -> list[float]:
    """Gera o embedding de um texto usando o provedor configurado."""
    texto = texto.replace("\n", " ").strip()
    if not texto:
        texto = " "

    if EMBEDDING_PROVIDER == "huggingface":
        model = _get_hf_model()
        vetor = model.encode(texto, normalize_embeddings=True)
        return vetor.tolist()

    if EMBEDDING_PROVIDER == "openai":
        client = _get_openai_client()
        response = client.embeddings.create(input=[texto], model=EMBEDDING_MODEL)
        return response.data[0].embedding

    raise ValueError(f"EMBEDDING_PROVIDER desconhecido: {EMBEDDING_PROVIDER}")


def get_embeddings_batch(textos: list[str]) -> list[list[float]]:
    """Gera embeddings para uma lista de textos de uma vez (mais rápido no HuggingFace)."""
    textos = [t.replace("\n", " ").strip() or " " for t in textos]

    if EMBEDDING_PROVIDER == "huggingface":
        model = _get_hf_model()
        vetores = model.encode(textos, normalize_embeddings=True, show_progress_bar=False)
        return [v.tolist() for v in vetores]

    # Fallback genérico (um por vez) para outros provedores
    return [get_embedding(t) for t in textos]
