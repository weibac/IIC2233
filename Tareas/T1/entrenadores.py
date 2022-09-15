from objetos import Baya, Caramelo, Pocion
from parametros import GASTO_ENERGIA_BAYA, GASTO_ENERGIA_CARAMELO, GASTO_ENERGIA_POCION, MAX_ENERGIA, MIN_ENERGIA, PROB_EXITO_BAYA, PROB_EXITO_CARAMELO, PROB_EXITO_POCION
from programones import ProgramonAgua, ProgramonFuego, ProgramonPlanta
from random import random, choice
from typing import List


class Entrenador:
    def __init__(self, datos, nombre, energia, programones, objetos) -> None:
        self.nombre = nombre
        self.__energia = energia
        self.programones = programones
        self.objetos = objetos
        self.bayas_posibles = []
        self.pociones_posibles = []
        self.caramelos_posibles = []
        self.procesar_init(datos)

    def procesar_init(self, datos):
        # Energia
        self.__energia = int(self.__energia)
        # Programones
        if type(self.programones) == str:
            self.programones = [self.programones]
        for a in range(len(self.programones)):
            if datos.progmnes[self.programones[a]]['tipo'] == 'fuego':
                self.programones[a] = ProgramonFuego(datos.progmnes[self.programones[a]])
            elif datos.progmnes[self.programones[a]]['tipo'] == 'planta':
                self.programones[a] = ProgramonPlanta(datos.progmnes[self.programones[a]])
            elif datos.progmnes[self.programones[a]]['tipo'] == 'agua':
                self.programones[a] = ProgramonAgua(datos.progmnes[self.programones[a]])
            # Bonus megaevolucion
            self.programones[a].cargar_megaev(**datos.evols[self.programones[a].nombre])
        # Objetos en inventario
        if type(self.objetos) == str:
            self.objetos = [self.objetos]
        for a in range(len(self.objetos)):
            if datos.objs[self.objetos[a]]['tipo'] == 'baya':
                self.objetos[a] = Baya(**datos.objs[self.objetos[a]])
            elif datos.objs[self.objetos[a]]['tipo'] == 'pocion':
                self.objetos[a] = Pocion(**datos.objs[self.objetos[a]])
            elif datos.objs[self.objetos[a]]['tipo'] == 'caramelo':
                self.objetos[a] = Caramelo(**datos.objs[self.objetos[a]])
        # Objetos posibles
        for objeto in datos.objs.values():
            if objeto['tipo'] == 'baya':
                self.bayas_posibles.append(Baya(**datos.objs[objeto['nombre']]))
            elif objeto['tipo'] == 'pocion':
                self.pociones_posibles.append(Pocion(**datos.objs[objeto['nombre']]))
            elif objeto['tipo'] == 'caramelo':
                self.caramelos_posibles.append(Caramelo(**datos.objs[objeto['nombre']]))

    @property
    def energia(self):
        return self.__energia

    @energia.setter
    def energia(self, value):
        if value >= MAX_ENERGIA:
            self.__energia = MAX_ENERGIA
        elif value < MIN_ENERGIA:
            self.__energia = MIN_ENERGIA
        else:
            energia_antigua = self.__energia
            self.__energia = value
            print(f'Pérdida energía: {energia_antigua - self.__energia}')
            print(f'La energía bajó de {energia_antigua} a {self.__energia}')

    def estado_entrenador(self):  # TODO
        pass

    def crear_objeto(self, tipo: str):
        if tipo == 'baya':
            prob_exito = PROB_EXITO_BAYA
            gasto = GASTO_ENERGIA_BAYA
            objetos_posibles = self.bayas_posibles
        elif tipo == 'pocion':
            prob_exito = PROB_EXITO_POCION
            gasto = GASTO_ENERGIA_POCION
            objetos_posibles = self.pociones_posibles
        elif tipo == 'caramelo':
            prob_exito = PROB_EXITO_CARAMELO
            gasto = GASTO_ENERGIA_CARAMELO
            objetos_posibles = self.caramelos_posibles
        if gasto > self.energia:  # TODO: segun wsp si no hay suficiente energia se gasta igual
            print(f'Crear un objeto {tipo} cuesta\
                  {gasto} de energia pero solo tienes {self.energia}')
        elif prob_exito > random():
            objeto_creado = choice(objetos_posibles)
            print(f'Has creado un {objeto_creado.nombre} de tipo {objeto_creado.tipo}')
            self.objetos.append(objeto_creado)
            self.energia -= gasto
