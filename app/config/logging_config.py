import json
import logging
from datetime import datetime, timezone
from logging.handlers import RotatingFileHandler
from pathlib import Path


class JSONFormatter(logging.Formatter):
    def format(self, record):
        dato = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "level": record.levelname,
            "service": "api-calculadora",
            "environment": __import__("os").getenv("APP_ENV", "dev"),
            "event": record.getMessage(),
        }
        dato.update(getattr(record, "details", {}))
        return json.dumps(dato, ensure_ascii=False, default=str)


def crear_logger(nombre, archivo):
    Path("logs").mkdir(exist_ok=True)
    logger = logging.getLogger(nombre)
    logger.setLevel(logging.INFO)
    logger.propagate = False
    if not logger.handlers:
        handler = RotatingFileHandler(
            f"logs/{archivo}",
            maxBytes=1_000_000,
            backupCount=3,
            encoding="utf-8",
        )
        handler.setFormatter(JSONFormatter())
        logger.addHandler(handler)
    return logger


tecnico = crear_logger("calculadora.tecnico", "tecnico.jsonl")
auditoria = crear_logger("calculadora.auditoria", "auditoria.jsonl")
