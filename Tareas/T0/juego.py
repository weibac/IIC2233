from parametros import PROB_BESTIA, POND_PUNT
from math import ceil
from random import randint
from string import ascii_uppercase as letras


class Partida:
    def __init__(self, nom, dim_x, dim_y):
        self.username = nom
        self.dim_x = dim_x
        self.dim_y = dim_y
        self.jugando = True
        self.turno = 0
        self.casillas = self.dim_x * self.dim_y
        self.descubiertas = set()
        self.sin_bestias = set()
        self.bestias = ceil(self.casillas * PROB_BESTIA)
        self.letras_num = {letras[a]: a for a in range(dim_x)}
        self.tablero_real = None
        self.tablero_visible = None
        self.crear_tableros()

    def crear_tableros(self):
        tablero_real = [[0 for a in range(self.dim_x)] for b in range(self.dim_y)]
        i = 0
        while i < self.bestias:  # poner bestias
            n_casilla = randint(0, self.casillas - 1)
            pos_y = n_casilla // self.dim_x
            pos_x = n_casilla % self.dim_x
            if tablero_real[pos_y][pos_x] != 'N':
                tablero_real[pos_y][pos_x] = 'N'
                i += 1

        for y in range(len(tablero_real)):  # contar cuantas bestias adyacentes
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
                    if x < len(tablero_real[0]) - 1 and tablero_real[y][x + 1] == 'N':
                        tablero_real[y][x] += 1
                    # 3 de abajo
                    if y < len(tablero_real) - 1:
                        if x > 0 and tablero_real[y + 1][x - 1] == 'N':
                            tablero_real[y][x] += 1
                        if tablero_real[y + 1][x] == 'N':
                            tablero_real[y][x] += 1
                        if x < len(tablero_real[y]) - 1 and tablero_real[y + 1][x + 1] == 'N':
                            tablero_real[y][x] += 1

        for y in range(len(tablero_real)):  # pasar a str y construir set sin_bestias
            for x in range(len(tablero_real[y])):
                tablero_real[y][x] = str(tablero_real[y][x])
                if tablero_real[y][x] != 'N':
                    self.sin_bestias.add((x, y))

        self.tablero_real = tablero_real
        self.tablero_visible = [[' ' for a in range(self.dim_x)] for b in range(self.dim_y)]

    def interpretar_coords(self, coords):
        x = self.letras_num[coords[0].upper()]
        y = int(coords[1:])
        return x, y

    def probar_casilla(self, x, y):
        if self.tablero_real[y][x] == '0':  # caso recursivo bonus
            self.tablero_visible[y][x] = self.tablero_real[y][x]
            self.descubiertas.add((x, y))
            # 3 de arriba
            if y > 0:
                if x > 0 and (x - 1, y - 1) not in self.descubiertas:
                    self.probar_casilla(x - 1, y - 1)
                if (x, y - 1) not in self.descubiertas:
                    self.probar_casilla(x, y - 1)
                if x < self.dim_x - 1 and (x + 1, y - 1) not in self.descubiertas:
                    self.probar_casilla(x + 1, y - 1)
            # izquierda
            if x > 0 and (x - 1, y) not in self.descubiertas:
                self.probar_casilla(x - 1, y)
            # derecha
            if x < self.dim_x - 1 and (x + 1, y) not in self.descubiertas:
                self.probar_casilla(x + 1, y)
            # 3 de abajo
            if y < self.dim_y - 1:
                if x > 0 and (x - 1, y + 1) not in self.descubiertas:
                    self.probar_casilla(x - 1, y + 1)
                if (x, y + 1) not in self.descubiertas:
                    self.probar_casilla(x, y + 1)
                if x < self.dim_x - 1 and (x + 1, y + 1) not in self.descubiertas:
                    self.probar_casilla(x + 1, y + 1)
        elif self.tablero_real[y][x] == 'N':  # pierdes
            self.jugando = False
        else:
            self.tablero_visible[y][x] = self.tablero_real[y][x]
            self.descubiertas.add((x, y))
        if self.sin_bestias <= self.descubiertas:  # ganas
            self.jugando = False

    def calcular_puntaje(self):
        return self.bestias * len(self.descubiertas) * POND_PUNT
