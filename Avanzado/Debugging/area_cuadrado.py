def calcular_area_cuadrado(lado):
    area = lado*lado
    return area


lado_cuadrado = [1, 3, 4]
area_cuadrados = []


for lado in lado_cuadrado:
    # Si ponemos el break en la linea 8, usando display una vez en lado y continue, vemos cada iteracion
    area = calcular_area_cuadrado(lado)
    area_cuadrados.append(area)


# Para el debugging, en la consola escribir:
# python -m pdb {nombre_del_archivo}