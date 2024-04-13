import asyncio
import time

def funcion_sincrona():
    print("Ejecutando funcion sincrona")
    time.sleep(1)
    print("Fin de funcion sincrona")

async def funcion_asincrona():
    print("Ejecutando funcion asincrona")
    await asyncio.sleep(1)
    print("Fin de funcion asincrona")

async def main():
    corrutinas = [funcion_asincrona(), funcion_asincrona()]
    await asyncio.gather(*corrutinas)

asyncio.run(main())

funcion_sincrona()
funcion_sincrona()
