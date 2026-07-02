import sqlite3
from pathlib import Path

DB = Path("output/fortnog.db")


class Database:

    def __init__(self):

        DB.parent.mkdir(exist_ok=True)

        self.conn = sqlite3.connect(DB)

        self.cursor = self.conn.cursor()

    def criar(self):

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS fornecedores(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            nome TEXT,

            cnpj TEXT,

            cidade TEXT,

            estado TEXT

        )

        """)

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS produtos(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            codigo TEXT UNIQUE,

            descricao TEXT,

            categoria TEXT,

            potencia_cv REAL,

            potencia_kw REAL,

            tensao TEXT,

            pagina INTEGER,

            fornecedor TEXT,

            preco REAL,

            custo REAL,

            imagem TEXT

        )

        """)

        self.conn.commit()

    def inserir(self, produto):

        self.cursor.execute("""

        INSERT OR IGNORE INTO produtos(

            codigo,

            descricao,

            categoria,

            potencia_cv,

            potencia_kw,

            tensao,

            pagina,

            fornecedor,

            preco,

            custo,

            imagem

        )

        VALUES(?,?,?,?,?,?,?,?,?,?,?)

        """, (

            produto.codigo,

            produto.nome,

            produto.categoria,

            produto.potencia_cv,

            produto.potencia_kw,

            produto.tensao,

            produto.pagina,

            produto.fornecedor,

            produto.preco,

            produto.custo,

            produto.imagem

        ))

        self.conn.commit()
