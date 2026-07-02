from pathlib import Path

def criar_pastas():

    pastas = [
        "catalogos",
        "images",
        "output",
        "logs",
        "modelos"
    ]

    for pasta in pastas:
        Path(pasta).mkdir(exist_ok=True)
