# Representacion de los datos
# La representacion interna del tablero sera la de una lista compuesta por seis listas de numeros, estos numeros
# seran 0, para representar el espacio vacio, 1 para representar ficha roja y -1 para representar ficha amarilla
# Las coordenadas del tablero seran del tipo (fila,columna) y tendran su origen en la esquina superior izquierda
#, creciendo las columnas hacia la derecha y las filas hacia abajo

#  !pip install ipythonblocks
#  Vease http://ipythonblocks.org/ para mas informacion

from ipythonblocks import BlockGrid, colors

FILMAX = 6
COLMAX = 7

def obtenNuevoTablero():
    """Crea un nuevo tablero """
    tablero = []
    for i in range(FILMAX):
        tablero.append([0] * COLMAX)

    return tablero

def reseteaTablero(tablero):
    """ Limpia el tablero """
    for col in range(COLMAX):
        for fil in range(FILMAX):
            tablero[fil][col] = 0

def dibujaTablero(tablero):
    """ Dibuja el tablero que se le pasa en formato grafico"""
    grid = BlockGrid(width=COLMAX, height=FILMAX, block_size=25, lines_on=True)

    for fil in range(grid.height):
        for col in range(grid.width):
            if tablero[fil][col] == 1:
                grid[fil,col] = colors['Red']
            elif tablero[fil][col] == -1:
                grid[fil,col] = colors['Green']
            else:
                grid[fil,col] = colors['Black']

    grid.show()

def estaEnTablero(fil, col):
    """ Devuelve verdadero si fil,col estan en el tablero """
    return fil >= 0 and fil < FILMAX and col >= 0 and col < COLMAX

def esUnMovimientoValido(tablero, colJugada):
    """ Devuelve falso si el movimiento a la coord colJugada no es posible,
         y en caso de ser posible devuelve las coordenadas [fil,col]
         de donde queda la ficha tras el movimiento"""

    if not estaEnTablero(0, colJugada):
        return False

    for fil in range(FILMAX-1, -1, -1):
        if (fil == FILMAX-1 and tablero[fil][colJugada] == 0) or \
            (tablero[fil][colJugada] == 0 and  tablero[fil+1][colJugada] != 0) :
            return [ fil, colJugada]

    return False

def daLosMovimientosValidos(tablero):
    """ Devuelve una lista  [fil,col] con los movimientos validos del tablero"""
    movimientosValidos = []

    for col in range(COLMAX):
        movimiento = esUnMovimientoValido(tablero, col)
        if movimiento:
            movimientosValidos.append(movimiento)
    return movimientosValidos

def obtenCopiaTablero(tablero):
    """ Devuelve una copia del tablero """
    copiaTablero = obtenNuevoTablero()

    for fil in range(FILMAX):
        for col in range(COLMAX):
            copiaTablero[fil][col] = tablero[fil][col]

    return copiaTablero

def hazMovimiento(tablero,ficha, colJugada):
    """  Pone la ficha en la columna, y actualiza el tablero.
    Si el movimiento no es posible devuelve falso"""

    if ficha not in (-1,1):
        raise TypeError("El valor de la ficha ha de ser -1 o 1")

    movimiento = esUnMovimientoValido(tablero, colJugada)

    if movimiento == False:
        return False

    tablero[movimiento[0]][movimiento[1]] = ficha

    return True

def daLaVictoria(tablero,tipoFicha, filJugada, colJugada):
    """ Analiza si una ficha en las coords. fil y col da una
    situacion de victoria, en cuyo caso devuelve una lista con las coordenadas de
    las fichas que forman la linea victoriosa, en caso contrario devuelve false """

    if not estaEnTablero(filJugada,colJugada):
        return False

    for cdirection in [0,1,-1]:
        for  fdirection in [0,1,-1]:
            if cdirection == 0 and fdirection == 0:
                continue
            listaFichasGanadoras = [[filJugada, colJugada]]
            c, f = colJugada, filJugada
            c += cdirection   # Primer paso en la direccion
            f += fdirection
            while estaEnTablero(f,c) and tablero[f][c] == tipoFicha:
                listaFichasGanadoras.append( [f,c])
                c += cdirection
                f += fdirection
            if len(listaFichasGanadoras) >= 4:
                return listaFichasGanadoras

    return False
