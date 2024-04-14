import pandas as pd
df = pd.read_csv('empleados.csv', delimiter=";")

print(df.head(20))
print(df.shape)
print(df.isnull().sum())

# Empiezo desde aqui

for column_name in df:
    if df[column_name].isnull().sum() == len(df):
        new_df = df.drop(columns=[column_name])

print("/n", new_df.isnull().sum())

# Solucion de la profe:

df_actualizado = df.drop(axis=1, columns=["Apellido"])
# axis=1 nos permite eliminar una columna con valores nulos

print("\n", df_actualizado)