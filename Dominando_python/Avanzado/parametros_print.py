print("Cadena de texto")

variable = 1
print(f"Variable: {variable}")

print("Elemento 1", "Elemento 2", "Elemento 3", sep="/")
print("Elemento 4", "Elemento 5", "Elemento 6", sep="\n")

print("Primero", end=".") # Por defecto es "\n"
print("Segundo")

with open("print_ejemplo.txt", "w") as archivo:
    print("Hello world!", file=archivo)

import time

print("inico", end="...", flush=False)
time.sleep(2)
print("fin")