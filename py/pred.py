import pandas as pd
from sklearn.linear_model import LogisticRegression

# cargar los datos en un dataframe de pandas
datos = pd.read_csv('data.csv')

# seleccionar las columnas relevantes para la predicción
X = datos[['goles_local', 'goles_visitante', 'Ubicacion']]
y = datos['Resultado']

# convertir la columna 'Ubicacion' en una variable dummy
X = pd.get_dummies(X, columns=['Ubicacion'])

# dividir los datos en conjuntos de entrenamiento y prueba
X_entrenamiento = X[:-10]
X_prueba = X[-10:]
y_entrenamiento = y[:-10]
y_prueba = y[-10:]

# crear un modelo de regresión logística y entrenarlo
modelo = LogisticRegression()
modelo.fit(X_entrenamiento, y_entrenamiento)

# hacer una predicción en los datos de prueba
prediccion = modelo.predict(X_prueba)

# imprimir los equipos y resultados de cada partido
for i, resultado in enumerate(prediccion):
    equipos = datos.loc[len(datos) - 10 + i, ['equipo_local', 'equipo_visitante']].values
    print(f"{equipos[0]} vs {equipos[1]}: {resultado}")

# imprimir la predicción
#print(prediccion)

