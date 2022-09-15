from parametros import VIDA_PEKKA, RECUPERACION_VIDA_PEKKA, ORO_INICIAL, \
    PONDERADOR_BARBAROS
from threading import Lock


class CentroUrbano:

    def __init__(self) -> None:
        self.oro = ORO_INICIAL
        self.chozas = 0
        # Completar

    lock_oro = Lock()

    @property
    def oro(self, lock_oro):
        with lock_oro:
            return self.oro

    @oro.setter
    def oro(self, value, lock_oro):
        with lock_oro:
            self.oro = value

    lock_chozas = Lock()

    @property
    def chozas(self, lock_chozas):
        with lock_chozas:
            return self.chozas

    @chozas.setter
    def chozas(self, value, lock_chozas):
        with lock_chozas:
            self.chozas = value

    @property
    def barbaros(self) -> int:
        return int(self.chozas * PONDERADOR_BARBAROS)
