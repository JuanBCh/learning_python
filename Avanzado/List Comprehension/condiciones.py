# lista_condicionada = [ expresion(elemento) for elemento in objeto_iterable if condicion]

def calcular_cuadrado(num):
    return num**2

def es_par(num):
    return num % 2 == 0

lista_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_cuadrados = [calcular_cuadrado(num) for num in lista_num]
print(lista_cuadrados)

lista_cuadrados_pares = [calcular_cuadrado(num) for num in lista_num if es_par(num)]
print(lista_cuadrados_pares)

lista_resultados = [calcular_cuadrado(num) if es_par(num) else 0 for num in lista_num]
print(lista_resultados)

