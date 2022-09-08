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
    DatosTuple = namedtuple('datos_archivos', ['entrens', 'progmnes', 'evols', 'objs'])
    datos = DatosTuple(entrenadores, programones, evoluciones, objetos)
    # Agregar megaevolución

    # Crear menus fijos
    menu_entrenador = Menu(HEADER_MENU_ENTRENADOR, ANCHO_MENU_ENTRENADOR, OPCIONES_MENU_ENTRENADOR)
    menu_objetos = Menu(HEADER_MENU_OBJETOS, ANCHO_MENU_OBJETOS, OPCIONES_MENU_OBJETOS)

    # Testing area
    liga = LigaProgramon(datos)
    print(liga.entrenadores[0].nombre)
    print(liga.entrenadores[0].programones)


setup()
