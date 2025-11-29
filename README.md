# Introducción
Simulador beta de cultivo urbano: una app Flask que recibe horas de luz solar y nivel de riego para estimar el puntaje de crecimiento de una parcela ficticia. Este es el punto de partida para incorporar el resto de componentes del proyecto final (persistencia, concurrencia, APIs, etc.).

# Implementaciones
- **Persistencia con SQLAlchemy**: cada simulación validada se almacena en `sqlite:///instance/growth.db` con los parámetros ingresados, el puntaje estimado y la fecha. Esto habilita auditorías, análisis estadísticos y reentrenamientos futuros.
- **API REST JSON**: ruta `POST /api/predict` que recibe `{ "horas_luz": float, "nivel_riego": float }`, reutiliza las mismas validaciones del formulario y devuelve un objeto JSON con el puntaje de crecimiento y el ID de simulación almacenado. Ideal para integrar sensores, automatizaciones o pruebas con herramientas HTTP.
- **Arquitectura modular**: la lógica de validación y simulación se separó en `services/validacion.py` y `services/simulaciones.py`, facilitando su reutilización desde vistas HTML, APIs y futuros componentes concurrentes.

# Creditos
El proyecto tomo de base el ejemplo de DigitalSreeni para desplegar un modelo de machine learning ya entrenado hacia una local web application usando Flask
- Video de DigitalSreeni: https://youtu.be/bluclMxiUkA?t=1342
- Repositorio clonado (Solamente el directorio 268): https://github.com/bnsreenu/python_for_microscopists

# Simple Open License (MIT-style)

Copyright (c) 2025 Yeremy

You can use this code however you want.  
Feel free to copy it, change it, improve it, share it, or use it as part of
your own projects — academic or otherwise.

The only thing I ask is to keep this short notice somewhere in your copy,
just so people know where it originally came from.

This project is provided "as is", with no promises or guarantees.  
Use it at your own risk and have fun.
