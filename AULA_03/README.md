# Introdução à IA - Aula 03: Distâncias entre Embeddings e Busca Semântica

## 📂 Arquivos

- `embeddings_utils.py` — gera embeddings (padrão: modelo local e gratuito do
  Hugging Face, `sentence-transformers/all-MiniLM-L6-v2`) e implementa:
  - `distancia_euclidiana()`
  - `similaridade_cosseno()`
  - `distancia_cosseno()`
- `teste_distancias_termos.py` — testa as funções com (A) o exemplo numérico
  do enunciado (`[1,0,0]`, `[0,1,0]`, `[1,0,0]`) e (B) embeddings reais de
  termos (gato, felino, cachorro, carro, caminhão, moto, banana, maçã, goiaba).
- `teste_distancias_frases.py` — compara uma frase âncora com 4 frases de
  categorias diferentes (similar, relacionada, domínio diferente,
  oposto/negação), mostrando como as distâncias variam com o significado.
- `busca_semantica.py` — lê os `.md` da pasta `aula_2/` (gerados na Aula 02
  com o Docling), divide por linha/parágrafo/capítulo, e retorna o TOP 3
  trechos mais similares a uma pergunta.
- `aula_2/` — cópia dos markdowns gerados na Aula 02, usados como base para
  a busca semântica.

## 🚀 Como rodar

```bash
pip install -r requirements.txt
python teste_distancias_termos.py
python teste_distancias_frases.py
python busca_semantica.py
```

Não precisa de nenhuma chave de API por padrão (usa Hugging Face local). Se
quiser usar a OpenAI em vez disso, copie `.env.example` para `.env`, preencha
`OPENAI_API_KEY` e mude `EMBEDDING_PROVIDER=openai`.

## 📖 Conceitos

- **Distância Euclidiana**: distância "em linha reta" entre dois vetores.
  Quanto **menor**, mais parecidos.
- **Similaridade de Cosseno**: mede o ângulo entre dois vetores (ignora
  magnitude). Vai de -1 a 1. Quanto **maior**, mais parecidos.
- **Distância de Cosseno**: `1 - similaridade de cosseno`. Quanto **menor**,
  mais parecidos.
- **Busca Semântica**: compara o significado (embedding) da pergunta com o
  significado de cada trecho do texto, em vez de buscar por palavra-chave
  exata.
