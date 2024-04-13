import re

def email_valido(email):
    """Verifica el formato del email, no su existencia"""
    formato_valido = r"^([a-z0-9]+[-_.])*[a-z0-9]+@[a-z0-9]+(\.[a-z]{2,})+$" # la r es raw string (sin procesar)
    if re.match(formato_valido, email, re.IGNORECASE):
        return True
    return False


valido = email_valido("juan@mail.com")
print("Email valido:", valido)