# Un closure es una funcion anidada que hace uso de variables de la funcion que la contiene
# Esta funcion principal retorna la funcion anidada.

def agregar_persona_directorio():
    directorio = {}

    def agregar(nombre, edad, ciudad):
        directorio[nombre] = {"edad": edad, "ciudad": ciudad}
        return directorio
    
    return agregar

almacenar = agregar_persona_directorio()
directorio = almacenar("Jose", 24, "Montevideo")
directorio = almacenar("Paco", 26, "Bogota")

print(directorio)