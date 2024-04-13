# Una IP o direccion IP es un numero identificador de un dispositivo que se conecta a internet a travez del protocolo TCP IP.

import requests

request = requests.get("https://ident.me") # Esta api retorna una ip publica del dispositivo que hace la peticion
ip_publica = request.text
print(ip_publica) 

# import public_ip as ip  # ==> No funciona?
# ip_publica_2 = ip.get()
# print(ip_publica_2)