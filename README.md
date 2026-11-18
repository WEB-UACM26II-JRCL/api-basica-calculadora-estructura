# API basica: calculadora y estructura
Practica de Programacion Web con Python y FastAPI.
## Requisitos
Python 3.10 o superior
## Instalacion
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
## Ejecucion
uvicorn main:app --reload
## Documentacion
http://127.0.0.1:8000/docs

## Capturas de comunicacion Frontend - Backend

**Resta (8 - 2):**
![Resta](capturas/resta.png)

**Multiplicacion (8 * 2):**
![Multiplicacion](capturas/multiplicar.png)

**Division (8 / 2):**
![Division](capturas/division.png)

**Division entre cero (Error HTTP 400):**
![Division entre cero](<capturas/division a cero.png>)

### Prueba Paso 5.2 (CORS - Simulando frontend externo)
![Prueba de paso 5.2](capturas/paso5_2.png)

### Prueba Paso 7.1 (Validacion de DTO de entrada)
![Prueba de paso 7.1](capturas/paso7_1.png)
