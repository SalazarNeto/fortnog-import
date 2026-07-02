from dataclasses import dataclass, asdict


@dataclass
class Produto:

    codigo: str
    categoria: str
    pagina: int

    nome: str = ""
    descricao: str = ""
    tensao: str = ""
    potencia_kw: float | None = None
    potencia_cv: float | None = None

    fornecedor: str = "ALTRI BRASIL LTDA"

    preco: float = 10.0

    custo: float = 10.0

    imagem: str = ""

    def dict(self):
        return asdict(self)
