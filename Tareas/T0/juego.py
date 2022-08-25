from parametros import PROB_BESTIA, POND_PUNT
from math import ceil
from random import shuffle

def crear_tablero(x, y):
    casillas = x * y
    bestias = ceil(casillas * PROB_BESTIA)
    tablero_lineal = ['N' for a in range(bestias)] + [' ' for a in range(casillas - bestias)]
    print(tablero_lineal)
    shuffle(tablero_lineal)
    tablero = [tablero_lineal[a * x:(a + 1) * x] for a in range(y)]
    return tablero