from parametros import MAX_ENERGIA, MIN_ENERGIA


class Entrenador:
    def __init__(self, nombre, energia, programones, objetos) -> None:
        self.nombre = nombre
        self.__energia = energia
        self.programones = programones
        self.objetos = objetos

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