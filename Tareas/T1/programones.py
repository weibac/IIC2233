from parametros import AUMENTAR_ATAQUE_FUEGO, AUMENTAR_VELOCIDAD_AGUA, AUMENTAR_VIDA_PLANTA, MAX_ATAQUE, MAX_AUMENTO_ENTRENAMIENTO, MAX_AUMENTO_EXPERIENCIA, MAX_DEFENSA, MAX_EXPERIENCIA, MAX_NIVEL, MAX_VELOCIDAD, MAX_VIDA, MIN_ATAQUE, MIN_AUMENTO_ENTRENAMIENTO, MIN_AUMENTO_EXPERIENCIA, MIN_DEFENSA, MIN_NIVEL, MIN_VELOCIDAD, MIN_VIDA, PONDERACIONES_LUCHA
from random import randint, choice
from abc import ABC, abstractmethod


class Programon(ABC):
    def __init__(self, **kwargs) -> None:
        self.nombre = nombre
        self.tipo = tipo
        self.ventajas = ['fuego', 'planta', 'agua']
        self.__experiencia = 0
        self.__nivel = nivel
        self.nivel_megaev = nivel_megaev
        self.__vida = vida
        self.__ataque = ataque
        self.__defensa = defensa
        self.__velocidad = velocidad
    
    @property
    def experiencia(self):
        return self.__experiencia
    
    @experiencia.setter
    def experiencia(self, value):
        if value >= MAX_EXPERIENCIA:
            self.__experiencia = value - MAX_EXPERIENCIA
            self.nivel += 1
        else:
            self.__experiencia = value

    @property
    def nivel(self):
        return self.__nivel

    @nivel.setter
    def nivel(self, value):
        if value > MAX_NIVEL:
            self.__nivel = MAX_NIVEL
        elif value < MIN_NIVEL:
            self.__nivel = MIN_NIVEL
        else:
            self.__nivel = value
            self.vida += randint(MIN_AUMENTO_ENTRENAMIENTO, MAX_AUMENTO_ENTRENAMIENTO)
            self.ataque += randint(MIN_AUMENTO_ENTRENAMIENTO, MAX_AUMENTO_ENTRENAMIENTO)
            self.defensa += randint(MIN_AUMENTO_ENTRENAMIENTO, MAX_AUMENTO_ENTRENAMIENTO)
            self.velocidad += randint(MIN_AUMENTO_ENTRENAMIENTO, MAX_AUMENTO_ENTRENAMIENTO)
            print(f'{self.nombre} sube de nivel!')  # TODO: tal vez hay que poner + info

    @property
    def vida(self):
        return self.__vida

    @vida.setter
    def vida(self, value):
        if value > MAX_VIDA:
            self.__vida = MAX_VIDA
        elif value < MIN_VIDA:
            self.__vida = MIN_VIDA
        else:
            self.__vida = value

    @property
    def ataque(self):
        return self.__ataque

    @ataque.setter
    def ataque(self, value):
        if value > MAX_ATAQUE:
            self.__ataque = MAX_ATAQUE
        elif value < MIN_ATAQUE:
            self.__ataque = MIN_ATAQUE
        else:
            self.__ataque = value

    @property
    def defensa(self):
        return self.__defensa

    @defensa.setter
    def defensa(self, value):
        if value > MAX_DEFENSA:
            self.__defensa = MAX_DEFENSA
        elif value < MIN_DEFENSA:
            self.__defensa = MIN_DEFENSA
        else:
            self.__defensa = value

    @property
    def velocidad(self):
        return self.__velocidad

    @velocidad.setter
    def velocidad(self, value):
        if value > MAX_VELOCIDAD:
            self.__velocidad = MAX_VELOCIDAD
        elif value < MIN_VELOCIDAD:
            self.__velocidad = MIN_VELOCIDAD
        else:
            self.__velocidad = value

    def entrenamiento(self) -> None:
        # TODO: tal vez print
        self.experiencia += randint(MIN_AUMENTO_EXPERIENCIA, MAX_AUMENTO_EXPERIENCIA)

    def ventaja_tipo(self, oponente) -> int:
        if self.tipo == oponente.tipo:
            ventaja = 0
        else:
            posicion_self = self.ventajas.index(self.tipo)
            posicion_oponente = self.ventajas.index(oponente.tipo)
            if (posicion_self + 1) % 3 == posicion_oponente % 3:
                ventaja = 1
            else:
                ventaja = -1
        return ventaja

    def puntaje_lucha(self, oponente) -> int:
        ventaja = self.ventaja_tipo(oponente)
        parametros = (self.vida, self.nivel, self.ataque, self.defensa, self.velocidad, ventaja)
        puntaje = sum(parametros[a] * PONDERACIONES_LUCHA[a] for a in range(len(parametros)))
        return puntaje


    #  TODO: PREGUNTAR COMO ESTRUCTURAR ESTO
    def luchar(self, oponente):
        gana_self = None
        puntaje_self = self.puntaje_lucha(oponente)
        puntaje_oponente = oponente.puntaje_lucha(self)
        if puntaje_self > puntaje_oponente:
            gana_self = True
        elif puntaje_self < puntaje_oponente:
            gana_self = False
        else:
            gana_self = choice(True, False)
        if gana_self:
            self.accion_victoria()
        else:
            oponente.accion_victoria()

    @abstractmethod
    def accion_victoria(self):
        pass


class ProgramonFuego(Programon):
    def __init__(self, **kwargs) -> None:
        super().__init__()

    def accion_victoria(self) -> None:
        self.ataque += AUMENTAR_ATAQUE_FUEGO


class ProgramonPlanta(Programon):
    def __init__(self, **kwargs) -> None:
        super().__init__()

    def accion_victoria(self) -> None:
        self.vida += AUMENTAR_VIDA_PLANTA


class ProgramonAgua(Programon):
    def __init__(self, **kwargs) -> None:
        super().__init__()

    def accion_victoria(self) -> None:
        self.velocidad += AUMENTAR_VELOCIDAD_AGUA
