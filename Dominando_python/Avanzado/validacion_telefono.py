import phonenumbers

def validar_telefono(telefono: str, codigo_pais=None):
    try:
        telefono = phonenumbers.parse(telefono, codigo_pais)
        return phonenumbers.is_valid_number(telefono)
    except Exception as e:
        print(e)
        return False

# valido = validar_telefono("099988876", "UY") # => True
# valido = validar_telefono("99988876", "UY") # => True
valido = validar_telefono("+59899988876") # => True
print(valido)

