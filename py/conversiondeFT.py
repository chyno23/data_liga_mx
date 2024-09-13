import pandas as pd

# Leer el archivo CSV en un DataFrame de Pandas
df = pd.read_csv('dataliga1/mexico-master/2020s/2020-21/mx.1.csv')

# Crear nuevas columnas con los goles locales y visitantes
df[['goles_local', 'goles_visitante']] = df['FT'].str.split('-', expand=True).astype(int)

# Eliminar la columna "resultado" original
df.drop(['FT'], axis=1, inplace=True)

# Mostrar el resultado
print(df)
