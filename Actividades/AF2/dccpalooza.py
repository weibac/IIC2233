from parametros import PROBABILIDAD_EVENTO, PUBLICO_EXITO, PUBLICO_INICIAL, \
                       PUBLICO_TERREMOTO, AFINIDAD_OLA_CALOR, \
                       AFINIDAD_LLUVIA, PUBLICO_OLA_CALOR
from random import random, choice


class DCCPalooza:

    def __init__(self):
        self.artista_actual = ''
        self.__dia = 1
        self.line_up = []
        self.cant_publico = PUBLICO_INICIAL
        self.artistas = []
        self.prob_evento = PROBABILIDAD_EVENTO
        self.suministros = []

    @property
    def dia(self):
        return self.__dia

    @property
    def funcionando(self):
        return self.exito_del_concierto and self.dia <= 3

    @property
    def exito_del_concierto(self):
        return self.cant_publico >= PUBLICO_EXITO

    def imprimir_estado(self):
        print(f"Día: {self.__dia}\nCantidad de Personas: "
              f"{self.cant_publico}\nArtistas:")
        for artista in self.line_up:
            print(f"- {artista.nombre}")

    def ingresar_artista(self, artista):
        self.line_up.append(artista)
        print(f'Se ha ingresado un nuevo artista!!!\n{artista}')

    def asignar_lineup(self):
        self.line_up = []
        for artista in self.artistas:
            if self.dia == artista.dia_presentacion:
                self.ingresar_artista(artista)

    def nuevo_dia(self):
        # COMPLETAR
        if self.funcionando:
            self.dia += 1
            print('Comienza un nuevo dia')

    def ejecutar_evento(self):
        # COMPLETAR
        if self.prob_evento:
            evento_choice = choice([0, 1, 2])
            if evento_choice == 0:
                for a in range(len(self.artistas)):
                    if self.artistas[a].nombre == self.artista_actual:
                        self.artistas[a].afininidad_con_publico -= AFINIDAD_LLUVIA
                        print('Llueve! :C')
            elif evento_choice == 1:
                self.cant_publico -= PUBLICO_TERREMOTO
                print('TERREMOTO! CORRAN!\nSe han ido {PUBLICO_TERREMOTO} personas.')
            else:
                for a in range(len(self.artistas)):
                    if self.artistas[a].nombre == self.artista_actual:
                        self.artistas[a].afininidad_con_publico -= AFINIDAD_OLA_CALOR
                        print('Qué calor! :/')
                self.cant_publico -= PUBLICO_OLA_CALOR
                print('Nos estamos asando!\nSe han ido {PUBLICO_OLA_CALOR} personas.')