from parametros import MAX_ENERGIA, MIN_ENERGIA
from programones import ProgramonAgua, ProgramonFuego, ProgramonPlanta


class Entrenador:
    def __init__(self, datos, nombre, energia, programones, objetos) -> None:
        self.nombre = nombre
        self.__energia = energia
        self.programones = programones
        self.objetos = objetos
        self.arreglar_init(datos)

    def arreglar_init(self, datos):
        # Energia
        self.__energia = int(self.__energia)
        # Programones
        if type(self.programones) == str:
            self.programones = [self.programones]
        for a in range(len(self.programones)):
            if datos.progmnes[self.programones[a]]['tipo'] == 'fuego':
                self.programones[a] = ProgramonFuego(datos.progmnes[self.programones[a]])
            elif datos.progmnes[self.programones[a]]['tipo'] == 'planta':
                self.programones[a] = ProgramonPlanta(datos.progmnes[self.programones[a]])
            elif datos.progmnes[self.programones[a]]['tipo'] == 'agua':
                self.programones[a] = ProgramonAgua(datos.progmnes[self.programones[a]])
            self.programones[a].cargar_megaev(**datos.evols[self.programones[a].nombre])
        # Objetos
        if type(self.objetos) == str:
            self.objetos = [self.objetos]
        for a in range(len(self.objetos)):
            if datos.objs[self.objetos[a]]['tipo'] == 'fuego':
                self.objetos[a] = ProgramonFuego(datos.objs[self.objetos[a]])
            elif datos.objs[self.objetos[a]]['tipo'] == 'planta':
                self.objetos[a] = ProgramonPlanta(datos.objs[self.objetos[a]])
            elif datos.objs[self.objetos[a]]['tipo'] == 'agua':
                self.objetos[a] = ProgramonAgua(datos.objs[self.objetos[a]])
            self.objetos[a].cargar_megaev(**datos.evols[self.objetos[a].nombre])

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