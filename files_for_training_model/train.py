# https://youtu.be/bluclMxiUkA
"""
Prototipo de entrenamiento para el simulador de cultivo urbano.
Usamos un conjunto de datos sintético que representa parcelas de prueba donde se ajustan
las horas de luz solar recibida, el nivel de riego/aspersión y el puntaje de crecimiento
obtenido en cada cultivo.

La regresión lineal múltiple nos permite estimar el crecimiento esperado a partir de ambos
parámetros de control y funcionará como base hasta contar con mediciones reales.
"""

from pathlib import Path
import pandas as pd
import seaborn as sns
import numpy as np

BASE_DIR = Path(__file__).parent
df = pd.read_csv(BASE_DIR / 'growth_data.csv')
print(df.head())

df = df.drop("plot_id", axis=1)
#Algunas gráficas en Seaborn para entender el comportamiento del crecimiento

sns.lmplot(x='sunlight_hours', y='growth_score', data=df)  
sns.lmplot(x='watering_level', y='growth_score', data=df)  


x_df = df.drop('growth_score', axis=1)
y_df = df['growth_score']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x_df, y_df, test_size=0.3, random_state=42)

from sklearn import linear_model

#Crear objeto de regresión lineal
model = linear_model.LinearRegression()

#Ahora llamamos al método fit para entrenar el modelo usando las variables independientes.
#Y el valor que se debe predecir (puntaje de crecimiento estimado)

model.fit(X_train, y_train) #Variables independientes, variable dependiente a predecir
print(model.score(X_train, y_train))  #Imprime el valor R^2, una medida de qué tan bien


prediction_test = model.predict(X_test)    
print(y_test, prediction_test)
print("Mean sq. errror between y_test and predicted =", np.mean(prediction_test-y_test)**2)

import pickle
pickle.dump(model, open('model.pkl','wb'))

model = pickle.load(open('model.pkl','rb'))
print(model.predict([[20.1, 56.3]]))


#El modelo está listo. Veamos los coeficientes, almacenados como reg.coef_.
#Representan la influencia de cada control sobre el crecimiento estimado.
#La intersección se almacena como reg.intercept_
#print(model.coef_, model.intercept_)

#Ejemplo rápido para pronosticar el crecimiento de una parcela hipotética
#print(model.predict([[13, 2]]))
