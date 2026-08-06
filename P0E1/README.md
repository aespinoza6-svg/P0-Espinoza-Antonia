# P0-Espinoza-Antonia

## Proposito general
Implementar desde cero, sin usar librerias de algebra lineal, una funcion propia de multiplicacion de matrices (`mimatmul`) y comparar su rendimiento con `numpy.matmul`. El proyecto avanza de forma incremental: P0E1 (configuracion e inicio) y P0E2 (benchmark, grafico y documentacion final).

## Sistema operativo
- Windows 11 (AMD64)

## Version de Python
- 3.14.7

## Ambiente virtual

Crear el ambiente virtual:

```
python -m venv .venv
```

Activar el ambiente virtual (Windows):

```
.venv\Scripts\activate
```

Instalar las dependencias:

```
pip install -r requirements.txt
```

## Como ejecutar el proyecto

Obtener la informacion del computador:

```
python src/system_info.py
```

Ejecutar las pruebas:

```
pytest
```

## Estado actual
El ambiente de desarrollo esta configurado (Python, Git, GitHub, OpenCode y editor). El repositorio incluye la informacion basica del computador en `data/system_info.json`, una primera version de `mimatmul` y sus pruebas iniciales. La implementacion completa, el benchmark definitivo y el grafico final se entregaran en P0E2.
