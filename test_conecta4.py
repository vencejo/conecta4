"""Modulo de testeo del conecta4."""

import conecta4

c4 = conecta4.Tablero()

def setup():
    """Codigo de preparacion de los tests."""
    global c4
    c4.reseteaTablero()


def teardown():
    """Codigo de cierre de los tests."""
    pass


def test_daLaVictoria_vertical():
    """Testeo linea victoriosa vertical."""
    global c4
    c4.reseteaTablero()
    c4.tablero[5][2] = 1
    c4.tablero[4][2] = 1
    c4.tablero[3][2] = 1
    c4.tablero[2][2] = 1
    assert c4.daLaVictoria(1, 2, 2) == [[2, 2], [3, 2], [4, 2], [5, 2]]


def test_daLaVictoria_horizontal():
    """Testeo linea victoriosa horizontal."""
    global c4
    c4.reseteaTablero()
    c4.tablero[5][0] = 1
    c4.tablero[5][1] = 1
    c4.tablero[5][2] = 1
    c4.tablero[5][3] = 1
    assert c4.daLaVictoria(1, 5, 0) == [[5, 0], [5, 1], [5, 2], [5, 3]]


def test_daLaVictoria_diagonalAscendente():
    """Testeo linea victoriosa diagonal ascendente."""
    global c4
    c4.reseteaTablero()
    c4.tablero[5][0] = 1
    c4.tablero[4][1] = 1
    c4.tablero[3][2] = 1
    c4.tablero[2][3] = 1
    assert c4.daLaVictoria(1, 5, 0) == [[5, 0], [4, 1], [3, 2], [2, 3]]


def test_daLaVictoria_diagonalDescendente():
    """Testeo linea victoriosa diagonal descendente."""
    global c4
    c4.reseteaTablero()
    c4.tablero[2][0] = 1
    c4.tablero[3][1] = 1
    c4.tablero[4][2] = 1
    c4.tablero[5][3] = 1
    assert c4.daLaVictoria(1, 2, 0) == [[2, 0], [3, 1], [4, 2], [5, 3]]


def test_daLaVictoria_SinVictoria1():
    """Testeo condicion sin victoria 1."""
    global c4
    c4.reseteaTablero()
    c4.tablero[5][2] = -1
    c4.tablero[4][2] = 1
    c4.tablero[3][2] = 1
    c4.tablero[2][2] = 1
    assert c4.daLaVictoria(1, 2, 2) == False
