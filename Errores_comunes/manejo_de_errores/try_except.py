import requests

def procesar_respuesta(endpoint, num_vehiculo):

    try:
        request = requests.get(endpoint)
        status_code = request.status_code
        print(f"El status code es: {status_code}")

        response = request.json()
        print(f"Cantidad de vehiculos: {len(response)}")

        print(f"Caracteristicas del vehiculo seleccionado: {response[num_vehiculo]}")

    except requests.JSONDecodeError: # No se puede transformar la respuesta a JSON
        print("Error al decodificar el JSON")
    except IndexError: #El numero de la lista que queremos seleccionar no existe
        print("El numero de vehiculo seleccionado no existe")
    except Exception as e:
        print(f"Se levanto una excepcion: {e}")

    else: #Esto es si no salto ninguna excepcion
        print("No se levanto ninguna excepcion")

    finally: #Esto se ejecuta siempre
        print("Fin del procesamiento de la respuesta")

endpoint_ok = "https://run.mocky.io/v3/6d585571-664c-46e1-8289-769ad70c119a"
endpoint_not_found = "https://run.mocky.io/v3/a94518cb-ba70-4abc-8793-e4d7ee50a914"
procesar_respuesta(endpoint=endpoint_ok, num_vehiculo=1)
# procesar_respuesta(endpoint=endpoint_not_found, num_vehiculo=3)