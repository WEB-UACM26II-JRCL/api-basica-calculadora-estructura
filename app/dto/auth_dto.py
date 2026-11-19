from pydantic import BaseModel


class LoginEntrada(BaseModel):
    usuario: str
    password: str


class TokensSalida(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class RefreshEntrada(BaseModel):
    refresh_token: str


class AccessSalida(BaseModel):
    access_token: str
    token_type: str = "bearer"
