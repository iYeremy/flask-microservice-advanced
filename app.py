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

from database import Simulacion, inicializar_bd, sesion_bd

#Create an app object using the Flask class. 
app = Flask(__name__)
inicializar_bd()

LIMITES_CONTROLES = {
    "horas_luz": (0.0, 100.0),
    "nivel_riego": (0.0, 100.0),
}


def validar_controles(origen):
    errores = {}
    valores = {}
    for campo, (limite_inferior, limite_superior) in LIMITES_CONTROLES.items():
        valor_crudo = origen.get(campo)
        if valor_crudo is None:
            errores[campo] = "Campo requerido."
            continue
        try:
            valor = float(valor_crudo)
        except ValueError:
            errores[campo] = "Debe ser un número válido."
            continue
        if not limite_inferior <= valor <= limite_superior:
            errores[campo] = f"Debe estar entre {limite_inferior} y {limite_superior}."
            continue
        valores[campo] = valor
    return valores, errores

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

    controles, errores = validar_controles(request.form)
    if errores:
        return render_template('index.html', errors=errores, prediction_text=None)

    caracteristicas = [np.array([controles["horas_luz"], controles["nivel_riego"]])]  #Formato [[a, b]] para el modelo
    prediction = model.predict(caracteristicas)  # features Must be in the form [[a, b]]

    output = round(prediction[0], 2)
    with sesion_bd() as session:
        session.add(
            Simulacion(
                horas_luz=controles["horas_luz"],
                nivel_riego=controles["nivel_riego"],
                puntaje_crecimiento=output,
            )
        )

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
