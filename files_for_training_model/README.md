# files_for_training_model

Carpeta pensada para todos los insumos del modelo de crecimiento. No es necesaria para ejecutar la app web, pero sí cuando se quiere actualizar `model.pkl`.

-   `growth_data.csv`: dataset sintético (columnas `parcela_id`, `horas_luz`, `nivel_riego`, `puntaje_crecimiento`). Sirve como reemplazo directo del antiguo `heart_data`.
-   `train.py`: script que
    1. Lee el CSV desde esta misma carpeta.
    2. Entrena un `LinearRegression` (scikit-learn).
    3. Guarda el modelo en `files_for_training_model/model.pkl` usando rutas absolutas (importante para que no aparezca en otras carpetas).
    4. Imprime métricas para dejar constancia del entrenamiento.
-   `requirements-train.txt`: dependencias mínimas del script (`numpy`, `pandas`, `scikit-learn`). Instálalas en un entorno aparte para evitar mezclar librerías con la app Flask.

**Flujo recomendado para reentrenar**

```bash
cd files_for_training_model
pip install -r ../requirements-train.txt
python train.py
cp model.pkl ../models/model.pkl
```
