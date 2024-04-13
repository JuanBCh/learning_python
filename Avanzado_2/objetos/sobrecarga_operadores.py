class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.distancia_recorrida = 0

    def __add__(self, distancia):
        self.distancia_recorrida += distancia
        return self.distancia_recorrida
    
    def __lt__(self, otra_persona):
        return self.edad < otra_persona.edad


paco = Persona("Paco", 25)
emi = Persona("Emilio", 27)

paco + 5
paco + 8

print(paco.distancia_recorrida)
print(paco > emi) # => False