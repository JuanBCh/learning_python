import requests

endpoint_ok = "https://run.mocky.io/v3/6d585571-664c-46e1-8289-769ad70c119a"
endpoint_not_found = "https://run.mocky.io/v3/a94518cb-ba70-4abc-8793-e4d7ee50a914"

class ImposibleDecodificarRespuesta(Exception): #Exception esta definida de forma estandar en Python
    """No se puede decodificar la respuesta en JSON"""

    def __init__(self, mensaje):
        self.mensaje = mensaje

    def __str__(self):
        return f"Ocurrio un error decodificando la respuesta: {self.mensaje}"
    

def procesar_respuesta(endpoint, num_vehiculo):

    try:
        request = requests.get(endpoint)
        status_code = request.status_code
        print(f"El status code es: {status_code}")

        response = request.json()
        print(f"Cantidad de vehiculos: {len(response)}")

        print(f"Caracteristicas del vehiculo seleccionado: {response[num_vehiculo]}")
    except requests.JSONDecodeError:
        raise ImposibleDecodificarRespuesta("Peticion con respuesta vacia")

procesar_respuesta(endpoint=endpoint_ok, num_vehiculo=1)
# procesar_respuesta(endpoint=endpoint_not_found, num_vehiculo=3)