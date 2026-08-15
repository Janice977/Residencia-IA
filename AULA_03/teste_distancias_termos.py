"""
Item 3 do enunciado — Testando as funções.

Parte A: exemplo numérico simples (vetores prontos, sem precisar gerar
embedding nenhum) — serve para validar a matemática das funções.

Parte B: embeddings reais de termos (gato, felino, cachorro, carro,
caminhão, moto, banana, maçã, goiaba), para ver o comportamento das
distâncias com significado semântico de verdade.
"""

import numpy as np
import pandas as pd
from embeddings_utils import get_embedding, distancia_euclidiana, distancia_cosseno, similaridade_cosseno

# ---------------------------------------------------------------------------
# Parte A — exemplo numérico do enunciado
# ---------------------------------------------------------------------------
print("=" * 60)
print("PARTE A — Exemplo numérico (vetores prontos)")
print("=" * 60)

embedding_a = np.array([1, 0, 0])
embedding_b = np.array([0, 1, 0])
embedding_c = np.array([1, 0, 0])

pares_numericos = [("a", "b", embedding_a, embedding_b),
                   ("a", "c", embedding_a, embedding_c),
                   ("b", "c", embedding_b, embedding_c)]

resultados_numericos = []
for nome1, nome2, v1, v2 in pares_numericos:
    resultados_numericos.append({
        "Par": f"{nome1}-{nome2}",
        "Dist. Euclidiana": round(distancia_euclidiana(v1, v2), 4),
        "Similaridade Cosseno": round(similaridade_cosseno(v1, v2), 4),
        "Distância Cosseno": round(distancia_cosseno(v1, v2), 4),
    })

print(pd.DataFrame(resultados_numericos).to_string(index=False))
print()
print("Interpretação: a e c são idênticos (distância 0); a e b, b e c são")
print("ortogonais entre si (distância euclidiana máxima nesse espaço, cosseno = 1).")

# ---------------------------------------------------------------------------
# Parte B — embeddings reais de termos
# ---------------------------------------------------------------------------
print()
print("=" * 60)
print("PARTE B — Embeddings reais de termos")
print("=" * 60)

termos = ["gato", "felino", "cachorro", "carro", "caminhão", "moto", "banana", "maçã", "goiaba"]
print("Gerando embeddings...")
embeddings = {termo: get_embedding(termo) for termo in termos}

pares_termos = [
    ("gato", "felino"),     # sinônimos -> esperado: bem parecidos
    ("gato", "cachorro"),   # mesma categoria (animais)
    ("gato", "carro"),      # categorias diferentes
    ("carro", "caminhão"),  # mesma categoria (veículos)
    ("carro", "moto"),      # mesma categoria (veículos)
    ("banana", "maçã"),     # mesma categoria (frutas)
    ("banana", "goiaba"),   # mesma categoria (frutas)
    ("gato", "banana"),     # categorias diferentes
    ("gato", "gato"),       # idênticos
]

resultados_termos = []
for termo_a, termo_b in pares_termos:
    va, vb = embeddings[termo_a], embeddings[termo_b]
    resultados_termos.append({
        "Termo A": termo_a,
        "Termo B": termo_b,
        "Dist. Euclidiana": round(distancia_euclidiana(va, vb), 4),
        "Similaridade Cosseno": round(similaridade_cosseno(va, vb), 4),
        "Distância Cosseno": round(distancia_cosseno(va, vb), 4),
    })

print(pd.DataFrame(resultados_termos).to_string(index=False))
