# Encontrar y eliminar filas con muchos valores nulos

import pandas as pd
df = pd.read_csv('empleados.csv', delimiter=";")

print(df.head(20))
print(df.shape)

# Empiezo desde aqui

for column in df:
    conditions = column == "Nombre" or column == "Salario" or column == "Gerencia" or column == "Departamento"
    new_df = df
    if conditions:
        for index in range(len(df)):
            data = str(df[column][index])
            if data == "nan":
                print(data)
                new_df.drop(index=index)

print("df\n", df)
print("new_df\n", new_df)
# No pude

# Solucion de la profe

print(df[df.isnull().any(axis=1)])

df_actualizado = df.dropna(axis=0, thresh=5)
print("df_actualziada\n", df_actualizado) # => Hay 5 filas menos