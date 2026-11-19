from fastapi import APIRouter, HTTPException
from app.dto.calculadora_dto import OperacionEntrada, OperacionSalida
from app.services import calculadora_service as servicio

router = APIRouter(tags=["Calculadora"])


@router.get("/sumar", response_model=OperacionSalida)
def sumar(a: float, b: float):
    resultado = servicio.sumar(a, b)
    return OperacionSalida(resultado=resultado)


@router.get("/restar", response_model=OperacionSalida)
def restar(a: float, b: float):
    resultado = servicio.restar(a, b)
    return OperacionSalida(resultado=resultado)


@router.post("/multiplicar", response_model=OperacionSalida)
def multiplicar(datos: OperacionEntrada):
    resultado = servicio.multiplicar(datos.a, datos.b)
    return OperacionSalida(resultado=resultado)


@router.post("/dividir", response_model=OperacionSalida)
def dividir(datos: OperacionEntrada):
    try:
        resultado = servicio.dividir(datos.a, datos.b)
        return OperacionSalida(resultado=resultado)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error)) from error
