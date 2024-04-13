#  Las funciones lamda sirven para tener funciones anonimas de una
# sola linea. Es para evaluar expresiones cortas.

def calcular_area_cuadrado(lado):
    return lado ** 2

calcular_area = lambda lado: lado ** 2

print(calcular_area_cuadrado(7)) # => 49
print(calcular_area(7)) # => 49

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8]
lista_pares = filter(lambda num: num % 2 == 0, lista_numeros)

print(list(lista_pares)) # => [2, 4, 6, 8]

nueva_lista = map(lambda num: num * 10, lista_numeros)

print(list(nueva_lista)) # => [10, 20, 30, 40, 50, 60, 70, 80]
