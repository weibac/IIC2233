from parametros import PROB_BESTIA, POND_PUNT
from math import ceil
from random import randint


def crear_tableros(dim_x, dim_y):
    casillas = dim_x * dim_y
    bestias = ceil(casillas * PROB_BESTIA)

    tablero_real = [[0 for a in range(dim_x)] for b in range(dim_y)]
    i = 0
    while i < bestias: # poner bestias
        n_casilla = randint(0, casillas - 1)
        pos_y = n_casilla // dim_x
        pos_x = n_casilla % dim_x
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
    return tablero_real
