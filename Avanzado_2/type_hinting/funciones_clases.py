def calcular_perimetro_cuadrado(lado: float) -> float:
    return 4 * lado

print(calcular_perimetro_cuadrado(4))

class Persona:
    def __init__(self, nombre: str, posicion: int) -> None:
        self.nombre = nombre
        self.posicion = posicion

    def caminar(self, distancia_km: int) -> int:
        self.posicion += distancia_km
        print(self.posicion)
        return self.posicion
    
paco = Persona(nombre="Paco", posicion=0)
posicion_paco = paco.caminar(9)