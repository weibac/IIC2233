from abc import ABC, abstractmethod
from random import randint
from parametros import AUMENTO_DEFENSA, MAX_AUMENTO_BAYA, MAX_AUMENTO_POCION, MIN_AUMENTO_BAYA, MIN_AUMENTO_POCION


class Objeto(ABC):
    def __init__(self, nombre, tipo) -> None:
        self.nombre = nombre
        self.tipo = tipo

    @abstractmethod
    def aplicar_objeto(self):
        pass

    def __str__(self) -> str:
        return self.nombre


class Baya(Objeto):
    def __init__(self, nombre, tipo) -> None:
        super().__init__(nombre, tipo)

    def aplicar_objeto(self, programon):
        print(f'{programon} come la baya {self} y obtiene muchos nutrientes!')
        programon.vida += randint(MIN_AUMENTO_BAYA, MAX_AUMENTO_BAYA)


class Pocion(Objeto):
    def __init__(self, nombre, tipo) -> None:
        super().__init__(nombre, tipo)

    def aplicar_objeto(self, programon):
        print(f'{programon} se toma la pocion {self} y queda muy contento!')
        programon.ataque += randint(MIN_AUMENTO_POCION, MAX_AUMENTO_POCION)


class Caramelo(Baya, Pocion):
    def __init__(self, nombre, tipo) -> None:
        super().__init__(nombre, tipo)

    def aplicar_objeto(self, programon):
        print(f'{programon} come el caramelo {self}! Es super rico y super nutritivo!')
        super().aplicar_objeto()
        programon.defensa += AUMENTO_DEFENSA
