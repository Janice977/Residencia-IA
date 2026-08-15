"""
Compara uma frase âncora com 4 frases de categorias diferentes:
similar, relacionado, domínio diferente e oposto/negação.

O objetivo é ver como a Distância Euclidiana e a Similaridade/Distância de
Cosseno se comportam à medida que o significado se afasta da frase âncora.
"""

import numpy as np
import pandas as pd
from embeddings_utils import get_embedding, distancia_euclidiana, distancia_cosseno, similaridade_cosseno

frase_ancora = "O cachorro correu no parque e brincou com a bola."

frases_comparacao = [
    ("Similar (mesmo sentido, palavras diferentes)",
     "Um cão estava correndo no jardim e brincando com seu brinquedo."),
    ("Relacionado (mesmo contexto de animais)",
     "O gato dormiu na almofada da sala durante toda a tarde."),
    ("Diferente (outro domínio - economia)",
     "A taxa de juros do banco central subiu dois pontos percentuais."),
    ("Oposto/Negação",
     "Nenhum animal esteve no parque e o cão permaneceu preso em casa."),
]


def rodar():
    print("Gerando embedding da frase âncora...")
    vec_ancora = get_embedding(frase_ancora)

    print("Gerando embeddings das frases de comparação...")
    resultados = []
    for categoria, frase in frases_comparacao:
        vec = get_embedding(frase)
        resultados.append({
            "Categoria": categoria,
            "Frase": frase,
            "Dist. Euclidiana": round(distancia_euclidiana(vec_ancora, vec), 4),
            "Similaridade Cosseno": round(similaridade_cosseno(vec_ancora, vec), 4),
            "Distância Cosseno": round(distancia_cosseno(vec_ancora, vec), 4),
        })

    df = pd.DataFrame(resultados)
    print(f"\nFrase âncora: \"{frase_ancora}\"\n")
    print(df.to_string(index=False))
    return df


if __name__ == "__main__":
    rodar()
