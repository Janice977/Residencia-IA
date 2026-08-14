"""Funções utilitárias pequenas, compartilhadas entre os módulos do pipeline."""

import os
import re


def slugify(nome: str) -> str:
    """Transforma o nome de um arquivo em um id de documento seguro (ex: documento_01)."""
    nome = os.path.splitext(nome)[0]
    nome = re.sub(r"[^a-zA-Z0-9_-]+", "_", nome).strip("_").lower()
    return nome
