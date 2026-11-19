from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
import jwt
from app.services.auth_service import validar_token

bearer = HTTPBearer(auto_error=False)


def usuario_actual(
    cred: HTTPAuthorizationCredentials | None = Depends(bearer),
) -> str:
    if cred is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Falta el access token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    try:
        payload = validar_token(cred.credentials, "access")
        return payload["sub"]
    except (jwt.InvalidTokenError, ValueError, KeyError):
        raise HTTPException(
            status_code=401,
            detail="Access token invalido o expirado",
            headers={"WWW-Authenticate": "Bearer"},
        )
