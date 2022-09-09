from parametros import ANCHO_MENU_ENTRENADOR, ANCHO_MENU_OBJETOS, HEADER_MENU_ENTRENADOR, HEADER_MENU_OBJETOS, OPCIONES_MENU_ENTRENADOR, OPCIONES_MENU_OBJETOS, RUTA_ENTRENADORES, RUTA_EVOLUCIONES, RUTA_OBJETOS, RUTA_PROGRAMONES
from menus import Menu
from liga import LigaProgramon
from archivos import cargar_archivo
from collections import namedtuple


def setup():
    # Cargar archivos a base datos
    entrenadores = cargar_archivo(RUTA_ENTRENADORES)
    programones = cargar_archivo(RUTA_PROGRAMONES)
    evoluciones = cargar_archivo(RUTA_EVOLUCIONES)
    objetos = cargar_archivo(RUTA_OBJETOS)
    DatosTuple = namedtuple('datos_archivos', ['entrens', 'progmnes', 'evols', 'objs'])  # TODO: Tal vez poner los nombres enteros 
    datos = DatosTuple(entrenadores, programones, evoluciones, objetos)

    # Init Liga
    liga = LigaProgramon(datos)

    # Crear menus fijos
    menu_entrenador = Menu(HEADER_MENU_ENTRENADOR, ANCHO_MENU_ENTRENADOR, OPCIONES_MENU_ENTRENADOR)
    menu_objetos = Menu(HEADER_MENU_OBJETOS, ANCHO_MENU_OBJETOS, OPCIONES_MENU_OBJETOS)

    # Testing area
    for nom in datos.progmnes:
        print(datos.progmnes[nom])
    print(liga.entrenadores[2].nombre)
    print(liga.entrenadores[2].programones)
    print(liga.entrenadores[2].programones[-1])
    print(liga.entrenadores[2].programones[0])
    print(liga.entrenadores[2].programones[0].nombre_megaev)
    print(liga.entrenadores[2].objetos)
    print(liga.entrenadores[2].objetos[0])


setup()
