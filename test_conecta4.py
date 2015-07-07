"""Modulo de testeo del conecta4."""

import conecta4 as c4

tablero = c4.obtenNuevoTablero()

def setup():
    """Codigo de preparacion de los tests."""
    global tablero
    tablero = c4.reseteaTablero(tablero)


def teardown():
    """Codigo de cierre de los tests."""
    pass


def test_daLaVictoria_vertical():
    """Testeo linea victoriosa vertical."""
    global tablero
    tablero = c4.reseteaTablero(tablero)
    tablero[5][2] = 1
    tablero[4][2] = 1
    tablero[3][2] = 1
    tablero[2][2] = 1
    assert c4.daLaVictoria(tablero, 1, 2, 2) == [[2, 2], [3, 2], [4, 2], [5, 2]]


def test_daLaVictoria_horizontal():
    """Testeo linea victoriosa horizontal."""
    global tablero
    tablero = c4.reseteaTablero(tablero)
    tablero[5][0] = 1
    tablero[5][1] = 1
    tablero[5][2] = 1
    tablero[5][3] = 1
    assert c4.daLaVictoria(tablero, 1, 5, 0) == [[5, 0], [5, 1], [5, 2], [5, 3]]



def test_daLaVictoria_diagonalAscendente():
    """Testeo linea victoriosa diagonal ascendente."""
    global tablero
    tablero = c4.reseteaTablero(tablero)
    tablero[5][0] = 1
    tablero[4][1] = 1
    tablero[3][2] = 1
    tablero[2][3] = 1
    assert c4.daLaVictoria(tablero, 1, 5, 0) == [[5, 0], [4, 1], [3, 2], [2, 3]]



def test_daLaVictoria_diagonalDescendente():
    """Testeo linea victoriosa diagonal descendente."""
    global tablero
    tablero = c4.reseteaTablero(tablero)
    tablero[2][0] = 1
    tablero[3][1] = 1
    tablero[4][2] = 1
    tablero[5][3] = 1
    assert c4.daLaVictoria(tablero, 1, 2, 0) == [[2, 0], [3, 1], [4, 2], [5, 3]]


def test_daLaVictoria_SinVictoria1():
    """Testeo condicion sin victoria 1."""
    global tablero
    tablero = c4.reseteaTablero(tablero)
    tablero[5][2] = -1
    tablero[4][2] = 1
    tablero[3][2] = 1
    tablero[2][2] = 1
    assert c4.daLaVictoria(tablero, 1, 2, 2) == False
