from abc import ABC, abstractmethod
from random import randint
from parametros import AUMENTO_DEFENSA, MAX_AUMENTO_BAYA, MAX_AUMENTO_POCION, MIN_AUMENTO_BAYA, MIN_AUMENTO_POCION


class Objeto(ABC):
    def __init__(self, nombre, tipo) -> None:
        self.nombre = nombre
        self.tipo = tipo

    @abstractmethod
    def aplicar(self):
        pass

    def __str__(self) -> str:
        return self.nombre


class Baya(Objeto):
    def __init__(self, nombre, tipo) -> None:
        super().__init__(nombre, tipo)
        self.mensaje = '{} come la baya {} y obtiene muchos nutrientes!'

    def aplicar(self, programon):
        print(self.mensaje.format(programon, self))
        programon.vida += randint(MIN_AUMENTO_BAYA, MAX_AUMENTO_BAYA)


class Pocion(Objeto):
    def __init__(self, nombre, tipo) -> None:
        super().__init__(nombre, tipo)
        self.mensaje = '{} se toma la pocion {} y queda muy contento!'

    def aplicar(self, programon):
        print(self.mensaje.format(programon, self))
        programon.ataque += randint(MIN_AUMENTO_POCION, MAX_AUMENTO_POCION)


class Caramelo(Baya, Pocion):
    def __init__(self, nombre, tipo) -> None:
        super().__init__(nombre, tipo)
        self.mensaje = '{} come el caramelo {}! Es super rico y super nutritivo!'

    def aplicar(self, programon):
        super().aplicar(programon)
        programon.defensa += AUMENTO_DEFENSA
