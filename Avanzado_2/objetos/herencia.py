class Persona:

    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.documento = None
    
    def agregar_documento(self, numero_documento):
        self.documento = numero_documento
        print("Documento guardado")


class Deportista(Persona):

    def __init__(self, nombre, apellido, edad, deporte):
        super().__init__(nombre, apellido, edad)
        self.deporte = deporte
    

pepe = Deportista("Pepe", "Pepas", 26, "Tenis")
pepe.agregar_documento(1452)
print(pepe.deporte)