import csv
import os


ruta = "csv_vacio.csv" # Esta ruta es relativa porque se va a crear con respecto a este archivo
ruta_absoluta = "~/Documentos/Formacion/Python/Avanzado/" #No funciona porque no es la ruta real (creo)
ruta_absoluta_os = os.path.join(os.getcwd(), "csv_vacio.csv") # Nos garantiza la compatibilidad en cualquier computadora

archivo_abierto = open(ruta_absoluta_os, "w") # w de write
writer = csv.writer(archivo_abierto, delimiter=",") # la variable se llama asi por con convension
archivo_abierto.close() # Hay que cerrar el archivo
