"""mimatmul.py: multiplicacion de matrices en Python puro con ciclos explicitos."""


def _validar_matriz(M, nombre):
    """Valida que M sea una lista de listas rectangular no vacia."""
    if not isinstance(M, list) or not M:
        raise ValueError(f"{nombre} debe ser una matriz no vacia")
    if not isinstance(M[0], list):
        raise ValueError(f"{nombre} debe ser una lista de listas")
    columnas = len(M[0])
    if columnas == 0:
        raise ValueError(f"{nombre} no puede tener filas vacias")
    for fila in M:
        if not isinstance(fila, list) or len(fila) != columnas:
            raise ValueError(
                f"{nombre} debe ser una matriz rectangular (todas las filas del mismo largo)"
            )
    return len(M), columnas


def mimatmul(A, B):
    """Multiplica dos matrices A y B usando ciclos explicitos de Python.

    A es m x k y B es k x n. Devuelve una matriz m x n como lista de listas.
    El resultado es consistente con A @ B de NumPy.
    """
    filas_a, columnas_comunes = _validar_matriz(A, "A")
    filas_b, columnas_b = _validar_matriz(B, "B")
    if columnas_comunes != filas_b:
        raise ValueError(
            f"Dimensiones incompatibles: A es {filas_a}x{columnas_comunes} y "
            f"B es {filas_b}x{columnas_b}. El numero de columnas de A debe ser "
            "igual al numero de filas de B."
        )

    C = [[0.0 for _ in range(columnas_b)] for _ in range(filas_a)]
    for i in range(filas_a):
        for j in range(columnas_b):
            for k in range(columnas_comunes):
                C[i][j] += A[i][k] * B[k][j]
    return C
