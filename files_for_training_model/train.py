# https://youtu.be/bluclMxiUkA
"""
La regresión lineal múltiple utiliza varias variables explicativas para predecir el resultado de una variable respuesta.
Existen muchas variables y la regresión lineal múltiple está diseñada para crear un modelo
basado en todas estas variables.

#Enlace del conjunto de datos:
https://cdn.scribbr.com/wp-content/uploads//2020/02/heart.data_.zip?_ga=2.217642335.893016210.1598387608-409916526.1598387608

#Enfermedad cardíaca
El efecto que las variables independientes biking y smoking
tienen sobre la variable dependiente heart disease

el porcentaje de personas que van al trabajo en bicicleta cada día, el porcentaje de personas que fuman,
y el porcentaje de personas con enfermedad cardíaca en una muestra imaginaria de 500 ciudades.


"""

import pandas as pd
import seaborn as sns
import numpy as np

df = pd.read_csv('heart_data.csv')
print(df.head())

df = df.drop("Unnamed: 0", axis=1)
#Algunas gráficas en Seaborn para entender los datos

sns.lmplot(x='biking', y='heart.disease', data=df)  
sns.lmplot(x='smoking', y='heart.disease', data=df)  


x_df = df.drop('heart.disease', axis=1)
y_df = df['heart.disease']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x_df, y_df, test_size=0.3, random_state=42)

from sklearn import linear_model

#Crear objeto de regresión lineal
model = linear_model.LinearRegression()

#Ahora llamamos al método fit para entrenar el modelo usando las variables independientes.
#Y el valor que se debe predecir (Images_Analyzed)

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
#Estos son a, b y c de nuestra ecuación. 
#La intersección se almacena como reg.intercept_
#print(model.coef_, model.intercept_)

#Todo listo para predecir el número de imágenes que alguien analizaría en un momento dado
#print(model.predict([[13, 2, 23]]))
