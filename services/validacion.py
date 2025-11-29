"""Validaciones de los parámetros de control del simulador."""

LIMITES_CONTROLES = {
    "horas_luz": (0.0, 100.0),
    "nivel_riego": (0.0, 100.0),
}


def validar_controles(origen):
    """Valida y convierte a float los campos esperados.

    Args:
        origen: Diccionario con posibles claves horas_luz y nivel_riego.

    Returns:
        Tuple (valores_validos, errores) donde valores_validos contiene los floats
        listos para usarse y errores describe cualquier inconsistencia.
    """
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
