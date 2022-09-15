from parametros import AUMENTAR_ATAQUE_FUEGO, AUMENTAR_VELOCIDAD_AGUA, AUMENTAR_VIDA_PLANTA, MAX_ATAQUE, MAX_AUMENTO_ENTRENAMIENTO, MAX_AUMENTO_EXPERIENCIA, MAX_DEFENSA, MAX_EXPERIENCIA, MAX_NIVEL, MAX_VELOCIDAD, MAX_VIDA, MEGA_ATAQUE, MEGA_DEFENSA, MEGA_VELOCIDAD, MEGA_VIDA, MIN_ATAQUE, MIN_AUMENTO_ENTRENAMIENTO, MIN_AUMENTO_EXPERIENCIA, MIN_DEFENSA, MIN_NIVEL, MIN_VELOCIDAD, MIN_VIDA, ORDEN_VENTAJAS, PONDERACIONES_LUCHA
from random import randint, choice
from abc import ABC, abstractmethod


class Programon(ABC):
    def __init__(self, nombre, tipo, nivel, vida, ataque, defensa, velocidad) -> None:
        self.nombre = nombre
        self.tipo = tipo
        self.ventajas = ORDEN_VENTAJAS
        self.__experiencia = 0
        self.__nivel = int(nivel)
        self.nivel_megaev = None
        self.nombre_megaev = None
        self.__vida = int(vida)
        self.__ataque = int(ataque)
        self.__defensa = int(defensa)
        self.__velocidad = int(velocidad)

    def cargar_megaev(self, nombre, nivel, evolucion) -> None:
        self.nivel_megaev = int(nivel)
        self.nombre_megaev = evolucion

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
            print(f'{self.nombre} sube de nivel al nivel {self.nivel}!')
            self.vida += randint(MIN_AUMENTO_ENTRENAMIENTO, MAX_AUMENTO_ENTRENAMIENTO)
            self.ataque += randint(MIN_AUMENTO_ENTRENAMIENTO, MAX_AUMENTO_ENTRENAMIENTO)
            self.defensa += randint(MIN_AUMENTO_ENTRENAMIENTO, MAX_AUMENTO_ENTRENAMIENTO)
            self.velocidad += randint(MIN_AUMENTO_ENTRENAMIENTO, MAX_AUMENTO_ENTRENAMIENTO)
            # Megaevolución
            if self.__nivel >= self.nivel_megaev:
                print(f'{self.nombre} megaevoluciona! Ahora se llama: {self.nombre_megaev}')
                self.nombre = self.nombre_megaev
                self.vida += MEGA_VIDA
                self.ataque += MEGA_ATAQUE
                self.defensa += MEGA_DEFENSA
                self.velocidad += MEGA_VELOCIDAD

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
            vida_antigua = self.__vida
            self.__vida = value
            print(f'Aumento vida: {self.__vida - vida_antigua}')
            print(f'La vida subió de {vida_antigua} a {self.__vida}')

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
            ataque_antiguo = self.__ataque
            self.__ataque = value
            print(f'Aumento ataque: {self.__ataque - ataque_antiguo}')
            print(f'El ataque subió de {ataque_antiguo} a {self.__ataque}')

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
            defensa_antigua = self.__defensa
            self.__defensa = value
            print(f'Aumento defensa: {self.__defensa - defensa_antigua}')
            print(f'La defensa subió de {defensa_antigua} a {self.__defensa}')

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
            velocidad_antigua = self.__velocidad
            self.__velocidad = value
            print(f'Aumento velocidad: {self.__velocidad - velocidad_antigua}')
            print(f'La velocidad subió de {velocidad_antigua} a {self.__velocidad}')

    def entrenamiento(self) -> None:
        aumento_exp = randint(MIN_AUMENTO_EXPERIENCIA, MAX_AUMENTO_EXPERIENCIA)
        print(f'{self.nombre} entrenó duro y ganó {aumento_exp} de experiencia')
        self.experiencia += aumento_exp

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

    def luchar(self, oponente) -> bool:
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
            print(f'{self} gana!')
            self.accion_victoria()
        else:
            print(f'{oponente} gana!')
            oponente.accion_victoria()
        return gana_self

    @abstractmethod
    def accion_victoria(self):
        pass

    def __str__(self) -> str:
        return self.nombre


class ProgramonFuego(Programon):
    def __init__(self, kwargs) -> None:
        super().__init__(**kwargs)

    def accion_victoria(self) -> None:
        self.ataque += AUMENTAR_ATAQUE_FUEGO


class ProgramonPlanta(Programon):
    def __init__(self, kwargs) -> None:
        super().__init__(**kwargs)

    def accion_victoria(self) -> None:
        self.vida += AUMENTAR_VIDA_PLANTA


class ProgramonAgua(Programon):
    def __init__(self, kwargs) -> None:
        super().__init__(**kwargs)

    def accion_victoria(self) -> None:
        self.velocidad += AUMENTAR_VELOCIDAD_AGUA
