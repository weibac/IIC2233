from menus import Menu
from archivos import cargar_archivo
from parametros import ANCHO_MENU_ENTRENADOR, ANCHO_MENU_OBJETOS, HEADER_MENU_ENTRENADOR, HEADER_MENU_OBJETOS, OPCIONES_MENU_ENTRENADOR, OPCIONES_MENU_OBJETOS, RUTA_ENTRENADORES, RUTA_EVOLUCIONES, RUTA_OBJETOS, RUTA_PROGRAMONES \


def setup():
    # Cargar archivos
    entrenadores = cargar_archivo(RUTA_ENTRENADORES)
    programones = cargar_archivo(RUTA_PROGRAMONES)
    evoluciones = cargar_archivo(RUTA_EVOLUCIONES)
    objetos = cargar_archivo(RUTA_OBJETOS)

    print(objetos)
    #Agregar megaevolución

    # Crear menus fijos
    menu_entrenador = Menu(HEADER_MENU_ENTRENADOR, ANCHO_MENU_ENTRENADOR, OPCIONES_MENU_ENTRENADOR)
    menu_objetos = Menu(HEADER_MENU_OBJETOS, ANCHO_MENU_OBJETOS, OPCIONES_MENU_OBJETOS)
    print(menu_entrenador.seleccionar_opcion())


setup()
