import logging
from pathlib import Path

Path("logs").mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[
        logging.FileHandler("logs/importador.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("fortnog")
