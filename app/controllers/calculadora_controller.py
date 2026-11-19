from fastapi import APIRouter, Depends, HTTPException
from app.dto.calculadora_dto import OperacionEntrada, OperacionSalida
from app.security.dependencies import usuario_actual
from app.services import calculadora_service as servicio

router = APIRouter(
    tags=["Calculadora"],
    dependencies=[Depends(usuario_actual)],
)


@router.get("/sumar", response_model=OperacionSalida)
def sumar(a: float, b: float):
    return OperacionSalida(resultado=servicio.sumar(a, b))


@router.get("/restar", response_model=OperacionSalida)
def restar(a: float, b: float):
    return OperacionSalida(resultado=servicio.restar(a, b))


@router.post("/multiplicar", response_model=OperacionSalida)
def multiplicar(datos: OperacionEntrada):
    return OperacionSalida(resultado=servicio.multiplicar(datos.a, datos.b))


@router.post("/dividir", response_model=OperacionSalida)
def dividir(datos: OperacionEntrada):
    try:
        return OperacionSalida(resultado=servicio.dividir(datos.a, datos.b))
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error)) from error
