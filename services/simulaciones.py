"""Servicios de simulacion: carga del modelo y persistencia del resultado."""

from pathlib import Path
import pickle
import numpy as np

from database import Simulacion, sesion_bd

RUTA_MODELO = Path(__file__).resolve().parents[1] / "models" / "model.pkl"
_MODELO = None


def obtener_modelo():
    """Carga el modelo solo una vez y lo reutiliza."""
    global _MODELO
    if _MODELO is None:
        with RUTA_MODELO.open('rb') as archivo:
            _MODELO = pickle.load(archivo)
    return _MODELO


def ejecutar_simulacion(controles):
    """Calcula el puntaje y almacena la simulación.

    Args:
        controles: diccionario con horas_luz y nivel_riego validados.

    Returns:
        tuple(puntaje, id_simulacion)
    """
    modelo = obtener_modelo()
    caracteristicas = [np.array([controles["horas_luz"], controles["nivel_riego"]])]
    prediccion = modelo.predict(caracteristicas)
    puntaje = round(prediccion[0], 2)

    with sesion_bd() as session:
        simulacion = Simulacion(
            horas_luz=controles["horas_luz"],
            nivel_riego=controles["nivel_riego"],
            puntaje_crecimiento=puntaje,
        )
        session.add(simulacion)
        session.flush()
        simulacion_id = simulacion.id

    return puntaje, simulacion_id
