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
    opciones_menu_inicio = []  # TODO: tal vez cargar desde datos en vez de liga
    for entrenador in liga.entrenadores:
        nombres_programones = [programon.nombre for programon in entrenador.programones]
        opcion = f'{entrenador.nombre}: {", ".join(nombres_programones)}'
        opciones_menu_inicio.append(opcion)
    menu_inicio = Menu(HEADER_MENU_INICIO, opciones_menu_inicio)

    menu_entrenador = Menu(HEADER_MENU_ENTRENADOR, OPCIONES_MENU_ENTRENADOR)
    menu_objetos = Menu(HEADER_MENU_OBJETOS, OPCIONES_MENU_OBJETOS)
    MenusTuple = namedtuple('menus', ['inicio', 'entrenador', 'objeto'])
    menus = MenusTuple(menu_inicio, menu_entrenador, menu_objetos)

    return liga, menus


def menu_objetos(menu_objetos, liga):
    opcion = menu_objetos.seleccionar_opcion()
    if opcion == 1:
        pass
    elif opcion == 2:
        pass
    elif opcion == 3:
        pass
    elif opcion == 4:
        pass
    elif opcion == 5:
        pass


def menu_entrenador(menus, liga, indice_jugador):
    accion = menus.entrenador.seleccionar_opcion()
    if accion == 1:
        pass
    elif accion == 2:
        liga.simular_ronda()
    elif accion == 3:
        liga.resumen_campeonato()
    elif accion == 4:
        menu_objetos(menus.objeto, liga)
    elif accion == 5:
        pass
        opciones_menu_objeto = []
        bayas = []
        pociones = []
        caramelos = []
        for objeto in liga.entrenadores[indice_jugador].objetos:
            if objeto.tipo == 'baya':
                bayas.append(objeto)
            elif objeto.tipo == 'pocion':
                pociones.append(objeto)
            elif objeto.tipo == 'caramelo':
                caramelos.append(objeto)
        [lista for lista in [bayas, pociones, caramelos] if len(lista) > 0]
        if len(bayas) > 0:
            opciones_menu_objeto.append()
    elif accion == 6:
        liga.entrenadores[indice_jugador].estado_entrenador()
    elif accion == 7:
        pass
    elif accion == 8:
        pass


def main():
    liga, menus = setup()
    print('\nBienvenid@ al DCCampeonato Programon!\n')
    indice_jugador = menus.inicio.seleccionar_opcion() - 1
    print(f'Has seleccionado a: {liga.entrenadores[indice_jugador].nombre}')
    menu_entrenador(menus, liga, indice_jugador)


if __name__ == '__main__':
    main()
