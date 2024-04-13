#  lista = [ expresion(elemento) for elemento in objeto_iterable]

def calcular_cuarado(numero):
    return numero**2

lista_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista_cuadrados= []
for num in lista_num:
    cuadrado = calcular_cuarado(num)
    lista_cuadrados.append(cuadrado)
print("Ciclo for:", lista_cuadrados)

# Para convertir esto en list comprehension:

list_comprehension = [num**2 for num in lista_num]
print("List comprehension:", lista_cuadrados)

# Ahora con una funcion:

list_f_comprehension = [calcular_cuarado(num) for num in lista_num]
print("Funcion: ", list_f_comprehension)

