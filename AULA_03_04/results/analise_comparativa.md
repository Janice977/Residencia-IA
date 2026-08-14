# Análise Comparativa das Estratégias de Chunking

## Documento: bioetica_e_ia.pdf (`bioetica_e_ia`)

| Teste | Estratégia | Tamanho | Overlap | Nº Chunks | Média | Mín | Máx | Desvio Padrão |
|---|---|---|---|---|---|---|---|---|
| 1 | fixed | 200 | 0 | 257 | 198.93 | 13 | 200 | 11.66 |
| 2 | fixed | 500 | 0 | 103 | 496.83 | 213 | 500 | 28.25 |
| 3 | fixed | 1000 | 0 | 52 | 984.5 | 213 | 1000 | 109.09 |
| 4 | fixed | 2000 | 0 | 26 | 1969.42 | 1211 | 2000 | 154.69 |
| 5 | fixed_overlap | 500 | 50 | 114 | 498.49 | 363 | 500 | 12.81 |
| 6 | fixed_overlap | 500 | 200 | 171 | 497.95 | 213 | 500 | 21.93 |
| 7 | paragraph | None | 0 | 135 | 377.37 | 3 | 4291 | 473.02 |
| 8 | sentence_group | None | 0 | 139 | 366.58 | 38 | 1088 | 264.57 |
| 9 | recursive | 1000 | 100 | 73 | 704.84 | 192 | 995 | 225.87 |
| 10 | markdown_headers | None | 0 | 25 | 2049.76 | 10 | 8596 | 2079.16 |

- **Estratégia que gerou MAIS chunks**: Teste 1 (fixed, 257 chunks)
- **Estratégia que gerou MENOS chunks**: Teste 10 (markdown_headers, 25 chunks)
- **Maior tamanho médio de chunk**: Teste 10 (markdown_headers, 2049.76 caracteres)
- **Menor tamanho médio de chunk**: Teste 1 (fixed, 198.93 caracteres)

## Documento: escrita_academica_ia.pdf (`escrita_academica_ia`)

| Teste | Estratégia | Tamanho | Overlap | Nº Chunks | Média | Mín | Máx | Desvio Padrão |
|---|---|---|---|---|---|---|---|---|
| 1 | fixed | 200 | 0 | 212 | 196.92 | 23 | 200 | 16.65 |
| 2 | fixed | 500 | 0 | 86 | 486.37 | 63 | 500 | 60.85 |
| 3 | fixed | 1000 | 0 | 43 | 978.86 | 563 | 1000 | 81.87 |
| 4 | fixed | 2000 | 0 | 22 | 1939.55 | 678 | 2000 | 281.77 |
| 5 | fixed_overlap | 500 | 50 | 95 | 490.05 | 156 | 500 | 45.25 |
| 6 | fixed_overlap | 500 | 200 | 142 | 492.89 | 156 | 500 | 42.06 |
| 7 | paragraph | None | 0 | 116 | 365.93 | 2 | 2674 | 485.23 |
| 8 | sentence_group | None | 0 | 99 | 425.97 | 5 | 1668 | 259.65 |
| 9 | recursive | 1000 | 100 | 60 | 714.9 | 141 | 993 | 219.32 |
| 10 | markdown_headers | None | 0 | 20 | 2136.8 | 16 | 6175 | 1924.15 |

- **Estratégia que gerou MAIS chunks**: Teste 1 (fixed, 212 chunks)
- **Estratégia que gerou MENOS chunks**: Teste 10 (markdown_headers, 20 chunks)
- **Maior tamanho médio de chunk**: Teste 10 (markdown_headers, 2136.8 caracteres)
- **Menor tamanho médio de chunk**: Teste 1 (fixed, 196.92 caracteres)

## Documento: twitter_algoritmo.pdf (`twitter_algoritmo`)

| Teste | Estratégia | Tamanho | Overlap | Nº Chunks | Média | Mín | Máx | Desvio Padrão |
|---|---|---|---|---|---|---|---|---|
| 1 | fixed | 200 | 0 | 273 | 198.93 | 40 | 200 | 9.68 |
| 2 | fixed | 500 | 0 | 109 | 498.92 | 440 | 500 | 5.73 |
| 3 | fixed | 1000 | 0 | 55 | 989.31 | 440 | 1000 | 75.44 |
| 4 | fixed | 2000 | 0 | 28 | 1943.68 | 440 | 2000 | 294.69 |
| 5 | fixed_overlap | 500 | 50 | 121 | 499.13 | 440 | 500 | 5.46 |
| 6 | fixed_overlap | 500 | 200 | 181 | 499.25 | 440 | 500 | 4.48 |
| 7 | paragraph | None | 0 | 196 | 275.77 | 1 | 1386 | 317.9 |
| 8 | sentence_group | None | 0 | 140 | 386.76 | 15 | 1049 | 274.83 |
| 9 | recursive | 1000 | 100 | 78 | 707.94 | 65 | 996 | 250.86 |
| 10 | markdown_headers | None | 0 | 22 | 2480.55 | 73 | 9877 | 3176.8 |

- **Estratégia que gerou MAIS chunks**: Teste 1 (fixed, 273 chunks)
- **Estratégia que gerou MENOS chunks**: Teste 10 (markdown_headers, 22 chunks)
- **Maior tamanho médio de chunk**: Teste 10 (markdown_headers, 2480.55 caracteres)
- **Menor tamanho médio de chunk**: Teste 1 (fixed, 198.93 caracteres)
