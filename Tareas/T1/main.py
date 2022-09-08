from menus import Menu
from archivos import cargar_archivo
from parametros import ANCHO_MENU_ENTRENADOR, ANCHO_MENU_OBJETOS, HEADER_MENU_ENTRENADOR, HEADER_MENU_OBJETOS, OPCIONES_MENU_ENTRENADOR, OPCIONES_MENU_OBJETOS \


def setup():
    menu_entrenador = Menu(HEADER_MENU_ENTRENADOR, ANCHO_MENU_ENTRENADOR, OPCIONES_MENU_ENTRENADOR)
    print(menu_entrenador)
    menu_objetos = Menu(HEADER_MENU_OBJETOS, ANCHO_MENU_OBJETOS, OPCIONES_MENU_OBJETOS)
    print(menu_objetos)

setup()
