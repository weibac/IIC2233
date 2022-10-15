from PyQt5.QtCore import QTimer, pyqtSignal, QObject

import random

import parametros as p


class Planta(QObject):
    def __init__(self, x, y):
        super().__init__()
        self._x = x
        self._y = y


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
    senal_alogic_act_zombie = pyqtSignal(int, tuple, tuple)

    def __init__(self):
        super().__init__()
        self.id = Zombie.id
        Zombie.id += 1
        self.frame_caminar = 0
        self.frame_comer = 0
        self.tipo = random.choice(['Walker', 'Runner'])
        self.estado = 'Caminando'  # Tmb puede ser comiendo
        self._x = p.ANCHO_PANTALLA_JUEGO
        self.y = 300  # TODO
        if self.tipo == 'Walker':
            self._velocidad = p.VELOCIDAD_ZOMBIE
        elif self.tipo == 'Runner':
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
        if value <= 100:
            # perder
            pass
        else:
            self._x = value
