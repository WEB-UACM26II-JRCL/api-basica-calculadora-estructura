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

### Prueba Paso 8.2 (Logica de negocio en capa de servicio)
![Prueba de paso 8.2](capturas/paso8_2.png)

### Prueba Paso 8.2 (Capa de servicio en interprete Python)
![Prueba de paso 8.2](capturas/paso8_2_1.png)

### Prueba Paso 9.1 (Controlador, rutas HTTP y error 400)
![Prueba de paso 9.1](capturas/paso9_1.png)

## Estructura
etapa_1/main.py: version inicial
main.py: inicio de la version estructurada
app/controllers/: rutas HTTP
app/dto/: datos de entrada y salida
app/services/: operaciones matematicas

## Ejemplos de uso
GET /sumar?a=8&b=2
GET /restar?a=8&b=2
POST /multiplicar {"a": 8, "b": 2}
POST /dividir {"a": 8, "b": 2}

## Verificacion
Abrir http://127.0.0.1:8000/docs
Probar las cuatro operaciones y la division entre cero.

### Prueba Paso 10.2 (Contraste con version inicial en puerto 8001)
![Version inicial puerto 8001](capturas/paso10_2_puerto8001.png)

### Pruebas Paso 11.1 (Arquitectura en capas - Puerto 8000)
**1. Suma (`GET /sumar?a=8&b=2` -> `10`):**
![Prueba suma](capturas/paso11_1_sumar.png)

**2. Resta (`GET /restar?a=8&b=2` -> `6`):**
![Prueba resta](capturas/paso11_1_restar.png)

**3. Multiplicacion (`POST /multiplicar` -> `16`):**
![Prueba multiplicacion](capturas/paso11_1_multiplicar.png)

**4. Division (`POST /dividir` -> `4`):**
![Prueba division](capturas/paso11_1_dividir.png)

**5. Division entre cero (`POST /dividir` -> `HTTP 400`):**
![Prueba division entre cero](capturas/paso11_1_dividir_cero.png)

**6. Validacion de entrada incompleta (`POST /multiplicar` sin `b` -> `HTTP 422`):**
![Prueba error 422](capturas/paso11_1_error_422.png)
