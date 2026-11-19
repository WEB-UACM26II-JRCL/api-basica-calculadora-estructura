from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.controllers.calculadora_controller import router

app = FastAPI(title="Calculadora arquitectura en capas")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5500", "http://127.0.0.1:5500"],
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)

app.include_router(router)
