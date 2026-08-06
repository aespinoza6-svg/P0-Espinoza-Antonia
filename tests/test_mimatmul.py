"""Pruebas iniciales para mimatmul."""
import pytest

from src.mimatmul import mimatmul


def test_matriz_2x2():
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    assert mimatmul(A, B) == [[19, 22], [43, 50]]


def test_matriz_identidad():
    A = [[1, 2, 3]]
    B = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    assert mimatmul(A, B) == [[1, 2, 3]]


def test_dimensiones_incompatibles():
    with pytest.raises(ValueError):
        mimatmul([[1, 2]], [[1, 2, 3]])
