from parametros import VIDA_PEKKA, RECUPERACION_VIDA_PEKKA, ORO_INICIAL, \
    PONDERADOR_BARBAROS
from threading import Lock


class CentroUrbano:

    def __init__(self) -> None:
        # Completar
        self.lock_oro = Lock()
        self.lock_chozas = Lock()
        # Tuve que bajarlos para que iniciara bien
        self.__oro = ORO_INICIAL
        self.__chozas = 0

    @property
    def oro(self):
        with self.lock_oro:
            return self.__oro

    @oro.setter
    def oro(self, value):
        with self.lock_oro:
            self.oro = value

    @property
    def chozas(self):
        with self.lock_chozas:
            return self.__chozas

    @chozas.setter
    def chozas(self, value):
        with self.lock_chozas:
            self.chozas = value

    @property
    def barbaros(self) -> int:
        return int(self.chozas * PONDERADOR_BARBAROS)
