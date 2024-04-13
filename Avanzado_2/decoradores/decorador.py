def funcion_decorador(funcion):
    
    def funcion_wrapper():

        print("Dentro de la funcion wrapper")
        funcion()
    
    return funcion_wrapper

def funcion_prueba():
    print("Funcion de prueba")

# Agregar el decorador como instancia
funcion_prueba = funcion_decorador(funcion_prueba)
funcion_prueba()

# Otra manera util
@funcion_decorador
def funcion_prueba_2():
    print("Otra funcion de prueba")

funcion_prueba_2()