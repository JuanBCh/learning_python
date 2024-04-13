def calcular_perimetro(*args):
    perimetro = 0
    for lado in args:
        perimetro += lado
    return perimetro

cuadrilatero = calcular_perimetro(1, 2, 3, 4)
print(cuadrilatero)

triangulo = calcular_perimetro(2, 5, 9)
print(triangulo)