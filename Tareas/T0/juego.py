from parametros import PROB_BESTIA, POND_PUNT
from math import ceil
from random import randint
from string import ascii_uppercase as letras

class Partida:
    def __init__(self, nom, dim_x, dim_y):
        self.jugando = True
        self.username = nom
        self.dim_x = dim_x
        self.dim_y = dim_y
        self.casillas = self.dim_x * self.dim_y
        self.bestias = ceil(self.casillas * PROB_BESTIA)
        self.letras_num = {letras[a] : str(a) for a in range(dim_x)}
        self.tablero = None
        self.visibilidad_tablero = None
        self.crear_tableros()

    def crear_tableros(self):
        tablero_real = [[0 for a in range(self.dim_x)] for b in range(self.dim_y)]
        i = 0
        while i < self.bestias: # poner bestias
            n_casilla = randint(0, self.casillas - 1)
            pos_y = n_casilla // self.dim_x
            pos_x = n_casilla % self.dim_x
            if tablero_real[pos_y][pos_x] != 'N':
                tablero_real[pos_y][pos_x] = 'N'
                i += 1

        for y in range(len(tablero_real)): # contar cuantas bestias adyacentes
            for x in range(len(tablero_real[y])):
                if tablero_real[y][x] != 'N':
                    # 3 de arriba
                    if y > 0:
                        if x > 0 and tablero_real[y - 1][x - 1] == 'N':
                            tablero_real[y][x] += 1
                        if tablero_real[y - 1][x] == 'N':
                            tablero_real[y][x] += 1
                        if x < len(tablero_real[y]) - 1 and tablero_real[y - 1][x + 1] == 'N':
                            tablero_real[y][x] += 1
                    # izquierda
                    if x > 0 and tablero_real[y][x - 1] == 'N':
                        tablero_real[y][x] += 1
                    # derecha
                    if x < len(tablero_real) - 1 and tablero_real[y][x + 1] == 'N':
                        tablero_real[y][x] += 1
                    # 3 de abajo
                    if y < len(tablero_real) - 1:
                        if x > 0 and tablero_real[y + 1][x - 1] == 'N':
                            tablero_real[y][x] += 1
                        if tablero_real[y + 1][x] == 'N':
                            tablero_real[y][x] += 1
                        if x < len(tablero_real[y]) - 1 and tablero_real[y + 1][x + 1] == 'N':
                            tablero_real[y][x] += 1

        self.tablero_real = tablero_real
        self.visibilidad_tablero = [[False for a in range(self.dim_x)] for b in range(self.dim_y)]

    def interpretar_casilla(inp):
        if inp[0].isdigit():
            x = inp[1].upper()
            y = inp[0]
        else:
            x = inp[0]
            y = inp[1].upper()
        return x, y

    # def descubrir_casilla(x, y):
        # TODO