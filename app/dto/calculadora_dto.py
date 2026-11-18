from pydantic import BaseModel


class OperacionEntrada(BaseModel):
    """Datos que el cliente envia mediante JSON."""
    a: float
    b: float


class OperacionSalida(BaseModel):
    """Estructura de la respuesta de la calculadora."""
    resultado: float
