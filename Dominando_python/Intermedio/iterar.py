# Si bien iterar ciclos anidados no esta mal, pueden surguir complicaciones
# Usamos la funcion zip() para iterar dos listas al mismo tiempo

lista_nombres = ["Juan", "Pedro", "Maria", "Jose"]
lista_edades = [25, 30, 35, 40]

datos_zip = zip(lista_nombres, lista_edades)

print(list(datos_zip))

# zip() retorna una lista de indice no mayor a la lista mas corta que le enviamos

for nombre, edad in zip(lista_nombres, lista_edades):
    print(nombre, edad)