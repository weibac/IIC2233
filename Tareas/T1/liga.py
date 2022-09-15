from entrenadores import Entrenador
from random import randint, shuffle


class LigaProgramon:
    def __init__(self, datos) -> None:
        self.entrenadores = [Entrenador(datos, **datos.entrens[nom]) for nom in datos.entrens]
        self.perdedores = []
        self.ronda_actual = 1
        self.campeon = None

    def resumen_campeonato(self):
        participantes = []
        participando = []
        for entrenador in self.entrenadores:
            if entrenador.nombre not in self.perdedores:
                participando.append(entrenador.nombre)
            participantes.append(entrenador.nombre)
        print('Resumen campeonato:')
        print(f'Participantes: {", ".join(participantes)}')
        print(f'Ronda actual: {self.ronda_actual}')
        print(f'Siguen compitiendo: {", ".join(participando)}')
        print()

    def simular_ronda(self, indice_jugador, indice_programon):  # TODO: print numero ronda
        # Definir orden en el que luchan los entrenadores
        orden_luchar = []
        for a in range(len(self.entrenadores)):
            if self.entrenadores[a].nombre not in self.perdedores:
                orden_luchar.append(a)
        shuffle(orden_luchar)
        # Combate por parejas
        iterador = 1
        while iterador < len(orden_luchar):
            # Desempaquetar entrenadores
            entrenador_1 = self.entrenadores[orden_luchar[iterador - 1]]
            entrenador_2 = self.entrenadores[orden_luchar[iterador]]
            print(f'Enfrentamiento {iterador // 2 + 1}')
            print(f'{entrenador_1.nombre} se enfrenta a {entrenador_2.nombre}')
            # Elegir programones
            if orden_luchar[iterador - 1] == indice_jugador:
                ind_prog_1 = indice_programon
                ind_prog_2 = randint(0, len(entrenador_2.programones) - 1)
            elif orden_luchar[iterador] == indice_jugador:
                ind_prog_1 = randint(0, len(entrenador_1.programones) - 1)
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
        # Revisar si el usuario perdio
        if self.entrenadores[indice_jugador].nombre in self.perdedores:
            usuario_perdio = True
        else:
            usuario_perdio = False
        self.ronda_actual += 1
        return usuario_perdio
