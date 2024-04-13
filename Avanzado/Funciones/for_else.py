nombres = ["Paco", "Ana", "Pedro", "Jose", "Maria"]

for nombre in nombres:
    print(nombre)
else: # Este se ejecuta solamente si todos los ciclos son ejecutados.
    print("Ciclo terminado")

for nombre in nombres:
    if nombre == "Pedro":
        break
    print(nombre)
else: # Este se ejecuta solamente si todos los ciclos son ejecutados.
    print("ciclo terminado")
