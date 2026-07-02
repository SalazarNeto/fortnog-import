import pdfplumber


class TableReader:

    def __init__(self, arquivo):

        self.arquivo = arquivo

    def ler(self):

        paginas = []

        with pdfplumber.open(self.arquivo) as pdf:

            for numero, pagina in enumerate(pdf.pages, start=1):

                tabelas = pagina.extract_tables()

                paginas.append(
                    {
                        "pagina": numero,
                        "tabelas": tabelas
                    }
                )

        return paginas
