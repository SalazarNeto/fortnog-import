from pathlib import Path

from src.logger import logger
from src.pdf_reader import PDFReader
from src.ocr import OCR
from src.parser import Parser
from src.table_reader import TableReader

PDF = Path("catalogos/ALTRI.pdf")


def testar_tabelas():

    logger.info("Verificando tabelas do PDF...")

    reader = TableReader(PDF)

    tabelas = reader.ler()

    encontrou = False

    for pagina in tabelas:

        if pagina["tabelas"]:

            encontrou = True

            logger.info(
                f"Página {pagina['pagina']} -> {len(pagina['tabelas'])} tabela(s)"
            )

    return encontrou


def processar_ocr():

    logger.info("Nenhuma tabela encontrada.")
    logger.info("Iniciando OCR...")

    reader = PDFReader(PDF)

    ocr = OCR(PDF)

    parser = Parser()

    total = reader.paginas()

    logger.info(f"{total} páginas")

    for pagina in range(total):

        texto = reader.texto(pagina)

        if len(texto.strip()) < 80:

            texto = ocr.texto(pagina)

        parser.extrair(
            pagina + 1,
            texto
        )

    parser.salvar()


def main():

    logger.info("=====================================")
    logger.info("FORTNOG IMPORTADOR")
    logger.info("=====================================")

    if testar_tabelas():

        logger.info("PDF possui tabelas estruturadas.")
        logger.info("OCR cancelado.")

        return

    processar_ocr()


if __name__ == "__main__":

    main()
