"""Pruebas de mimatmul."""
import numpy as np
import pytest

from src.mimatmul import mimatmul


def test_caso_conocido():
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    assert mimatmul(A, B) == [[19.0, 22.0], [43.0, 50.0]]


def test_matrices_cuadradas():
    A = [[1, 2, 3]]
    B = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    assert mimatmul(A, B) == [[1.0, 2.0, 3.0]]


def test_matrices_rectangulares():
    A = [[1, 2, 3], [4, 5, 6]]
    B = [[7, 8], [9, 10], [11, 12]]
    assert mimatmul(A, B) == [[58.0, 64.0], [139.0, 154.0]]


def test_consistente_con_numpy():
    rng = np.random.default_rng(42)
    for m, k, n in [(2, 3, 4), (3, 3, 3), (4, 2, 5)]:
        A = rng.random((m, k))
        B = rng.random((k, n))
        resultado = mimatmul(A.tolist(), B.tolist())
        esperado = A @ B
        assert np.allclose(resultado, esperado)


def test_dimensiones_incompatibles():
    with pytest.raises(ValueError):
        mimatmul([[1, 2]], [[1, 2, 3]])
