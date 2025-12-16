"""
Ejercicio 9: leer una fecha (día, mes, año) introducida como "dd/mm/aaaa"
y mostrar cada componente por separado.

La función:

Recibe un string con formato "d/m/aaaa" o "dd/mm/aaaa".

Devuelve (dia, mes, año) como enteros.

Si el formato o los rangos son incorrectos, lanza ValueError.
"""

def parse_date(date_str: str) -> tuple[int, int, int]:
    """Devuelve (día, mes, año) como enteros a partir de una cadena d/m/aaaa."""
    # TODO: usa split("/"), convierte a int y valida rangos sencillos
    date_str = date_str.strip()
    partes = date_str.split("/")
    if len(partes) != 3:
        raise ValueError("El formato debe ser d/m/aaaa")

    try:
        dia, mes, año = map(int, partes)
    except ValueError:
        raise ValueError("Los valores de la fecha deben ser enteros")

    if not (1 <= dia <= 31):
        raise ValueError("El día debe estar entre 1 y 31")
    if not (1 <= mes <= 12):
        raise ValueError("El mes debe estar entre 1 y 12")
    if año <= 0:
        raise ValueError("El año debe ser positivo")

    return dia, mes, año

