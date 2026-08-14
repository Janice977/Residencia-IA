# AULA 05: Documents, Metadados e Busca Vetorial com LangChain

## 🎯 Exercício 1 - Criando Documents na Mão

### Respostas Teóricas:
1. **Que tipos de dados são aceitos dentro de `metadata`?**
   - Aceita um dicionário Python (`dict`) com tipos primitivos (`str`, `int`, `float`, `bool`), listas e dicionários aninhados.
   - *Ressalva:* Dicionários aninhados funcionam no LangChain, mas costumam falhar em Vector Stores reais (ChromaDB/Pinecone), que exigem valores primitivos para filtragem.

2. **O que acontece se você criar um `Document` sem passar `metadata`?**
   - O LangChain cria automaticamente o atributo `metadata` como um dicionário vazio (`{}`).

---

## 📐 Exercício 2 - Schema de Metadados

### Tabela do Schema Final

| Campo | Tipo | Origem | Descrição |
| :--- | :--- | :--- | :--- |
| `fonte` | `str` | Obrigatório | Nome do arquivo `.md` de origem |
| `documento_id` | `str` | Obrigatório | Identificador único do documento |
| `chunk_index` | `int` | Obrigatório | Posição sequencial do chunk no documento original |
| `estrategia` | `str` | Obrigatório | Estratégia de chunking utilizada na Aula 04 |
| `chunk_size` | `int` | Obrigatório | Tamanho máximo de janela do splitter |
| `chunk_overlap` | `int` | Obrigatório | Sobreposição entre chunks consecutivos |
| `n_caracteres` | `int` | Obrigatório | Quantidade exata de caracteres do chunk |
| `secao_titulo` | `str` | **Próprio 1** | Capítulo ou seção do documento original |
| `idioma` | `str` | **Próprio 2** | Código ISO do idioma (`pt-BR`, `en-US`) |
| `data_processamento` | `str` | **Próprio 3** | Data ISO (YYYY-MM-DD) do processamento |

### Justificativa dos Campos Próprios
- **`secao_titulo`**: Permite citar em qual seção/capítulo o trecho foi encontrado.
- **`idioma`**: Permite aplicar filtros multilíngues no pipeline RAG.
- **`data_processamento`**: Garante governança e auditoria do versionamento dos chunks.

### Respostas Finais:
1. **Campo para Citar Fonte no RAG:** A combinação de **`fonte`** e **`secao_titulo`**.
2. **Utilidade do `chunk_index`:** Permite a **reconstrução de contexto (Neighbor Window Retrieval)** para recuperar os chunks vizinhos (`chunk_index - 1` e `+ 1`) se o texto retornado estiver cortado no meio da explicação.
