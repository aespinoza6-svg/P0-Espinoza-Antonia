# P0-Espinoza-Antonia

## Proposito general
Implementar desde cero, sin librerias de algebra lineal, una funcion propia de multiplicacion de matrices (`mimatmul`) en Python puro, medir su rendimiento con un benchmark y compararla con NumPy (`A @ B`). El repositorio documenta todo el proceso, incluye pruebas automaticas, datos de mediciones reales y el grafico final.

## Contenido del repositorio
```
P0-Espinoza-Antonia/
├── README.md
├── AGENTS.md
├── requirements.txt
├── src/
│   ├── system_info.py
│   ├── mimatmul.py
│   └── benchmark.py
├── tests/
│   └── test_mimatmul.py
├── data/
│   ├── system_info.json
│   └── benchmark_results.csv
└── figures/
    └── benchmark.png
```

## Caracteristicas del computador
| Caracteristica | Valor |
|---|---|
| Sistema operativo | Windows 11 (AMD64) |
| Procesador | Intel(R) Core(TM) i5-1035G1 CPU @ 1.00GHz |
| Nucleos fisicos | 4 |
| Procesadores logicos | 8 |
| Memoria RAM total | 7.75 GB |
| Version de Python | 3.14.7 |

La informacion completa se genera con `python src/system_info.py` y se guarda en `data/system_info.json`.

## Instalacion y ejecucion

Clonar el repositorio:

```
git clone https://github.com/aespinoza6-svg/P0-Espinoza-Antonia.git
cd P0-Espinoza-Antonia
```

Crear el ambiente virtual:

```
python -m venv .venv
```

Activar el ambiente (Windows):

```
.venv\Scripts\activate
```

Instalar las dependencias:

```
pip install -r requirements.txt
```

Ejecutar las pruebas:

```
pytest
```

Ejecutar el benchmark:

```
python src/benchmark.py
```

## Implementacion de mimatmul
`src/mimatmul.py` implementa la multiplicacion con ciclos explicitos de Python (tres bucles `for`). No utiliza `A @ B`, `np.matmul`, `np.dot` ni `np.einsum`. Funciona con matrices cuadradas y rectangulares, valida las dimensiones y lanza un error comprensible (`ValueError`) cuando no son compatibles. Los resultados son consistentes con NumPy (verificado en las pruebas).

## Benchmark
`src/benchmark.py` compara `mimatmul` contra NumPy (`A @ B`) con:

- matrices `float64`;
- tamanos 16, 32, 64, 128 y 256;
- 3 repeticiones por tamano y metodo;
- una ejecucion de calentamiento por tamano y metodo;
- reloj `time.perf_counter`;
- una fila por repeticion en `data/benchmark_results.csv`.

### Resultados (promedio de las 3 repeticiones)
| Tamano | mimatmul (s) | NumPy (s) |
|---|---|---|
| 16 | 0.000343 | 0.000003 |
| 32 | 0.003026 | 0.000024 |
| 64 | 0.021265 | 0.000065 |
| 128 | 0.176513 | 0.000366 |
| 256 | 1.926386 | 0.000837 |

El grafico con los datos completos esta en `figures/benchmark.png`.

## Observaciones de rendimiento

**¿mimatmul parece utilizar uno o varios nucleos?**
mimatmul usa ciclos explicitos de Python y el GIL impide el paralelismo real entre hilos; por lo tanto utiliza un solo nucleo.

**¿NumPy parece utilizar uno o varios nucleos?**
NumPy delega en una libreria BLAS optimizada en C/Fortran que, para matrices grandes, paraleliza el calculo y utiliza varios nucleos.

**¿Por que NumPy es mas rapido?**
Porque su nucleo esta implementado en C/Fortran altamente optimizado, usa vectorizacion y paralelizacion, y evita la interpretacion instruccion por instruccion de Python. En el tamano mas grande (256) NumPy fue mas de 2000 veces mas rapido.

**¿Por que las repeticiones no entregan exactamente el mismo tiempo?**
El tiempo de ejecucion varia por el planificador del sistema operativo, la frecuencia variable de la CPU, el estado de la memoria cache, la sincronizacion de OneDrive y otros procesos en segundo plano.

**¿Cual es aproximadamente la matriz cuadrada de mayor tamano que cabria en la RAM libre del computador?**
Una matriz `float64` de n x n ocupa `8 * n^2` bytes. Con la RAM libre observada durante las mediciones (aprox. 1.7 GB) cabria una matriz de aproximadamente `sqrt(1.7e9 / 8) ≈ 14.600` de lado. Con la maquina casi libre (p. ej. 6 GB libres) seria cercana a `sqrt(6e9 / 8) ≈ 27.000`. En la practica, NumPy necesita varias matrices a la vez (A, B y el resultado), por lo que el tamano real utilizable es menor.

## Uso de OpenCode

**¿Que parte realizo correctamente el agente?**
Configuro el entorno (Python, Git, ambiente virtual), creo la estructura del repositorio, implemento `mimatmul`, escribio las pruebas, desarrollo el benchmark y genero el grafico y la documentacion.

**¿Que parte tuvo que corregir o modificar?**
Tuve que organizar el proyecto en la ubicacion final dentro de OneDrive y corregir la rama por defecto de GitHub (`main`). Ademas, el agente ajusto el import de `src` en `benchmark.py` para que funcionara con `python src/benchmark.py`.

**¿Que archivo comprende mejor despues del proyecto?**
`src/mimatmul.py`, porque es la funcion mas sencilla: tres ciclos anidados que siguen la definicion matematica de la multiplicacion de matrices.

**¿Que parte del codigo todavia le resulta menos clara?**
El grafico en escala logaritmica y el por que exacto de la aceleracion de NumPy (la libreria BLAS y sus detalles de paralelizacion), aunque se entiende el resultado global.

## Verificacion
- `pytest`: 5 pruebas pasan.
- `python src/benchmark.py`: genera `data/benchmark_results.csv` y `figures/benchmark.png` a partir de mediciones reales.
