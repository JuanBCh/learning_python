# Hay columnas en nuestro dataframe que tiene valores NaN o None. Tu
# La trarea es calcular el numero de valores faltantes para cada columnas

import pandas as pd
df = pd.read_csv('empleados.csv', delimiter=";")

# Empiezo desde aqui

missing_values = {}

for column_name in df:
    missing_values[column_name] = 0
    for index in range(len(df)):
        nan = str(df[column_name][index]) == "nan"
        if nan:
            missing_values[column_name] += 1
    print(f"{column_name}: {missing_values[column_name]}")
    
# Ahora la solucion de la profe:

print("\n", "Solucion de la profe:")
print(df.isnull().sum())