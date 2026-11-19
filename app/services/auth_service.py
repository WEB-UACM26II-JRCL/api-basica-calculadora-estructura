import os
import secrets
from datetime import datetime, timedelta, timezone
from uuid import uuid4
import jwt

SECRET = os.environ["JWT_SECRET"]
ALGORITMO = "HS256"


# Las credenciales son solo para la practica (sin BD).
def verificar_credenciales(usuario: str, password: str) -> bool:
    return (secrets.compare_digest(usuario, os.environ["DEMO_USER"])
            and secrets.compare_digest(password, os.environ["DEMO_PASSWORD"]))


def crear_token(usuario: str, tipo: str, minutos: int) -> str:
    ahora = datetime.now(timezone.utc)
    payload = {
        "sub": usuario,
        "type": tipo,
        "iat": ahora,
        "exp": ahora + timedelta(minutes=minutos),
        "jti": str(uuid4()),
    }
    return jwt.encode(payload, SECRET, algorithm=ALGORITMO)


def validar_token(token: str, tipo: str) -> dict:
    payload = jwt.decode(
        token,
        SECRET,
        algorithms=[ALGORITMO],
        options={"require": ["sub", "exp", "type", "jti"]},
    )
    if payload.get("type") != tipo:
        raise ValueError("Tipo de token incorrecto")
    return payload
