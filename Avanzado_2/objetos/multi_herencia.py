class AnimalTerrestre:

    def comer(self):
        print("Animal terrestre comiendo")
    
    def caminar(self):
        print("Caminando")

class AnimalVolador:

    def comer(self):
        print("Animal volador comiendo")
    
    def volar(self):
        print("Volando")

class Pajaro(AnimalTerrestre, AnimalVolador):
    pass


pato = Pajaro()
pato.caminar()
pato.volar()
pato.comer() # => Como ambas clases padre tienen este metodo, python va a elegir la primera clase padre que se menciona al crear la clase hijo.