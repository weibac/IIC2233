from entrenadores import Entrenador
from random import randint, shuffle
from math import log2


class LigaProgramon:
    def __init__(self, datos) -> None:
        self.entrenadores = [Entrenador(datos, **datos.entrens[nom]) for nom in datos.entrens]
        self.perdedores = []
        self.ronda_actual = 0
        self.campeon = None

    def resumen_campeonato(self):  # TODO
        pass

    def simular_ronda(self, indice_jugador, indice_programon):  # TODO: print numero ronda
        # Definir orden en el que luchan los entrenadores
        orden_luchar = []
        for a in range(len(self.entrenadores)):
            if self.entrenadores[a].nombre not in self.perdedores:
                orden_luchar.append(a)
        shuffle(orden_luchar)
        # Combate por parejas
        iterador = 1
        while iterador <= len(orden_luchar) / 2:
            # Desempaquetar entrenadores
            entrenador_1 = self.entrenadores[orden_luchar[iterador - 1]]
            entrenador_2 = self.entrenadores[orden_luchar[iterador]]
            print(f'Entrentamiento {iterador // 2 + 1}')
            print(f'{entrenador_1.nombre} se enfrenta a {entrenador_2.nombre}')
            # Elegir programones
            if orden_luchar[iterador - 1] == indice_jugador:
                ind_prog_1 = indice_programon
            elif orden_luchar[iterador] == indice_jugador:
                ind_prog_2 = indice_programon
            else:
                ind_prog_1 = randint(0, len(entrenador_1.programones) - 1)
                ind_prog_2 = randint(0, len(entrenador_2.programones) - 1)
            programon_1 = entrenador_1.programones[ind_prog_1]
            programon_2 = entrenador_2.programones[ind_prog_2]
            print(f'{entrenador_1.nombre} elige a {programon_1.nombre}')
            print(f'{entrenador_2.nombre} elige a {programon_2.nombre}')
            # Luchar y ver quien gana
            if programon_1.luchar(programon_2):
                print(f'{entrenador_1.nombre} derrota a {entrenador_2.nombre}')
                self.perdedores.append(entrenador_2.nombre)
            else:
                print(f'{entrenador_2.nombre} derrota a {entrenador_1.nombre}')
                self.perdedores.append(entrenador_1.nombre)
            # Empaquetar programones y entrenadores
            entrenador_1.programones[ind_prog_1] = programon_1
            entrenador_2.programones[ind_prog_2] = programon_2
            self.entrenadores[orden_luchar[iterador - 1]] = entrenador_1
            self.entrenadores[orden_luchar[iterador]] = entrenador_2
            print('')
            iterador += 2
