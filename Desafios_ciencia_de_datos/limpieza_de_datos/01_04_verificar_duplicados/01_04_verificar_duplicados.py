# Averigua si nuestro dataframe tiene filas duplicadas.

import pandas as pd
df = pd.read_csv('empleados.csv', delimiter=";")

print(df.shape)

# Empiezo aqui

new_table = df.drop_duplicates()
duplicates = df.duplicated()

if len(df) == len(new_table):
    print("No hay duplicados")
else:
    print("Hay duplicados en las siguientes filas:")
    for index in range(len(duplicates)):
        if duplicates[index]:
            print(f"Fila {index}")

# Solucion de la profe

print(df[duplicates])