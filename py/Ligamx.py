import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import numpy as np
# Cargar los datos en un DataFrame de Pandas
data = pd.read_csv('Ligamx.csv')

# Transformar las columnas de "Dia" y "Fecha" a valores numéricos
data['Hora'] = pd.to_datetime(data['Hora'])
data['Hora'] = data['Hora'].dt.dayofyear
data['Fecha'] = pd.to_datetime(data['Fecha'])
data['Fecha'] = data['Fecha'].dt.dayofyear

# Transformar las columnas de "Local" y "Visitante" a valores numéricos utilizando One-Hot Encoding
local_encoding = pd.get_dummies(data['Local'], prefix='Local')
visitante_encoding = pd.get_dummies(data['Visitante'], prefix='Visitante')
data = pd.concat([data, local_encoding, visitante_encoding], axis=1)
data.drop(['Local', 'Visitante'], axis=1, inplace=True)

# Dividir los datos en dos conjuntos: uno para entrenar el modelo y otro para evaluarlo
X_train, X_test, y_train, y_test = train_test_split(data.drop(['Goles_local', 'Goles_Visitante'], axis=1), 
                                                    data[['Goles_local', 'Goles_Visitante']], 
                                                    test_size=0.3, random_state=42)

# Crear y entrenar el modelo utilizando regresión logística
model = LogisticRegression()
model.fit(X_train, y_train)

# Hacer una predicción de los resultados de los partidos utilizando el conjunto de datos de evaluación
y_pred = model.predict(X_test)

# Comparar los resultados predichos con los resultados reales para evaluar la precisión del modelo
print('Precisión del modelo: {:.2f}%'.format(model.score(X_test, y_test)*100))
