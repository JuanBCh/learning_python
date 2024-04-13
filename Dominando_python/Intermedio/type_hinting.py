# Type hinting es una manera de convertir python en un lenguaje de tipado estatico
# Le aniadimos notaciones al codigo para saber que tipo de variables vamos a usar

def calcular_perimetro_cuadrado(lado: int) -> int:
    return lado * 4

print(calcular_perimetro_cuadrado(4))

# Para usar varios tipos de datos en una variable se usa la libreria typing

from typing import Union

def calcular_area_cuadrado(lado: Union[int, float]) -> Union[int, float]:
    return lado ** 2

print(calcular_area_cuadrado(4))
print(calcular_area_cuadrado(4.1))