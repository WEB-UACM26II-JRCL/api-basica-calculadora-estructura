def sumar(a: float, b: float) -> float:
    """Devuelve la suma de dos valores."""
    return a + b


def restar(a: float, b: float) -> float:
    """Devuelve la diferencia entre dos valores."""
    return a - b


def multiplicar(a: float, b: float) -> float:
    """Devuelve el producto de dos valores."""
    return a * b


def dividir(a: float, b: float) -> float:
    """Devuelve el cociente; rechaza divisor igual a cero."""
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b
