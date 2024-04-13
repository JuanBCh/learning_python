# enumerate(iterable, start=0)

nombres = ["Paco", "Ana", "Jose", "Roberto"]
nombres_enumerado = list(enumerate(nombres, start=5))

print(nombres_enumerado)

for num, name in nombres_enumerado:
    print(f"{num}: {name}")

for i, name in enumerate(nombres): # Para no usar list() podemos hacerlo asi
    print(f"{i}: {name}")