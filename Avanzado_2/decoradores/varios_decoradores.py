import time

def medir_tiempo_ejecucion(funcion):
    
    def wrapper(*args, **kwargs):
        inicio = time.time()
        funcion(*args, **kwargs)
        fin = time.time()
        print(f"Tiempo total de ejecucion: {fin - inicio}")
    return wrapper

def puntos(funcion):

    def wrapper(*args, **kwargs):
        print(".........")
        funcion(*args, **kwargs)
        print(".........")
        
    return wrapper

@medir_tiempo_ejecucion
@puntos
def recorrer_ciclo():
    for i in range(4):
        print(i)
        time.sleep(1)

recorrer_ciclo()