import time

def medir_tiempo_ejecucion(funcion):
    
    def wrapper(*args, **kwargs): # => con estos parametros, podemos usar la funcion sin importar si la funcion que queremos decorar tiene o no parametros
        inicio = time.time()
        funcion(*args, **kwargs)
        fin = time.time()
        print(f"Tiempo total de ejecucion: {fin - inicio}")
    return wrapper

@medir_tiempo_ejecucion
def recorrer_ciclo():
    for i in range(3):
        print(i)
        time.sleep(1)

recorrer_ciclo()