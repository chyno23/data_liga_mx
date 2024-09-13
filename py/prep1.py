import pandas as pd
from sklearn.linear_model import LogisticRegression

# cargar los datos en un dataframe de pandas
datos = pd.read_csv('data.csv')

# seleccionar las columnas relevantes para la predicción
X = datos[['goles_local', 'goles_visitante', 'Ubicacion']]
y = datos['Resultado']

# convertir la columna 'Ubicacion' en una variable dummy
X = pd.get_dummies(X, columns=['Ubicacion'])

# entrenar el modelo
modelo = LogisticRegression()
modelo.fit(X, y)

# crear una fila de datos para el próximo partido
prox_partido = pd.DataFrame({
    'goles_local': [0],
    'goles_visitante': [0],
    'Ubicacion_equipo1': [1],
    'Ubicacion_equipo2': [0],
    'equipo': ['equipo1']
})

# convertir la columna 'Ubicacion' en una variable dummy
prox_partido = pd.get_dummies(prox_partido, columns=['Ubicacion'])

# predecir la probabilidad de cada posible resultado
proba = modelo.predict_proba(prox_partido)

# imprimir las probabilidades
print('Probabilidad de victoria local:', proba[0][0])
print('Probabilidad de empate:', proba[0][1])
print('Probabilidad de victoria visitante:', proba[0][2])
