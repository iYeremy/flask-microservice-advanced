# https://youtu.be/bluclMxiUkA
"""
Simulador beta de cultivo urbano que estima el puntaje de crecimiento de una parcela
a partir de dos parámetros muy simples: horas de luz solar y nivel de riego/aspersión.

Por ahora se apoya en un modelo sencillo entrenado con datos sintéticos,
pero servirá como base para las siguientes iteraciones del sistema.
"""

from flask import Flask, jsonify, render_template, request

from database import inicializar_bd
from services.simulaciones import ejecutar_simulacion
from services.validacion import validar_controles

# Crear la aplicación Flask e inicializar la base de datos una vez.
app = Flask(__name__)
inicializar_bd()


@app.route('/')
def home():
    """Pantalla principal con el formulario HTML."""
    return render_template('index.html', errors=None, prediction_text=None)


@app.route('/predict', methods=['POST'])
def predict():
    """Recibe datos del formulario, valida, simula y muestra el resultado."""
    controles, errores = validar_controles(request.form)
    if errores:
        return render_template('index.html', errors=errores, prediction_text=None)

    puntaje, _ = ejecutar_simulacion(controles)
    return render_template(
        'index.html',
        prediction_text='Puntaje estimado de crecimiento: {}'.format(puntaje)
    )


@app.route('/api/predict', methods=['POST'])
def predict_api():
    """Endpoint REST que replica la lógica del formulario y responde en JSON."""
    payload = request.get_json(silent=True)
    if payload is None:
        return jsonify({
            "estado": "error",
            "mensaje": "Envíe un cuerpo JSON con horas_luz y nivel_riego."
        }), 400

    controles, errores = validar_controles(payload)
    if errores:
        return jsonify({
            "estado": "error",
            "errores": errores
        }), 400

    puntaje, simulacion_id = ejecutar_simulacion(controles)
    return jsonify({
        "estado": "ok",
        "datos": {
            "id": simulacion_id,
            "horas_luz": controles["horas_luz"],
            "nivel_riego": controles["nivel_riego"],
            "puntaje_crecimiento": puntaje,
        }
    }), 201


# Entrada estándar para ejecutar la app.
if __name__ == "__main__":
    app.run()
