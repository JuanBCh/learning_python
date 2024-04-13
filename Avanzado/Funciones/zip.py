nombres = ["Jose", "Pedro", "Ana"]
apellidos = ["Gonzales", "Ramirez", "Perez"]

nombre_completo = list(zip(nombres, apellidos)) #Para hacer el unzip, es importante que el list() este definido en la variable
print(nombre_completo)

nombre_unzip, apellido_unzip = zip(*nombre_completo)
print(list(nombre_unzip))
print(list(apellido_unzip))

for nombre, apellido in zip(nombres, apellidos):
    print(nombre, apellido)