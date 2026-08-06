"""mimatmul.py: primera version de multiplicacion de matrices en Python puro."""


def mimatmul(A, B):
    """Multiplica dos matrices A y B representadas como listas de listas."""
    if not A or not B:
        raise ValueError("Las matrices no pueden estar vacias")
    filas = len(A)
    columnas_comunes = len(A[0])
    if columnas_comunes != len(B):
        raise ValueError("Dimensiones incompatibles para multiplicar")
    columnas = len(B[0])

    C = [[0 for _ in range(columnas)] for _ in range(filas)]
    for i in range(filas):
        for j in range(columnas):
            for k in range(columnas_comunes):
                C[i][j] += A[i][k] * B[k][j]
    return C
