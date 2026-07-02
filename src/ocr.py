import fitz
import pytesseract

from PIL import Image
from pathlib import Path


class OCR:

    def __init__(self, pdf):

        self.pdf = fitz.open(pdf)

    def extrair_pagina(self, numero):

        pagina = self.pdf.load_page(numero)

        pix = pagina.get_pixmap(dpi=300)

        imagem = Image.frombytes(
            "RGB",
            [pix.width, pix.height],
            pix.samples
        )

        return imagem

    def texto(self, numero):

        imagem = self.extrair_pagina(numero)

        texto = pytesseract.image_to_string(
            imagem,
            lang="por"
        )

        return texto
