# range(inicio, fin, paso)

serie_1 = range(5) # [0, 1, 2, 3, 4]
print(list(serie_1))

serie_2 = range(5,10) # [5, 6, 7, 8, 9]
print(list(serie_2))

serie_3 = range(3,11,2) # [3, 5, 7, 9]
print(list(serie_3))

for elem in serie_3:
    print(elem)