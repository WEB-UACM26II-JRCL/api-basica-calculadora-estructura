from fastapi import APIRouter, HTTPException, Request
import jwt
from app.config.logging_config import auditoria
from app.dto.auth_dto import (
    LoginEntrada,
    TokensSalida,
    RefreshEntrada,
    AccessSalida,
)
from app.services import auth_service as auth

router = APIRouter(prefix="/auth", tags=["Autenticacion"])


@router.post("/login", response_model=TokensSalida)
def login(datos: LoginEntrada, request: Request):
    exito = auth.verificar_credenciales(datos.usuario, datos.password)
    auditoria.info(
        "login",
        extra={
            "details": {
                "request_id": request.state.request_id,
                "action": "LOGIN",
                "actor_id": datos.usuario,
                "outcome": "SUCCESS" if exito else "DENIED",
            }
        },
    )
    if not exito:
        raise HTTPException(status_code=401, detail="Credenciales invalidas")
    return TokensSalida(
        access_token=auth.crear_token(datos.usuario, "access", 15),
        refresh_token=auth.crear_token(datos.usuario, "refresh", 7 * 24 * 60),
    )


@router.post("/refresh", response_model=AccessSalida)
def refresh(datos: RefreshEntrada, request: Request):
    try:
        payload = auth.validar_token(datos.refresh_token, "refresh")
    except (jwt.InvalidTokenError, ValueError):
        auditoria.warning(
            "refresh_denegado",
            extra={
                "details": {
                    "request_id": request.state.request_id,
                    "action": "REFRESH",
                    "outcome": "DENIED",
                }
            },
        )
        raise HTTPException(status_code=401, detail="Refresh token invalido")
    usuario = payload["sub"]
    auditoria.info(
        "refresh",
        extra={
            "details": {
                "request_id": request.state.request_id,
                "action": "REFRESH",
                "actor_id": usuario,
                "outcome": "SUCCESS",
            }
        },
    )
    return AccessSalida(access_token=auth.crear_token(usuario, "access", 15))
