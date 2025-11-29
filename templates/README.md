# templates

Vistas HTML utilizadas por Flask. Actualmente solo existe `index.html`, heredado del formulario original de la Guía 21 y adaptado a la temática de cultivo urbano.

- **Formulario principal**: inputs `horas_luz` y `nivel_riego` con placeholders aclarando que van de 0 a 100.
- **Mensajes**: muestra errores provenientes de `services/validacion.py` y esconde el texto de resultado cuando no hay predicción válida.
- **Texto auxiliar**: reitera el rango permitido para que usuarios nuevos entiendan qué valores ingresar.

Si se agregan dashboards, tablas de historial u otras vistas, deben ir en esta carpeta para que `render_template` las encuentre.
