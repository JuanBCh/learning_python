class Empleado:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.horas_trabajadas = 0
    
    def trabajar(self, horas):
        self.horas_trabajadas += horas
        print(f"Se agregaron {horas} horas de trabajo")
        print(f"{self.nombre} ha trabajado {self.horas_trabajadas} horas")

pepe = Empleado(nombre="Pepe", apellido="Rosas")
pepe.trabajar(6)
pepe.trabajar(8) 