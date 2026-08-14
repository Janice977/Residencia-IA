# Relatório — Avaliação de Estratégias de Chunking com LangChain

## 1. Configuração dos 10 testes

| Teste | Estratégia | Configuração |
|---|---|---|
| 1 | Fixo | 200 caracteres, sem overlap |
| 2 | Fixo | 500 caracteres, sem overlap |
| 3 | Fixo | 1000 caracteres, sem overlap |
| 4 | Fixo | 2000 caracteres, sem overlap |
| 5 | Fixo + overlap | 500 caracteres, overlap 50 |
| 6 | Fixo + overlap | 500 caracteres, overlap 200 |
| 7 | Por parágrafo | Separação por parágrafos (`\n\n`) |
| 8 | Por sentença | Sentenças agrupadas em 3 |
| 9 | Recursivo | Separadores hierárquicos (parágrafo → linha → frase → espaço → caractere) |
| 10 | Markdown | Separação por headings (`#`, `##`, `###`) |

Modelo de embedding utilizado: `<preencher com o valor de EMBEDDING_MODEL usado>`

## 2. Estatísticas

*(Cole aqui a tabela gerada em `results/analise_comparativa.md`, ou rode
`python analise_comparativa.py` e cole a saída)*

## 3. Exemplos de chunks

*(Cole 1–2 exemplos de chunk de cada estratégia, extraídos dos arquivos
`chunks_embeddings.json`)*

## 4. Análise da conversão PDF → Markdown

- Como o Docling representou **imagens**? (descartadas / referência / descrição textual / posição preservada?)
- Como o Docling representou **tabelas**? (Markdown `| coluna |` preservando estrutura, ou outro formato?)
- Que informações foram **perdidas** na conversão?

## 5. Análise das estratégias de chunking

Responda com base nos dados gerados:

1. Qual estratégia gerou mais chunks?
2. Qual gerou menos chunks?
3. Como o tamanho dos chunks variou entre as estratégias?
4. Qual estratégia preservou melhor a estrutura dos documentos?
5. Como tabelas foram tratadas pelo chunking?
6. Como imagens foram tratadas pelo chunking?
7. Quais informações foram perdidas durante a conversão PDF → Markdown?
8. O chunking por caracteres fragmentou conceitos ou estruturas importantes?
9. O chunking por parágrafo produziu chunks muito grandes?
10. O chunking por sentença conseguiu preservar melhor o contexto?
11. O Recursive Splitter apresentou vantagens?
12. O Markdown Splitter conseguiu preservar a estrutura semântica?
13. Qual estratégia parece mais adequada para um sistema de RAG?
14. Quais estratégias devem ser descartadas?
15. Quais estratégias você acha que devem ser utilizadas nos próximos experimentos?

## 6. Conclusão

*(Resuma qual(is) estratégia(s) foram escolhidas para aplicar em todos os
documentos, e por quê.)*
