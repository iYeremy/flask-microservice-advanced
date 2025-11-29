# services

Paquete donde vive la lógica compartida entre rutas, API y futuras extensiones.

- `validacion.py`: define los límites aceptados para `horas_luz` y `nivel_riego` y expone `validar_controles(origen)` que devuelve `(valores, errores)`. Cualquier módulo (HTML, API, sockets) puede llamarlo y usar el mismo mensaje de error.
- `simulaciones.py`: carga perezosamente `models/model.pkl`, arma el vector `[horas_luz, nivel_riego]`, llama al modelo de scikit-learn y guarda la simulación en SQLite usando `database.Simulacion`. Retorna `(puntaje, id)` para que cada ruta decida qué mostrar.

Mantener estas piezas aquí evita duplicar lógica en `app.py` y lo deja listo para añadir hilos o sockets sin reescribir las reglas de negocio. 
