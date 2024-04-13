# Scope global:
fecha = "02-03-2021"

def scope_local():
    # Scope localL
    local = "local"
    print(f"Scope {local}")

def funcion_principal():
    nombre = "Ana"

    def funcion_anidada():
        print(nombre)
    
    funcion_anidada()

scope_local()
funcion_principal()

# Un closure es una funcion anidada que se comporta como objetop. Ademas tiene acceso a las variables de la funcion que la retiene y recuerda el estado de las variables del scope anterior

def saludar():
    mensaje = "Buen dia"

    def imprimir_saludo():
        print(mensaje)
    
    return imprimir_saludo

saludo = saludar()

saludo()