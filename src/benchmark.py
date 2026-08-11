"""benchmark.py: compara mimatmul (Python puro) con NumPy (A @ B).

Genera data/benchmark_results.csv y figures/benchmark.png.
"""
import csv
import sys
import time
from pathlib import Path

PROYECTO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROYECTO))

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from src.mimatmul import mimatmul

DATA_DIR = PROYECTO / "data"
FIGURES_DIR = PROYECTO / "figures"

TAMANOS = [16, 32, 64, 128, 256]
REPETICIONES = 3


def medir_tiempo(funcion, *args):
    """Mide el tiempo de funcion(*args) con time.perf_counter."""
    inicio = time.perf_counter()
    funcion(*args)
    return time.perf_counter() - inicio


def generar_grafico(datos, archivo_png):
    """Genera el grafico de benchmark a partir de las mediciones."""
    tiempos = {}
    for metodo, tamano, repeticion, tiempo_s in datos:
        tiempos.setdefault(metodo, {}).setdefault(tamano, []).append(tiempo_s)

    fig, ax = plt.subplots(figsize=(8, 5))
    for metodo, color in [("mimatmul", "tab:blue"), ("numpy", "tab:orange")]:
        tamanos = sorted(tiempos[metodo])
        medias = [np.mean(tiempos[metodo][n]) for n in tamanos]
        ax.plot(tamanos, medias, marker="o", color=color, label=metodo)

    ax.set_xlabel("Tamano de la matriz (n x n)")
    ax.set_ylabel("Tiempo de ejecucion (s)")
    ax.set_title("Comparacion: mimatmul vs NumPy")
    ax.set_yscale("log")
    ax.legend()
    ax.grid(True, which="both", alpha=0.4)
    fig.tight_layout()

    archivo_png.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(archivo_png, dpi=150)
    plt.close(fig)


def main():
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    datos = []
    filas_csv = [["metodo", "tamano", "repeticion", "tiempo_s"]]

    rng = np.random.default_rng()
    for n in TAMANOS:
        A = rng.random((n, n))
        B = rng.random((n, n))
        A_lista = A.tolist()
        B_lista = B.tolist()

        medir_tiempo(mimatmul, A_lista, B_lista)
        medir_tiempo(lambda a, b: a @ b, A, B)

        for rep in range(1, REPETICIONES + 1):
            t_mimatmul = medir_tiempo(mimatmul, A_lista, B_lista)
            datos.append(("mimatmul", n, rep, t_mimatmul))
            filas_csv.append(["mimatmul", n, rep, round(t_mimatmul, 9)])

            t_numpy = medir_tiempo(lambda a, b: a @ b, A, B)
            datos.append(("numpy", n, rep, t_numpy))
            filas_csv.append(["numpy", n, rep, round(t_numpy, 9)])

            print(f"n={n:4d} rep={rep}: mimatmul={t_mimatmul:.6f}s numpy={t_numpy:.6f}s")

    archivo_csv = DATA_DIR / "benchmark_results.csv"
    with open(archivo_csv, "w", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)
        escritor.writerows(filas_csv)
    print(f"\nResultados guardados en {archivo_csv}")

    archivo_png = FIGURES_DIR / "benchmark.png"
    generar_grafico(datos, archivo_png)
    print(f"Grafico guardado en {archivo_png}")


if __name__ == "__main__":
    main()
