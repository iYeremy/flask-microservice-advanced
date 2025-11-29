# templates

Vistas HTML utilizadas por Flask. Actualmente solo existe `index.html`, heredado del formulario original de la Guía 21 y adaptado a la temática de cultivo urbano.

## index.html
- Estilos integrados (`<style>`) para mostrar un panel con fondo oscuro, inputs con etiquetas y un botón con gradiente. Esto hace que la demostración en video luzca más profesional sin depender de archivos CSS externos.
- Campos `horas_luz` y `nivel_riego` mantienen placeholders y validaciones requeridas.
- Sección de errores (`.errores`) que muestra la lista proveniente de `services/validacion.py`.
- Caja de resultado (`.resultado`) que solo aparece cuando hay predicción, resaltando el puntaje calculado.
- Texto recordatorio para el rango 0‑100 acorde al modelo actual.

Si se agregan dashboards, tablas de historial u otras vistas, deben ir en esta carpeta para que `render_template` las encuentre.
