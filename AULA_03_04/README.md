# Avaliação de Estratégias de Chunking com LangChain

Pipeline completo: **PDF → Markdown → 10 estratégias de chunking → Embeddings → JSON**,
usado para comparar como diferentes formas de dividir um documento afetam a
qualidade da representação para um sistema de RAG.

## 📂 Arquivos

- `utils.py` — funções pequenas e compartilhadas (ex: `slugify`).
- `pdf_to_markdown.py` — converte PDFs em Markdown usando o **Docling**.
- `chunking_strategies.py` — implementa os 10 testes de chunking usando os
  splitters do **LangChain** (`CharacterTextSplitter`,
  `RecursiveCharacterTextSplitter`, `MarkdownHeaderTextSplitter`) e uma
  implementação manual para o agrupamento por sentenças (não existe splitter
  pronto no LangChain para isso).
- `embeddings_utils.py` — gera embeddings. Por padrão usa um modelo **local e
  gratuito** do Hugging Face (`sentence-transformers/all-MiniLM-L6-v2`), para
  evitar os problemas de créditos esgotados da API paga da OpenAI. Pode ser
  trocado via `.env`.
- `pipeline.py` — orquestra tudo: lê os markdowns, roda os 10 testes, gera
  embeddings, salva os JSONs por teste e o `summary.json` comparativo.
- `analise_comparativa.py` — lê o `summary.json` e gera uma tabela markdown
  comparando as 10 estratégias (`results/analise_comparativa.md`).
- `relatorio_template.md` — modelo do relatório final com as perguntas de
  análise obrigatórias da atividade.

## 🚀 Como rodar

### 1. Instalar dependências

```bash
pip install -r requirements.txt
```

### 2. Configurar o modelo de embeddings (opcional)

Copie `.env.example` para `.env`. Por padrão já funciona sem chave de API
nenhuma (usa Hugging Face local).

### Fase 1 — Experimentar as 10 estratégias nos 3 `.md` das aulas anteriores

```bash
python pipeline.py --markdowns caminho/para/pasta/com/os/3_md --saida results
python analise_comparativa.py --saida results
```

### Fase 2 — Depois de escolher as melhores estratégias, aplicar em todos os PDFs

```bash
python pdf_to_markdown.py --pdfs pdfs --saida results
python pipeline.py --usar-markdown-de-results --saida results
python analise_comparativa.py --saida results
```

## 📁 Estrutura de saída

```
results/
├── documento_01/
│   ├── markdown/documento_01.md
│   ├── test_01/chunks_embeddings.json
│   ├── test_02/chunks_embeddings.json
│   ├── ...
│   └── test_10/chunks_embeddings.json
├── documento_02/
│   └── ...
├── summary.json
└── analise_comparativa.md
```

## 📖 As 10 estratégias

| Teste | Estratégia | Configuração |
|---|---|---|
| 1 | Fixo | 200 caracteres, sem overlap |
| 2 | Fixo | 500 caracteres, sem overlap |
| 3 | Fixo | 1000 caracteres, sem overlap |
| 4 | Fixo | 2000 caracteres, sem overlap |
| 5 | Fixo + overlap | 500 caracteres, overlap 50 |
| 6 | Fixo + overlap | 500 caracteres, overlap 200 |
| 7 | Por parágrafo | Separação por `\n\n` |
| 8 | Por sentença | Sentenças agrupadas de 3 em 3 |
| 9 | Recursivo | Separadores hierárquicos |
| 10 | Markdown | Separação por headings |
