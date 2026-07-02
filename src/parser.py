import re
import json
from pathlib import Path

from src.models import Produto
from src.database.database import Database


class Parser:

    def __init__(self):

        self.produtos = []

        self.db = Database()
        self.db.criar()

    def categoria(self, texto):

        texto = texto.upper()

        if "BOMBA SUBMERSA" in texto:
            return "Bomba Submersa"

        if "MOTOBOMBA" in texto:
            return "Motobomba"

        return "Não Classificado"

    def extrair(self, pagina, texto):

        categoria = self.categoria(texto)

        regex = r"\b[0-9]+(?:\.[0-9]+)?[A-Z]+[A-Z0-9\-]+\b"

        encontrados = re.findall(regex, texto)

        ignorar = {
            "220V",
            "127V",
            "380V",
            "415V",
            "60HZ",
            "NSK",
            "NEMA",
            "ISO",
            "AISI201",
            "AISI304",
            "AISI316"
        }

        vistos = set()

        for codigo in encontrados:

            codigo = codigo.strip()

            if codigo in ignorar:
                continue

            if len(codigo) < 5:
                continue

            if codigo in vistos:
                continue

            vistos.add(codigo)

            produto = Produto(
                codigo=codigo,
                categoria=categoria,
                pagina=pagina
            )

            self.produtos.append(produto)

            self.db.inserir(produto)

    def salvar(self):

        Path("output").mkdir(exist_ok=True)

        with open(
            "output/produtos.json",
            "w",
            encoding="utf8"
        ) as arq:

            json.dump(
                [p.dict() for p in self.produtos],
                arq,
                indent=4,
                ensure_ascii=False
            )

        print(f"{len(self.produtos)} produtos encontrados.")
