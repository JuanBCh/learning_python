n_entero = "{:.0f}" # Formato de número entero
n_decimal = "{:.2f}" # Formato de número decimal
n_0_izq = "{:0>5}" # Formato de número con ceros a la izquierda
n_0_der = "{:0<6}" # Formato de número con ceros a la derecha
n_miles = "{:,}" # Formato de número con separador de miles

print(n_entero.format(2.4)) # 2
print(n_decimal.format(2.4)) # 2.40
print(n_decimal.format(2.009)) # 2.01
print(n_0_izq.format(2.4)) # 002.4
print(n_0_der.format(2.4)) # 2.4000
print(n_miles.format(1000000)) # 1,000,000

print(f"{2.5:.2f}") # "2.50"