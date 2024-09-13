import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Carga los datos en un dataframe
datos = pd.read_csv("datos.csv")

# Separa los datos de entrada (equipo local, equipo visitante y goles locales) de los de salida (goles visitantes)
X = datos.iloc[:, :-1].values
y = datos.iloc[:, 3].values

# Codifica los nombres de los equipos como variables numéricas
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X_1 = LabelEncoder()
X[:, 0] = labelencoder_X_1.fit_transform(X[:, 0])
labelencoder_X_2 = LabelEncoder()
X[:, 1] = labelencoder_X_2.fit_transform(X[:, 1])

# Aplica one-hot encoding a las variables categóricas (nombres de los equipos)
onehotencoder = OneHotEncoder(categories = [0,1])
X = onehotencoder.fit_transform(X).toarray()

# Elimina una columna de cada variable categórica para evitar la trampa de las variables ficticias
X = X[:, 1:]

# Divide los datos en conjunto de entrenamiento y conjunto de prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Entrena el modelo de regresión lineal con los datos de entrenamiento
regresion = LinearRegression()
regresion.fit(X_train, y_train)

# Realiza predicciones sobre el conjunto de prueba
y_pred = regresion.predict(X_test)

# Evalúa la calidad de las predicciones utilizando el coeficiente de determinación R^2
from sklearn.metrics import r2_score
r2 = r2_score(y_test, y_pred)
print("Coeficiente de determinación R^2:", r2)
