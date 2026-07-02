from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

DATABASE = BASE_DIR / "output" / "fortnog.db"

CATALOGOS = BASE_DIR / "catalogos"

OUTPUT = BASE_DIR / "output"

IMAGES = BASE_DIR / "images"
