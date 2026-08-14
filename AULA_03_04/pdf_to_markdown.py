"""
Converte todos os PDFs de uma pasta para Markdown usando o Docling.

Uso:
    python pdf_to_markdown.py --pdfs pasta_com_pdfs --saida results
"""

import os
import glob
import argparse
from utils import slugify
# Import do docling fica dentro da função converter_pdfs() de propósito, para
# que outros módulos (como pipeline.py) possam reaproveitar slugify() sem
# precisar ter o docling instalado quando só trabalham com markdowns prontos.


def converter_pdfs(pasta_pdfs: str, pasta_resultados: str = "results") -> dict:
    """
    Converte todos os PDFs de `pasta_pdfs` para markdown, salvando cada um em
    results/<document_id>/markdown/<document_id>.md

    Retorna um dict {document_id: {"pdf": caminho_pdf, "markdown": caminho_md}}
    """
    from docling.document_converter import DocumentConverter

    pdfs = sorted(glob.glob(os.path.join(pasta_pdfs, "*.pdf")))
    if not pdfs:
        print(f"Nenhum PDF encontrado em '{pasta_pdfs}/'.")
        return {}

    converter = DocumentConverter()
    documentos = {}

    for caminho_pdf in pdfs:
        nome_arquivo = os.path.basename(caminho_pdf)
        document_id = slugify(nome_arquivo)
        print(f"Convertendo {nome_arquivo} -> {document_id}...")

        pasta_md = os.path.join(pasta_resultados, document_id, "markdown")
        os.makedirs(pasta_md, exist_ok=True)
        caminho_md = os.path.join(pasta_md, f"{document_id}.md")

        doc = converter.convert(caminho_pdf).document
        markdown = doc.export_to_markdown()

        with open(caminho_md, "w", encoding="utf-8") as f:
            f.write(markdown)

        documentos[document_id] = {"pdf": caminho_pdf, "pdf_name": nome_arquivo, "markdown": caminho_md}
        print(f"  -> salvo em {caminho_md}")

    print(f"\n{len(documentos)} documento(s) convertido(s).")
    return documentos


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdfs", default="pdfs", help="Pasta com os PDFs de entrada")
    parser.add_argument("--saida", default="results", help="Pasta raiz de resultados")
    args = parser.parse_args()

    converter_pdfs(args.pdfs, args.saida)
