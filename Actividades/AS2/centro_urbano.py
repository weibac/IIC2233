from parametros import VIDA_PEKKA, RECUPERACION_VIDA_PEKKA, ORO_INICIAL, \
    PONDERADOR_BARBAROS
from threading import Lock


class CentroUrbano:

    def __init__(self) -> None:
        self.oro = ORO_INICIAL
        self.chozas = 0
        # Completar
        self.lock_oro = Lock()
        self.lock_chozas = Lock()

    @property
    def oro(self):
        with self.lock_oro:
            return self.oro

    @oro.setter
    def oro(self, value):
        with self.lock_oro:
            self.oro = value

    @property
    def chozas(self):
        with self.lock_chozas:
            return self.chozas

    @chozas.setter
    def chozas(self, value):
        with self.lock_chozas:
            self.chozas = value

    @property
    def barbaros(self) -> int:
        return int(self.chozas * PONDERADOR_BARBAROS)
