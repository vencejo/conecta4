"""
Representacion de los datos

La representacion interna del tablero sera la de una lista compuesta por seis listas de numeros, estos numeros
seran 0, para representar el espacio vacio, 1 para representar ficha roja y -1 para representar ficha amarilla
Las coordenadas del tablero seran del tipo (fila,columna) y tendran su origen en la esquina superior izquierda
, creciendo las columnas hacia la derecha y las filas hacia abajo.
"""

#  !pip install ipythonblocks
#  Vease http://ipythonblocks.org/ para mas informacion

from ipythonblocks import BlockGrid, colors


class Tablero():

    """Guarda la informacion y los metodos relacionados con el tablero."""

    def __init__(self, filmax=6, colmax=7, numFichasParaGanar=4):
        """Inicializa el Tablero."""
        self.filmax = filmax
        self.colmax = colmax
        self.numFichasParaGanar = numFichasParaGanar
        self.tablero = self.obtenNuevoTablero()

    def obtenNuevoTablero(self):
        """Crea un nuevo tablero."""
        tablero = []
        for i in range(self.filmax):
            tablero.append([0] * self.colmax)
        return tablero

    def reseteaTablero(self):
        """Limpia el tablero."""
        for col in range(self.colmax):
            for fil in range(self.filmax):
                self.tablero[fil][col] = 0

    def dibujaTablero(self,  fichasGanadoras=None):
        """Dibuja  en formato grafico en ipython, el tablero que se le pasa,
        si se le pasa una lista con fichas ganadoras, las resalta en amarillo."""
        grid = BlockGrid(width=self.colmax, height=self.filmax, block_size=25, lines_on=True)

        for fil in range(grid.height):
            for col in range(grid.width):
                if fichasGanadoras and [fil, col] in fichasGanadoras:
                    grid[fil, col] = colors['Yellow']
                    continue
                if self.tablero[fil][col] == 1:
                    grid[fil, col] = colors['Red']
                elif self.tablero[fil][col] == -1:
                    grid[fil, col] = colors['Green']
                else:
                    grid[fil, col] = colors['Black']

        grid.show()

    def estaEnTablero(self, fil, col):
        """Devuelve verdadero si fil,col estan en el tablero."""
        return fil >= 0 and fil < self.filmax and col >= 0 and col < self.colmax

    def esUnMovimientoValido(self, colJugada):
        """ Devuelve falso si el movimiento a la coord colJugada no es posible,
             y en caso de ser posible devuelve las coordenadas [fil,col]
             de donde queda la ficha tras el movimiento"""

        if not self.estaEnTablero(0, colJugada):
            return False

        for fil in range(self.filmax-1, -1, -1):
            if (fil == self.filmax-1 and self.tablero[fil][colJugada] == 0) or \
                (self.tablero[fil][colJugada] == 0 and  self.tablero[fil+1][colJugada] != 0) :
                return [fil, colJugada]

        return False

    def daLosMovimientosValidos(self):
        """Devuelve una lista  [fil,col] con los movimientos validos del tablero."""
        movimientosValidos = []

        for col in range(self.colmax):
            movimiento = self.esUnMovimientoValido(col)
            if movimiento:
                movimientosValidos.append(movimiento)
        return movimientosValidos

    def obtenCopiaTablero(self):
        """Devuelve una copia del tablero."""
        copiaTablero = self.obtenNuevoTablero()

        for fil in range(self.filmax):
            for col in range(self.colmax):
                copiaTablero[fil][col] = self.tablero[fil][col]

        return copiaTablero

    def hazMovimiento(self, ficha, colJugada):
        """Pone la ficha en la columna, y actualiza el tablero.
        Si el movimiento no es posible devuelve falso."""

        if ficha not in (-1,1):
            raise TypeError("El valor de la ficha ha de ser -1 o 1")

        movimiento = self.esUnMovimientoValido(colJugada)

        if movimiento is False:
            return False

        self.tablero[movimiento[0]][movimiento[1]] = ficha

        return True

    def daLaVictoria(self, tipoFicha, filJugada, colJugada):
        """Analiza si una ficha en las coords. fil y col da una
        situacion de victoria, en cuyo caso devuelve una lista con las coordenadas de
        las fichas que forman la linea victoriosa, en caso contrario devuelve false."""

        if not self.estaEnTablero(filJugada, colJugada):
            return False

        for cdirection in [0, 1, -1]:
            for fdirection in [0, 1, -1]:
                if cdirection == 0 and fdirection == 0:
                    continue
                listaFichasGanadoras = [[filJugada, colJugada]]
                c, f = colJugada, filJugada
                c += cdirection   # Primer paso en la direccion
                f += fdirection
                while self.estaEnTablero(f, c) and self.tablero[f][c] == tipoFicha:
                    listaFichasGanadoras.append([f, c])
                    c += cdirection
                    f += fdirection
                if len(listaFichasGanadoras) >= self.numFichasParaGanar:
                    return listaFichasGanadoras

        return False

    def hayGanador(self):
        """ Dado un tablero se va moviendo por todas las fichas del mismo a ver si alguna es ganadora
        Si gana la ficha -1 devuelve (-1,listafichasGanadoras),
        si gana la 1 devuelve (1,listafichasGanadoras)
        y si no hay ganadora devuelve False """
        for fil in range(self.filmax):
            for col in range(self.colmax):
                tipoFicha = self.tablero[fil][col]
                if tipoFicha in (-1,1):
                    fichasGanadoras = self.daLaVictoria(tipoFicha, fil, col)
                    if fichasGanadoras is not False:
                        return (tipoFicha, fichasGanadoras)
        return False

if __name__ == '__main__':
    c4 = Tablero()
    c4.obtenNuevoTablero()
