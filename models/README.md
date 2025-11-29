# models

Contiene únicamente el modelo que la aplicación Flask carga al arrancar.

- `model.pkl`: archivo generado por `files_for_training_model/train.py`. No se versiona automáticamente; cada vez que se reentrena el modelo hay que copiar manualmente el archivo actualizado a esta carpeta (`cp files_for_training_model/model.pkl models/model.pkl`).

La app (`services/simulaciones.py`) lee siempre `models/model.pkl`, lo que garantiza que el mismo archivo se use tanto para la vista HTML como para la API REST.
