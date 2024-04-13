import logging

logging.basicConfig(level=logging.DEBUG, filename="ejemplo_logs.log") #Esto hace que se imptiman los mensajes a partir de este nivel de seguridad
# El filename="" es para crear un archivo con los logs
# La configuraion basica se tiene que definir solo una vez por archivo
# Se puede agregar otro parametro filemode="" que por defecto es filemode="a"
# Por defecto, no se borran los archivos viejos, sino que se agrega todo.
# Con el parametro filemode="w", se sobre escriben los datos

logging.debug("Log de debugging")
logging.info("Log informativo")
# Por defecto se van a imprimir en la terminal los de abajo.
# Esto es porque por defecto usa el nivel de warning como primer nivel.
# Solo se imprimen los de nivel 1 o mayor.
logging.warning("Log de advertencia")
logging.error("Log de error")
logging.critical("Log critico")

# Normalmente, estos logs no se usan solo para que aparezcan en consola.
# Tambien se busca que queden guardados en un archivo, para poderles hacer un seguimiento.
# Los archivos creados son de formato .log y son creados con la misma libreria logging