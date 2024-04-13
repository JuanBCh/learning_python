import logging

logger = logging.getLogger(__name__) # con __name__ estamos registrando el logger con el nombre del modulo o paquete que estamos trabajando
# Si es importado, el nombre cambiaria al nombre del modulo donde ocurre el evento
print(logger)

logger.warning("Log de adv personalizado")