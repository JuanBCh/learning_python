#  Operador de asignacion: ':='
#  (walrus := "walrus")

def calcular_cuadrado(num):
    return num ** 2

lista_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista_pares = []
for num in lista_num:
    # cuadrado = calcular_cuadrado(num)
    if (cuadrado := calcular_cuadrado(num)) % 2 == 0:
        lista_pares.append(cuadrado)
        print(f"El cuadrado de {num} es {cuadrado}, un numero par")
    else:
        print(f"El cuadrado de {num} es {cuadrado}, un numero inpar")

# Vamos por list comprehension
        
    
pares_comprehension = [cuadrado for num in lista_num if (cuadrado := calcular_cuadrado(num)) % 2 == 0]
print(pares_comprehension)
