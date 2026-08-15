"""
Funções para gerar embeddings e calcular distâncias entre eles.

Por padrão usa um modelo LOCAL e GRATUITO do Hugging Face
(sentence-transformers), para evitar os problemas de créditos esgotados da
API paga da OpenAI que já aconteceram em aulas anteriores. Pode ser trocado
via .env (EMBEDDING_PROVIDER=openai).
"""

import os
import numpy as np
from dotenv import load_dotenv

load_dotenv()

EMBEDDING_PROVIDER = os.getenv("EMBEDDING_PROVIDER", "huggingface")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2")

_cache = {}


def _hf_model():
    if "hf" not in _cache:
        from sentence_transformers import SentenceTransformer
        print(f"Carregando modelo de embeddings '{EMBEDDING_MODEL}' (Hugging Face, local)...")
        _cache["hf"] = SentenceTransformer(EMBEDDING_MODEL)
    return _cache["hf"]


def _openai_client():
    if "openai" not in _cache:
        from openai import OpenAI
        _cache["openai"] = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    return _cache["openai"]


def get_embedding(texto: str) -> np.ndarray:
    """Gera o embedding de um texto usando o provedor configurado."""
    texto = texto.replace("\n", " ").strip() or " "

    if EMBEDDING_PROVIDER == "huggingface":
        vetor = _hf_model().encode(texto, normalize_embeddings=True)
        return np.array(vetor, dtype=np.float32)

    if EMBEDDING_PROVIDER == "openai":
        model_name = os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small")
        response = _openai_client().embeddings.create(input=[texto], model=model_name)
        return np.array(response.data[0].embedding, dtype=np.float32)

    raise ValueError(f"EMBEDDING_PROVIDER desconhecido: {EMBEDDING_PROVIDER}")


def distancia_euclidiana(vec1: np.ndarray, vec2: np.ndarray) -> float:
    """Distância Euclidiana (norma L2 da diferença) entre dois vetores.

    Fórmula: d(u, v) = sqrt(sum((u_i - v_i)^2))
    Quanto MENOR, mais parecidos.
    """
    vec1, vec2 = np.asarray(vec1), np.asarray(vec2)
    if vec1.shape != vec2.shape:
        raise ValueError("Os dois embeddings devem ter a mesma dimensão.")
    return float(np.linalg.norm(vec1 - vec2))


def similaridade_cosseno(vec1: np.ndarray, vec2: np.ndarray) -> float:
    """Similaridade de Cosseno entre dois vetores.

    Fórmula: cos(theta) = (u . v) / (||u|| * ||v||)
    Quanto MAIOR (perto de 1), mais parecidos.
    """
    vec1, vec2 = np.asarray(vec1), np.asarray(vec2)
    if vec1.shape != vec2.shape:
        raise ValueError("Os dois embeddings devem ter a mesma dimensão.")
    n1, n2 = np.linalg.norm(vec1), np.linalg.norm(vec2)
    if n1 == 0 or n2 == 0:
        return 0.0
    return float(np.dot(vec1, vec2) / (n1 * n2))


def distancia_cosseno(vec1: np.ndarray, vec2: np.ndarray) -> float:
    """Distância de Cosseno (1 - similaridade). Quanto MENOR, mais parecidos."""
    return float(1.0 - similaridade_cosseno(vec1, vec2))
