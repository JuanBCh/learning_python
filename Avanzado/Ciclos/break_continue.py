nombres = ["Paco", "Emilio", "Ana", "Paula", "Jose"]

for elemento in nombres:
    if elemento == "Paula":
        break
    if elemento == "Emilio":
        continue
    print(elemento)
