from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Calculadora version inicial")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5500", "http://127.0.0.1:5500"],
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)

class Numeros(BaseModel):
    a: float
    b: float

@app.get("/sumar")
def sumar(a: float, b: float):
    return {"resultado": a + b}

@app.get("/restar")
def restar(a: float, b: float):
    return {"resultado": a - b}

@app.post("/multiplicar")
def multiplicar(datos: Numeros):
    return {"resultado": datos.a * datos.b}

@app.post("/dividir")
def dividir(datos: Numeros):
    if datos.b == 0:
        raise HTTPException(status_code=400, detail="No se puede dividir entre cero")
    return {"resultado": datos.a / datos.b}