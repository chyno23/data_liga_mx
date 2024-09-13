import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv('data.csv')
df['Resultado'] = df['Resultado'].apply(lambda x: 1 if x == 'Local' else 0)
X = df[['Ubicacion', 'Ubicacion_equipo1', 'Ubicacion_equipo2']]
y = df['Resultado']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

logreg = LogisticRegression()
logreg.fit(X_train, y_train)

partido = {'Ubicacion': 'Local', 'Ubicacion_equipo1': 'Local', 'Ubicacion_equipo2': 'Visitante'}
partido_df = pd.DataFrame(partido, index=[0])
partido_X = partido_df[['Ubicacion', 'Ubicacion_equipo1', 'Ubicacion_equipo2']]
proba_local_gane = logreg.predict_proba(partido_X)[:,1]
print('La probabilidad de que el equipo local gane es: {:.2f}'.format(proba_local_gane[0]))
