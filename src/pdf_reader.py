import fitz


class PDFReader:

    def __init__(self, arquivo):

        self.pdf = fitz.open(arquivo)

    def paginas(self):

        return len(self.pdf)

    def texto(self, pagina):

        return self.pdf.load_page(pagina).get_text()
