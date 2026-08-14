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

## Documento: attention_is_all_you_need.pdf (`attention_is_all_you_need`)

| Teste | Estratégia | Tamanho | Overlap | Nº Chunks | Média | Mín | Máx | Desvio Padrão |
|---|---|---|---|---|---|---|---|---|
| 1 | fixed | 200 | 0 | 245 | 192.89 | 117 | 200 | 15.54 |
| 2 | fixed | 500 | 0 | 98 | 492.66 | 425 | 500 | 16.2 |
| 3 | fixed | 1000 | 0 | 49 | 993.2 | 937 | 1000 | 15.68 |
| 4 | fixed | 2000 | 0 | 25 | 1951.04 | 956 | 2000 | 207.97 |
| 5 | fixed_overlap | 500 | 50 | 109 | 491.54 | 357 | 500 | 21.04 |
| 6 | fixed_overlap | 500 | 200 | 163 | 492.3 | 357 | 500 | 19.31 |
| 7 | paragraph | None | 0 | 128 | 380.49 | 11 | 9327 | 921.82 |
| 8 | sentence_group | None | 0 | 130 | 375.03 | 18 | 9713 | 844.12 |
| 9 | recursive | 1000 | 100 | 66 | 752.27 | 165 | 998 | 197.11 |
| 10 | markdown_headers | None | 0 | 28 | 1750.11 | 12 | 10946 | 2278.97 |

- **Estratégia que gerou MAIS chunks**: Teste 1 (fixed, 245 chunks)
- **Estratégia que gerou MENOS chunks**: Teste 4 (fixed, 25 chunks)
- **Maior tamanho médio de chunk**: Teste 4 (fixed, 1951.04 caracteres)
- **Menor tamanho médio de chunk**: Teste 1 (fixed, 192.89 caracteres)

## Documento: bert_pretraining.pdf (`bert_pretraining`)

| Teste | Estratégia | Tamanho | Overlap | Nº Chunks | Média | Mín | Máx | Desvio Padrão |
|---|---|---|---|---|---|---|---|---|
| 1 | fixed | 200 | 0 | 352 | 197.32 | 35 | 200 | 10.79 |
| 2 | fixed | 500 | 0 | 141 | 496.12 | 234 | 500 | 22.9 |
| 3 | fixed | 1000 | 0 | 71 | 987.75 | 234 | 1000 | 90.9 |
| 4 | fixed | 2000 | 0 | 36 | 1950.22 | 234 | 2000 | 294.21 |
| 5 | fixed_overlap | 500 | 50 | 156 | 497.53 | 440 | 500 | 8.09 |
| 6 | fixed_overlap | 500 | 200 | 234 | 497.38 | 335 | 500 | 12.42 |
| 7 | paragraph | None | 0 | 196 | 356.35 | 1 | 9371 | 742.08 |
| 8 | sentence_group | None | 0 | 204 | 342.74 | 22 | 3561 | 339.18 |
| 9 | recursive | 1000 | 100 | 95 | 746.83 | 88 | 997 | 233.66 |
| 10 | markdown_headers | None | 0 | 33 | 2131.33 | 32 | 11380 | 2327.32 |

- **Estratégia que gerou MAIS chunks**: Teste 1 (fixed, 352 chunks)
- **Estratégia que gerou MENOS chunks**: Teste 10 (markdown_headers, 33 chunks)
- **Maior tamanho médio de chunk**: Teste 10 (markdown_headers, 2131.33 caracteres)
- **Menor tamanho médio de chunk**: Teste 1 (fixed, 197.32 caracteres)

## Documento: gpt3_language_models.pdf (`gpt3_language_models`)

| Teste | Estratégia | Tamanho | Overlap | Nº Chunks | Média | Mín | Máx | Desvio Padrão |
|---|---|---|---|---|---|---|---|---|
| 1 | fixed | 200 | 0 | 1542 | 181.95 | 1 | 200 | 47.5 |
| 2 | fixed | 500 | 0 | 660 | 442.08 | 1 | 500 | 140.27 |
| 3 | fixed | 1000 | 0 | 334 | 924.49 | 30 | 1000 | 182.75 |
| 4 | fixed | 2000 | 0 | 167 | 1925.05 | 1057 | 2000 | 185.93 |
| 5 | fixed_overlap | 500 | 50 | 737 | 439.47 | 1 | 500 | 142.75 |
| 6 | fixed_overlap | 500 | 200 | 1103 | 438.65 | 1 | 500 | 144.9 |
| 7 | paragraph | None | 0 | 592 | 561.89 | 1 | 40445 | 2093.13 |
| 8 | sentence_group | None | 0 | 653 | 499.23 | 5 | 24979 | 1235.24 |
| 9 | recursive | 1000 | 100 | 462 | 724.6 | 1 | 999 | 257.14 |
| 10 | markdown_headers | None | 0 | 57 | 5863.95 | 318 | 52364 | 9565.49 |

- **Estratégia que gerou MAIS chunks**: Teste 1 (fixed, 1542 chunks)
- **Estratégia que gerou MENOS chunks**: Teste 10 (markdown_headers, 57 chunks)
- **Maior tamanho médio de chunk**: Teste 10 (markdown_headers, 5863.95 caracteres)
- **Menor tamanho médio de chunk**: Teste 1 (fixed, 181.95 caracteres)

## Documento: gpt4_technical_report.pdf (`gpt4_technical_report`)

| Teste | Estratégia | Tamanho | Overlap | Nº Chunks | Média | Mín | Máx | Desvio Padrão |
|---|---|---|---|---|---|---|---|---|
| 1 | fixed | 200 | 0 | 1440 | 197.24 | 9 | 200 | 13.29 |
| 2 | fixed | 500 | 0 | 579 | 494.96 | 16 | 500 | 32.73 |
| 3 | fixed | 1000 | 0 | 290 | 993.28 | 475 | 1000 | 43.94 |
| 4 | fixed | 2000 | 0 | 145 | 1988.37 | 1475 | 2000 | 61.99 |
| 5 | fixed_overlap | 500 | 50 | 644 | 494.43 | 16 | 500 | 33.8 |
| 6 | fixed_overlap | 500 | 200 | 964 | 494.68 | 16 | 500 | 31.32 |
| 7 | paragraph | None | 0 | 1036 | 277.48 | 1 | 9536 | 598.06 |
| 8 | sentence_group | None | 0 | 956 | 301.33 | 15 | 17455 | 747.3 |
| 9 | recursive | 1000 | 100 | 395 | 744.58 | 3 | 997 | 233.56 |
| 10 | markdown_headers | None | 0 | 212 | 1367.66 | 9 | 23342 | 3079.32 |

- **Estratégia que gerou MAIS chunks**: Teste 1 (fixed, 1440 chunks)
- **Estratégia que gerou MENOS chunks**: Teste 4 (fixed, 145 chunks)
- **Maior tamanho médio de chunk**: Teste 4 (fixed, 1988.37 caracteres)
- **Menor tamanho médio de chunk**: Teste 1 (fixed, 197.24 caracteres)

## Documento: instruct_gpt.pdf (`instruct_gpt`)

| Teste | Estratégia | Tamanho | Overlap | Nº Chunks | Média | Mín | Máx | Desvio Padrão |
|---|---|---|---|---|---|---|---|---|
| 1 | fixed | 200 | 0 | 1083 | 188.72 | 2 | 200 | 35.31 |
| 2 | fixed | 500 | 0 | 438 | 480.74 | 9 | 500 | 66.13 |
| 3 | fixed | 1000 | 0 | 221 | 965.73 | 9 | 1000 | 122.33 |
| 4 | fixed | 2000 | 0 | 111 | 1946.36 | 9 | 2000 | 225.54 |
| 5 | fixed_overlap | 500 | 50 | 485 | 482.2 | 11 | 500 | 66.35 |
| 6 | fixed_overlap | 500 | 200 | 729 | 482.55 | 11 | 500 | 63.34 |
| 7 | paragraph | None | 0 | 625 | 350.02 | 3 | 8855 | 719.9 |
| 8 | sentence_group | None | 0 | 547 | 394.01 | 25 | 9209 | 522.71 |
| 9 | recursive | 1000 | 100 | 292 | 756.5 | 1 | 999 | 231.39 |
| 10 | markdown_headers | None | 0 | 129 | 1707.36 | 12 | 18227 | 2951.18 |

- **Estratégia que gerou MAIS chunks**: Teste 1 (fixed, 1083 chunks)
- **Estratégia que gerou MENOS chunks**: Teste 4 (fixed, 111 chunks)
- **Maior tamanho médio de chunk**: Teste 4 (fixed, 1946.36 caracteres)
- **Menor tamanho médio de chunk**: Teste 1 (fixed, 188.72 caracteres)

## Documento: llama_foundation_models.pdf (`llama_foundation_models`)

| Teste | Estratégia | Tamanho | Overlap | Nº Chunks | Média | Mín | Máx | Desvio Padrão |
|---|---|---|---|---|---|---|---|---|
| 1 | fixed | 200 | 0 | 524 | 193.06 | 9 | 200 | 27.42 |
| 2 | fixed | 500 | 0 | 211 | 487.29 | 21 | 500 | 53.77 |
| 3 | fixed | 1000 | 0 | 106 | 982.26 | 322 | 1000 | 79.97 |
| 4 | fixed | 2000 | 0 | 53 | 1977.32 | 1322 | 2000 | 99.55 |
| 5 | fixed_overlap | 500 | 50 | 234 | 492.45 | 268 | 500 | 28.83 |
| 6 | fixed_overlap | 500 | 200 | 351 | 492.12 | 322 | 500 | 28.59 |
| 7 | paragraph | None | 0 | 281 | 372.82 | 7 | 12468 | 1072.62 |
| 8 | sentence_group | None | 0 | 303 | 337.87 | 16 | 11756 | 699.85 |
| 9 | recursive | 1000 | 100 | 142 | 751.62 | 94 | 998 | 228.22 |
| 10 | markdown_headers | None | 0 | 54 | 1952.65 | 97 | 21339 | 3260.38 |

- **Estratégia que gerou MAIS chunks**: Teste 1 (fixed, 524 chunks)
- **Estratégia que gerou MENOS chunks**: Teste 4 (fixed, 53 chunks)
- **Maior tamanho médio de chunk**: Teste 4 (fixed, 1977.32 caracteres)
- **Menor tamanho médio de chunk**: Teste 1 (fixed, 193.06 caracteres)

## Documento: lora_low_rank_adaptation.pdf (`lora_low_rank_adaptation`)

| Teste | Estratégia | Tamanho | Overlap | Nº Chunks | Média | Mín | Máx | Desvio Padrão |
|---|---|---|---|---|---|---|---|---|
| 1 | fixed | 200 | 0 | 499 | 197.24 | 95 | 200 | 8.3 |
| 2 | fixed | 500 | 0 | 200 | 495.91 | 228 | 500 | 21.93 |
| 3 | fixed | 1000 | 0 | 100 | 995.75 | 729 | 1000 | 27.24 |
| 4 | fixed | 2000 | 0 | 50 | 1993.22 | 1729 | 2000 | 38.36 |
| 5 | fixed_overlap | 500 | 50 | 222 | 496.79 | 279 | 500 | 15.8 |
| 6 | fixed_overlap | 500 | 200 | 332 | 497.08 | 383 | 500 | 9.77 |
| 7 | paragraph | None | 0 | 223 | 445.22 | 1 | 3529 | 643.58 |
| 8 | sentence_group | None | 0 | 271 | 366.43 | 14 | 4145 | 440.33 |
| 9 | recursive | 1000 | 100 | 142 | 708.6 | 69 | 998 | 254.37 |
| 10 | markdown_headers | None | 0 | 40 | 2495.85 | 37 | 13482 | 2698.1 |

- **Estratégia que gerou MAIS chunks**: Teste 1 (fixed, 499 chunks)
- **Estratégia que gerou MENOS chunks**: Teste 10 (markdown_headers, 40 chunks)
- **Maior tamanho médio de chunk**: Teste 10 (markdown_headers, 2495.85 caracteres)
- **Menor tamanho médio de chunk**: Teste 1 (fixed, 197.24 caracteres)

## Documento: retrieval_augmented_generation.pdf (`retrieval_augmented_generation`)

| Teste | Estratégia | Tamanho | Overlap | Nº Chunks | Média | Mín | Máx | Desvio Padrão |
|---|---|---|---|---|---|---|---|---|
| 1 | fixed | 200 | 0 | 360 | 198.7 | 15 | 200 | 10.27 |
| 2 | fixed | 500 | 0 | 144 | 497.65 | 315 | 500 | 16.09 |
| 3 | fixed | 1000 | 0 | 72 | 995.58 | 815 | 1000 | 22.66 |
| 4 | fixed | 2000 | 0 | 36 | 1998 | 1960 | 2000 | 6.87 |
| 5 | fixed_overlap | 500 | 50 | 160 | 498.04 | 410 | 500 | 10.55 |
| 6 | fixed_overlap | 500 | 200 | 240 | 497.58 | 260 | 500 | 18.48 |
| 7 | paragraph | None | 0 | 131 | 547.33 | 11 | 4047 | 799.21 |
| 8 | sentence_group | None | 0 | 233 | 307.04 | 19 | 1809 | 214.68 |
| 9 | recursive | 1000 | 100 | 103 | 702.13 | 17 | 998 | 258.54 |
| 10 | markdown_headers | None | 0 | 35 | 2056.8 | 12 | 23245 | 3883.19 |

- **Estratégia que gerou MAIS chunks**: Teste 1 (fixed, 360 chunks)
- **Estratégia que gerou MENOS chunks**: Teste 10 (markdown_headers, 35 chunks)
- **Maior tamanho médio de chunk**: Teste 10 (markdown_headers, 2056.8 caracteres)
- **Menor tamanho médio de chunk**: Teste 1 (fixed, 198.7 caracteres)

## Documento: scaling_laws_llm.pdf (`scaling_laws_llm`)

| Teste | Estratégia | Tamanho | Overlap | Nº Chunks | Média | Mín | Máx | Desvio Padrão |
|---|---|---|---|---|---|---|---|---|
| 1 | fixed | 200 | 0 | 492 | 187.25 | 1 | 200 | 38.93 |
| 2 | fixed | 500 | 0 | 200 | 477.21 | 3 | 500 | 75.95 |
| 3 | fixed | 1000 | 0 | 100 | 968.57 | 674 | 1000 | 77.52 |
| 4 | fixed | 2000 | 0 | 50 | 1971.34 | 1739 | 2000 | 70.58 |
| 5 | fixed_overlap | 500 | 50 | 222 | 476.36 | 3 | 500 | 79.46 |
| 6 | fixed_overlap | 500 | 200 | 332 | 478.33 | 3 | 500 | 73.22 |
| 7 | paragraph | None | 0 | 358 | 276.61 | 3 | 16079 | 920.32 |
| 8 | sentence_group | None | 0 | 440 | 221.82 | 5 | 1669 | 237.68 |
| 9 | recursive | 1000 | 100 | 137 | 740.26 | 17 | 998 | 193.62 |
| 10 | markdown_headers | None | 0 | 52 | 1922.02 | 13 | 23406 | 3259.34 |

- **Estratégia que gerou MAIS chunks**: Teste 1 (fixed, 492 chunks)
- **Estratégia que gerou MENOS chunks**: Teste 4 (fixed, 50 chunks)
- **Maior tamanho médio de chunk**: Teste 4 (fixed, 1971.34 caracteres)
- **Menor tamanho médio de chunk**: Teste 1 (fixed, 187.25 caracteres)
