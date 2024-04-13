import psutil

def recursos_usados_CPU():
    nucleos = psutil.cpu_count(logical=False) # True para logicos, False para fisicos
    print(f"La cantidad de nucleos es {nucleos}")

    carga = psutil.getloadavg()
    print(f"La carga promedio es: {carga}")

    uso = psutil.cpu_percent(interval=5, percpu=True)
    print(f"El porcentaje de uso de la cpu es: {uso}")


recursos_usados_CPU()
