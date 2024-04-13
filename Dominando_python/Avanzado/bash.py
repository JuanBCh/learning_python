# Bash es una herramienta usada para escribir instrucciones hacia el sistema operativo (linux) para windows es bat

import subprocess

nombre_bash = "bash_ejemplo.sh"
contenido = ""

with open(nombre_bash, mode="rb") as archivo_bash:
    contenido = archivo_bash.read()

print(f"Contenido del archivo: {contenido}")

subprocess.call(contenido, shell=True)