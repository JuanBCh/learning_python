lista_estudiantes = ["Paco", "Javier", "Emilio"]

def verificar_estudiante(nombre, lista_estudiantes):

    if type(nombre) != str:
        raise Exception("El nombre debe ser un texto")
    
    if nombre not in lista_estudiantes:
        raise Exception("El estudiante no esta en la lista")

    return True

verificar_estudiante(1, lista_estudiantes)
# verificar_estudiante("Ana", lista_estudiantes)
# verificar_estudiante("Paco", lista_estudiantes)