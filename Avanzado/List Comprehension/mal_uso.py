# Malos usos:

# Caso 1
total = sum([num for num in range(100)])
# Correccion
total_corregido = sum(num for num in range(100))

# Caso 2
[print(element) for element in range(1)]
# Correccion
for element in range(10):
    print(element)

# Caso 3
lista_anidada = [[1, 2], [2, 3], [3, 4]]
calores_lista = [numero for elemento in lista_anidada for numero in elemento]
# Correccion
valores_lista = []
for elemento in lista_anidada:
    for numero in elemento:
        valores_lista.append(numero)
