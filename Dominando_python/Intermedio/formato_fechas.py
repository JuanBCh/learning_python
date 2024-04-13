from datetime import datetime

ahora = datetime.now()
print(ahora, type(ahora)) 

fecha = ahora.strftime("%d-%m-%Y")
print(fecha, type(fecha))

hora_24 = ahora.strftime("%H:%M:%S")
print(hora_24, type(hora_24))

hora_12 = ahora.strftime("%I:%M:%S %p")
print(hora_12, type(hora_12))