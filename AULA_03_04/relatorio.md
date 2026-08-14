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
| 9 | Recursivo | Separadores hierárquicos (parágrafo → linha → frase → espaço → caractere), chunk_size=1000, overlap=100 |
| 10 | Markdown | Separação por headings (`#`, `##`, `###`) |

**Modelo de embedding utilizado**: `sentence-transformers/all-MiniLM-L6-v2` (Hugging Face, local, 384 dimensões).

**Documentos processados na Fase 1** (experimentação inicial, conforme pedido no
enunciado — usar apenas os 3 `.md` das aulas anteriores):
- `bioetica_e_ia.pdf` (12 páginas)
- `escrita_academica_ia.pdf` (14 páginas)
- `twitter_algoritmo.pdf` (18 páginas)

## 2. Estatísticas

### bioetica_e_ia.pdf

| Teste | Estratégia | Tamanho | Overlap | Nº Chunks | Média | Mín | Máx | Desvio Padrão |
|---|---|---|---|---|---|---|---|---|
| 1 | fixed | 200 | 0 | 257 | 198.93 | 13 | 200 | 11.66 |
| 2 | fixed | 500 | 0 | 103 | 496.83 | 213 | 500 | 28.25 |
| 3 | fixed | 1000 | 0 | 52 | 984.5 | 213 | 1000 | 109.09 |
| 4 | fixed | 2000 | 0 | 26 | 1969.42 | 1211 | 2000 | 154.69 |
| 5 | fixed_overlap | 500 | 50 | 114 | 498.49 | 363 | 500 | 12.81 |
| 6 | fixed_overlap | 500 | 200 | 171 | 497.95 | 213 | 500 | 21.93 |
| 7 | paragraph | - | 0 | 135 | 377.37 | 3 | 4291 | 473.02 |
| 8 | sentence_group | - | 0 | 139 | 366.58 | 38 | 1088 | 264.57 |
| 9 | recursive | 1000 | 100 | 73 | 704.84 | 192 | 995 | 225.87 |
| 10 | markdown_headers | - | 0 | 25 | 2049.76 | 10 | 8596 | 2079.16 |

### escrita_academica_ia.pdf

| Teste | Estratégia | Tamanho | Overlap | Nº Chunks | Média | Mín | Máx | Desvio Padrão |
|---|---|---|---|---|---|---|---|---|
| 1 | fixed | 200 | 0 | 212 | 196.92 | 23 | 200 | 16.65 |
| 2 | fixed | 500 | 0 | 86 | 486.37 | 63 | 500 | 60.85 |
| 3 | fixed | 1000 | 0 | 43 | 978.86 | 563 | 1000 | 81.87 |
| 4 | fixed | 2000 | 0 | 22 | 1939.55 | 678 | 2000 | 281.77 |
| 5 | fixed_overlap | 500 | 50 | 95 | 490.05 | 156 | 500 | 45.25 |
| 6 | fixed_overlap | 500 | 200 | 142 | 492.89 | 156 | 500 | 42.06 |
| 7 | paragraph | - | 0 | 116 | 365.93 | 2 | 2674 | 485.23 |
| 8 | sentence_group | - | 0 | 99 | 425.97 | 5 | 1668 | 259.65 |
| 9 | recursive | 1000 | 100 | 60 | 714.9 | 141 | 993 | 219.32 |
| 10 | markdown_headers | - | 0 | 20 | 2136.8 | 16 | 6175 | 1924.15 |

### twitter_algoritmo.pdf

| Teste | Estratégia | Tamanho | Overlap | Nº Chunks | Média | Mín | Máx | Desvio Padrão |
|---|---|---|---|---|---|---|---|---|
| 1 | fixed | 200 | 0 | 273 | 198.93 | 40 | 200 | 9.68 |
| 2 | fixed | 500 | 0 | 109 | 498.92 | 440 | 500 | 5.73 |
| 3 | fixed | 1000 | 0 | 55 | 989.31 | 440 | 1000 | 75.44 |
| 4 | fixed | 2000 | 0 | 28 | 1943.68 | 440 | 2000 | 294.69 |
| 5 | fixed_overlap | 500 | 50 | 121 | 499.13 | 440 | 500 | 5.46 |
| 6 | fixed_overlap | 500 | 200 | 181 | 499.25 | 440 | 500 | 4.48 |
| 7 | paragraph | - | 0 | 196 | 275.77 | 1 | 1386 | 317.9 |
| 8 | sentence_group | - | 0 | 140 | 386.76 | 15 | 1049 | 274.83 |
| 9 | recursive | 1000 | 100 | 78 | 707.94 | 65 | 996 | 250.86 |
| 10 | markdown_headers | - | 0 | 22 | 2480.55 | 73 | 9877 | 3176.8 |

## 3. Exemplos de chunks

**Teste 1 (fixed, 200 chars)** — corte cego, sem respeitar nenhuma estrutura:
> "273\n\n<!-- image -->\n\n## Entre o algoritmo e o Juramento de Hipócrates: bioética na era da inteligência artificial\n\nJuracy Barbosa dos Santos 1 , Guilhermina Rego 1 , Rui Nunes 1\n\n1. Faculdade de M"

(o chunk termina no meio da palavra "Medicina" — corte arbitrário típico do chunking fixo)

**Teste 7 (paragraph)** — cada parágrafo original vira um chunk:
> "1. Faculdade de Medicina da Universidade do Porto, Porto, Portugal."

(um parágrafo curto vira um chunk minúsculo — mostra a alta variância dessa estratégia)

**Teste 9 (recursive)** — tenta cortar em fronteiras naturais (parágrafo → linha → frase):
> chunks entre 65 e 996 caracteres, quase sempre terminando em frase completa, sem cortar palavras no meio.

**Teste 10 (markdown_headers)** — cada seção (`##`) vira um chunk, mesmo que gigante:
> a seção "Resumo" (com resumo em português, inglês e espanhol) virou um único chunk de mais de 8000 caracteres no documento de bioética.

## 4. Análise da conversão PDF → Markdown (Docling)

- **Imagens**: são **descartadas** (o conteúdo visual não é extraído nem descrito), mas o Docling insere um marcador `<!-- image -->` no lugar exato onde a imagem aparecia, preservando a **posição** dela no fluxo do documento. Não há descrição textual (nenhum "alt text") nem link para a imagem original.
- **Tabelas**: são convertidas em **tabelas markdown reais** (`| coluna | coluna |` com linha separadora `|---|---|`), preservando cabeçalhos, número de colunas e o conteúdo célula a célula. No documento `escrita_academica_ia.pdf`, por exemplo, uma tabela com 3 colunas e 5 linhas (fases do processo de escrita assistida por IA) foi reconstruída corretamente em markdown.
- **Headings**: preservados fielmente como `#`, `##` no markdown, o que permite o Teste 10 funcionar bem.
- **Ordem dos elementos**: mantida — o texto segue a mesma sequência do PDF original.
- **Informação perdida**: o conteúdo semântico das imagens (gráficos, diagramas, fotos) é totalmente perdido — só resta o marcador de posição. Números de página não ficam marcados explicitamente no corpo do markdown (não há um metadado `page: N` por padrão na exportação simples usada aqui).

## 5. Análise das estratégias de chunking

**1. Qual estratégia gerou mais chunks?**
O Teste 1 (fixed, 200 caracteres) — consistentemente, nos 3 documentos (257, 212 e 273 chunks). Faz sentido: quanto menor o chunk, mais pedaços são necessários para cobrir o documento inteiro.

**2. Qual gerou menos chunks?**
O Teste 10 (markdown_headers) — 25, 20 e 22 chunks nos 3 documentos. Como cada chunk corresponde a uma seção inteira do documento, o número de chunks é limitado à quantidade de headings.

**3. Como o tamanho dos chunks variou?**
Os testes de tamanho fixo (1 a 6) têm baixíssima variância (desvio padrão pequeno, chunks quase sempre no tamanho máximo configurado). Já as estratégias estruturais (7, 8, 10) têm desvio padrão muito alto — no Teste 10, por exemplo, o desvio chegou a 3176 no documento sobre Twitter, porque seções podem ter de 73 a quase 10.000 caracteres.

**4. Qual estratégia preservou melhor a estrutura dos documentos?**
O Teste 10 (markdown_headers), seguido do Teste 7 (paragraph) e do Teste 9 (recursive). O Teste 10 respeita literalmente a hierarquia de seções do autor; o Teste 9 tenta preservar frases e parágrafos inteiros sempre que possível dentro do limite de tamanho.

**5. Como tabelas foram tratadas?**
As tabelas já chegam como markdown estruturado na etapa de conversão (Docling). No chunking, porém, as estratégias de tamanho fixo (Testes 1–6) podem **cortar uma tabela no meio de uma linha**, quebrando a estrutura `|---|---|`. Já os Testes 7, 9 e 10 tendem a manter a tabela mais intacta, pois respeitam quebras de parágrafo/seção — mas isso não é garantido se a tabela for maior que o `chunk_size`.

**6. Como imagens foram tratadas?**
Como o marcador `<!-- image -->` é só uma linha curta, ele normalmente fica "grudado" no início ou fim de algum chunk vizinho, sem causar problema estrutural grave — mas também sem agregar nenhuma informação útil para a busca semântica (o embedding desse chunk não "sabe" o que a imagem mostrava).

**7. Quais informações foram perdidas durante a conversão PDF → Markdown?**
O conteúdo visual das imagens/gráficos (nenhuma descrição gerada) e, em alguns casos, a formatação visual original (ex: itálico, negrito específico, layout em colunas) — o Docling extrai o texto e a estrutura lógica, não o layout visual exato.

**8. O chunking por caracteres fragmentou conceitos ou estruturas importantes?**
Sim, claramente. Os Testes 1–4 (sem overlap) frequentemente cortam frases e até palavras no meio (ex.: "Faculdade de M" no exemplo da seção 3), o que pode prejudicar a qualidade do embedding gerado para aquele chunk.

**9. O chunking por parágrafo produziu chunks muito grandes?**
Depende do documento — a maioria dos parágrafos ficou pequena/média, mas alguns picos grandes apareceram (até 4291 caracteres em `bioetica_e_ia.pdf`), geralmente quando o Docling não inseriu uma quebra dupla de linha onde seria esperado (parágrafos "grudados").

**10. O chunking por sentença conseguiu preservar melhor o contexto?**
Parcialmente. Agrupar 3 sentenças cria unidades de tamanho mais previsível que o chunking por caractere puro, mas ainda pode misturar sentenças de tópicos diferentes se elas estiverem seguidas no texto sem relação direta.

**11. O Recursive Splitter apresentou vantagens?**
Sim — foi a estratégia com o melhor equilíbrio entre respeitar limites de tamanho (bom para custo/desempenho de embeddings) e evitar cortes no meio de frases, por tentar múltiplos separadores em ordem de prioridade antes de recorrer ao corte bruto por caractere.

**12. O Markdown Splitter conseguiu preservar a estrutura semântica?**
Sim, foi o mais fiel à intenção do autor do documento — cada chunk corresponde a uma unidade de sentido real (uma seção). A desvantagem é a alta variabilidade de tamanho, que pode ser um problema para modelos de embedding com limite de tokens.

**13. Qual estratégia parece mais adequada para um sistema de RAG?**
O **Recursive Splitter (Teste 9)** parece o melhor ponto de partida geral: mantém tamanho controlado (bom para custo e para o limite de contexto do modelo de embedding) e prioriza cortes em fronteiras naturais. Para documentos bem estruturados com headings claros, o **Markdown Splitter (Teste 10)** combinado com um limite máximo de tamanho (ex: dividir seções grandes recursivamente) seria o ideal — uma combinação de estratégias.

**14. Quais estratégias devem ser descartadas?**
O Teste 1 (200 caracteres, sem overlap) — chunks pequenos demais, com muito corte de palavras/frases, gerando ruído sem contexto suficiente para busca semântica útil.

**15. Quais estratégias devem ser utilizadas nos próximos experimentos?**
Recomenda-se aprofundar os Testes 9 (recursive) e 10 (markdown_headers) — inclusive testando uma variação híbrida: usar o Markdown Splitter primeiro (para respeitar seções) e, para seções muito grandes, aplicar o Recursive Splitter como segunda passada.

## 7. Fase 2 — Aplicação em todos os documentos (12 PDFs)

Após a experimentação inicial (Fase 1, 3 documentos), as 10 estratégias foram
aplicadas em **todos os 12 PDFs** da pasta do Google Drive, incluindo papers
técnicos em inglês bem mais longos e ricos em tabelas/fórmulas
(`attention_is_all_you_need.pdf`, `bert_pretraining.pdf`,
`gpt3_language_models.pdf`, `gpt4_technical_report.pdf`, `instruct_gpt.pdf`,
`llama_foundation_models.pdf`, `lora_low_rank_adaptation.pdf`,
`retrieval_augmented_generation.pdf`, `scaling_laws_llm.pdf`), além dos 3
documentos da Fase 1.

**Total**: 12 documentos × 10 testes = **120 experimentos**, com o `summary.json`
e os JSONs individuais de cada teste disponíveis em `results/`.

### Médias agregadas entre os 12 documentos

| Teste | Estratégia | Média de chunks/doc | Média do tamanho de chunk |
|---|---|---|---|
| 1 | fixed (200) | 606.6 | 194.1 |
| 2 | fixed (500) | 247.4 | 487.2 |
| 3 | fixed (1000) | 124.4 | 979.9 |
| 4 | fixed (2000) | 62.4 | 1962.8 |
| 5 | fixed_overlap (500/50) | 274.9 | 488.0 |
| 6 | fixed_overlap (500/200) | 411.8 | 488.4 |
| 7 | paragraph | 334.8 | 382.3 |
| 8 | sentence_group | 342.9 | 360.4 |
| 9 | recursive | 170.4 | 729.6 |
| 10 | markdown_headers | 58.9 | 2326.2 |

A tendência observada na Fase 1 **se confirmou** numa base 4x maior e mais
diversa: o Teste 1 (fixed 200) continua gerando o maior número de chunks, e o
Teste 10 (markdown_headers) continua gerando os chunks maiores e em menor
quantidade.

### Achado novo sobre tabelas (papers técnicos)

Os papers técnicos em inglês contêm muito mais tabelas que os documentos da
Fase 1 — por exemplo, `gpt4_technical_report.pdf` tem 197 linhas de tabela
markdown (contra praticamente zero nos 3 documentos originais). Isso reforça
o risco identificado na Fase 1: as estratégias de tamanho fixo (Testes 1–6)
têm chance bem maior de **cortar uma tabela no meio** nesses documentos,
enquanto o Recursive Splitter (Teste 9) e o Markdown Splitter (Teste 10)
preservam melhor esse tipo de conteúdo.

## 8. Conclusão final

Com os dados da Fase 1 (3 documentos) e da Fase 2 (12 documentos, incluindo
papers técnicos densos em tabelas e fórmulas), a recomendação se mantém e fica
mais robusta:

- **Estratégia principal recomendada para o pipeline de RAG**: **Recursive
  Character Text Splitter (Teste 9)**, `chunk_size=1000`, `chunk_overlap=100`.
  Motivo: mantém tamanho controlado e previsível (bom para custo e limite de
  contexto do modelo de embedding), evita cortar frases/tabelas no meio na
  maioria dos casos, e seu comportamento foi consistente tanto nos documentos
  curtos (artigos em português) quanto nos longos (papers técnicos em inglês).
- **Estratégia complementar**: **Markdown Header Splitter (Teste 10)**, útil
  quando o sistema de RAG precisa recuperar **seções inteiras** (ex.: "me
  mostre a seção de resultados experimentais"), mas exige cuidado adicional
  porque algumas seções ultrapassam 8000–9000 caracteres — nesses casos, uma
  segunda passada com o Recursive Splitter dentro de cada seção grande seria
  o ideal (estratégia híbrida).
- **Estratégias descartadas**: Teste 1 (fixed 200) — gera chunks pequenos
  demais e corta palavras/frases com frequência, prejudicando a qualidade da
  representação semântica sem ganho real de precisão na recuperação.
