# kwargs keyword arguments

def funcion_kuargs(**kwargs):
    print(kwargs)
    for llave, valor in kwargs.items():
        print(f"llave: {llave}, valor: {valor}")
    print(kwargs["nombre"], kwargs["apellido"])

funcion_kuargs(nombre="Paco", apellido="Botero") # {'nombre': 'Paco', 'apellido': 'Botero'}