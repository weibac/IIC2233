from PyQt5.QtCore import QTimer, pyqtSignal, QObject

from abc import ABC
import random

import parametros as p


class MetaClass(type(ABC), type(QObject)):
    pass


class Planta(ABC, QObject, metaclass=MetaClass):
    def __init__(self):
        super().__init__()


class Girasol(Planta):

    id = 0

    def __init__(self):
        super().__init__()
        self.id = Girasol.id
        Girasol.id += 1


class Lanzaguisantes(Planta):

    id = 0

    def __init__(self):
        super().__init__()
        self.id = Lanzaguisantes.id
        Lanzaguisantes.id += 1
        self.estado = 'Rep'  # de reposo tmb puede ser Dis de disparando


class LanzaguisantesH(Lanzaguisantes):

    id = 0

    def __init__(self):
        super().__init__()
        self.id = LanzaguisantesH.id
        LanzaguisantesH.id += 1


class Papa(Planta):

    id = 0

    def __init__(self):
        super().__init__()
        self.id = Papa.id
        Papa.id += 1


class Proyectil(QObject):
    def __init__(self, x, y):
        super().__init__()
        self._x = x
        self._y = y
        self.estado = 'Volando'  # Tmb puede ser impactando

    def run(self):
        if self.estado == 'Volando':
            #  moverse
            pass
        elif self.estado == 'Impactando':
            #  actualizar sprite
            pass


class Zombie(QObject):

    id = 0

    def __init__(self, ubicacion):
        super().__init__()
        self.id = Zombie.id
        Zombie.id += 1
        self.frame_caminar = 0
        self.frame_comer = 0
        self.tipo = random.choice(['Wkr', 'Rnr'])
        self.estado = 'Cam'  # Tmb puede ser Com de comiendo
        self._x = p.ANCHO_PANTALLA_JUEGO
        if ubicacion == 'arriba':
            self.y = 157
        else:
            self.y = 157 + 75
        if self.tipo == 'Wkr':
            self._velocidad = p.VELOCIDAD_ZOMBIE
        elif self.tipo == 'Rnr':
            self._velocidad = 1.5 * p.VELOCIDAD_ZOMBIE
        self.paso = self._velocidad * p.TICK
        self._vida = p.VIDA_ZOMBIE
        self._dano_mordida = p.DANO_MORDIDA
        print(f'Zombie creado id {self.id}')

    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, value):
        if value == 0:
            # enviar señal desapareci
            # terminar
            pass  # Desaparecer del mapa
        else:
            self._vida = value

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if value <= 230:
            # perder
            pass
        else:
            self._x = value
