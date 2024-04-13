lista_append = [1, 2, 3, 4, 5]
lista_extend = [6, 7, 8, 9, 10]
lista_insert = [11, 12, 13, 14, 15]

lista_letras = ['a', 'b', 'c', 'd', 'e']

lista_append.append(lista_letras)
print(lista_append) # [1, 2, 3, 4, 5, ['a', 'b', 'c', 'd', 'e']]

lista_extend.extend(lista_letras)
print(lista_extend) # [6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

# .insert() recibe dos parametros
# El primero es la posicion de la lista al cual queremos agregar el elemento
# El segundo es el elemento que queremos agregar
lista_insert.insert(len(lista_insert), lista_letras)
print(lista_insert) # [11, 12, 13, 14, 15, ['a', 'b', 'c', 'd', 'e']