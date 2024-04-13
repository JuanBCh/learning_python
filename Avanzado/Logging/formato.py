import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s", # La s indica que es string
    datefmt="%H:%M:%S"
)

nombre = "Paco"
logging.error(f"{nombre} metio la pata")

logging.warning("Log de advertencia")
logging.error("Log de error")
logging.critical("Log critico")

try:
    division = 2 / 0
except:
    logging.exception("Division por cero")
