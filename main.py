from time import perf_counter
from uuid import uuid4
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.config.logging_config import tecnico
from app.controllers.auth_controller import router as auth_router
from app.controllers.calculadora_controller import router as calculadora_router

app = FastAPI(title="Calculadora seguridad y logs")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5500", "http://127.0.0.1:5500"],
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type", "Authorization"],
)


@app.middleware("http")
async def registrar_peticion(request: Request, call_next):
    request.state.request_id = str(uuid4())
    inicio = perf_counter()
    estado = 500
    try:
        response = await call_next(request)
        estado = response.status_code
        response.headers["X-Request-ID"] = request.state.request_id
        return response
    except Exception:
        tecnico.exception(
            "error_no_controlado",
            extra={
                "details": {
                    "request_id": request.state.request_id,
                    "method": request.method,
                    "path": request.url.path,
                }
            },
        )
        raise
    finally:
        tecnico.info(
            "http_request",
            extra={
                "details": {
                    "request_id": request.state.request_id,
                    "method": request.method,
                    "path": request.url.path,
                    "status": estado,
                    "latency_ms": round((perf_counter() - inicio) * 1000, 2),
                }
            },
        )


app.include_router(auth_router)
app.include_router(calculadora_router)
