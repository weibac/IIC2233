from parametros import HEADER_MENU_ENTRENADOR, HEADER_MENU_INICIO, HEADER_MENU_OBJETOS, OPCIONES_MENU_ENTRENADOR, OPCIONES_MENU_OBJETOS, RUTA_ENTRENADORES, RUTA_EVOLUCIONES, RUTA_OBJETOS, RUTA_PROGRAMONES
from menus import Menu
from liga import LigaProgramon
from archivos import cargar_archivo
from collections import namedtuple


def setup():
    # Cargar archivos a base datos (named tuple)
    entrenadores = cargar_archivo(RUTA_ENTRENADORES)
    programones = cargar_archivo(RUTA_PROGRAMONES)
    evoluciones = cargar_archivo(RUTA_EVOLUCIONES)
    objetos = cargar_archivo(RUTA_OBJETOS)
    DatosTuple = namedtuple('datos_archivos', ['entrens', 'progmnes', 'evols', 'objs'])  # TODO: Tal vez poner los nombres enteros 
    datos = DatosTuple(entrenadores, programones, evoluciones, objetos)

    # Init Liga
    liga = LigaProgramon(datos)

    # Crear menus fijos
    menu_entrenador = Menu(HEADER_MENU_ENTRENADOR, OPCIONES_MENU_ENTRENADOR)
    menu_objetos = Menu(HEADER_MENU_OBJETOS, OPCIONES_MENU_OBJETOS)

    opciones_menu_inicio = []
    for entrenador in liga.entrenadores:
        nombres_programones = [programon.nombre for programon in entrenador.programones]
        opcion = f'{entrenador.nombre}: {", ".join(nombres_programones)}'
        opciones_menu_inicio.append(opcion)
    menu_inicio = Menu(HEADER_MENU_INICIO, opciones_menu_inicio)


    # Testing area
    print(menu_entrenador)
    print(menu_inicio)


setup()
