# https://youtu.be/bluclMxiUkA
"""
Simulador beta de cultivo urbano que estima el puntaje de crecimiento de una parcela
a partir de dos parámetros muy simples: horas de luz solar y nivel de riego/aspersión.

Por ahora se apoya en un modelo sencillo entrenado con datos sintéticos,
pero servirá como base para las siguientes iteraciones del sistema.
"""


import numpy as np
from flask import Flask, request, render_template
import pickle

#Create an app object using the Flask class. 
app = Flask(__name__)

#Load the trained model. (Pickle file)
model = pickle.load(open('models/model.pkl', 'rb'))

#Define the route to be home. 
#The decorator below links the relative route of the URL to the function it is decorating.
#Here, home function is with '/', our root directory. 
#Running the app sends us to index.html.
#Note that render_template means it looks for the file in the templates folder. 

#use the route() decorator to tell Flask what URL should trigger our function.
@app.route('/')
def home():
    return render_template('index.html')

#You can use the methods argument of the route() decorator to handle different HTTP methods.
#GET: A GET message is send, and the server returns data
#POST: Used to send HTML form data to the server.
#Add Post method to the decorator to allow for form submission. 
#Redirect to /predict page with the output
@app.route('/predict',methods=['POST'])
def predict():

    sunlight_hours = float(request.form.get('sunlight_hours'))  #Horas equivalentes de luz solar
    watering_level = float(request.form.get('watering_level'))  #Nivel de riego/aspersión
    features = [np.array([sunlight_hours, watering_level])]  #Formato [[a, b]] para el modelo
    prediction = model.predict(features)  # features Must be in the form [[a, b]]

    output = round(prediction[0], 2)

    return render_template(
        'index.html',
        prediction_text='Puntaje estimado de crecimiento: {}'.format(output)
    )


#When the Python interpreter reads a source file, it first defines a few special variables. 
#For now, we care about the __name__ variable.
#If we execute our code in the main program, like in our case here, it assigns
# __main__ as the name (__name__). 
#So if we want to run our code right here, we can check if __name__ == __main__
#if so, execute it here. 
#If we import this file (module) to another file then __name__ == app (which is the name of this python file).

if __name__ == "__main__":
    app.run()
