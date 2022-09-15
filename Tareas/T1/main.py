from parametros import ENERGIA_ENTRENAMIENTO, HEADER_MENU_ENTRENADOR, HEADER_MENU_INICIO, HEADER_MENU_OBJETOS, HEADER_MENU_PROGRAMONES, HEADER_MENU_USAR_OBJ, OPCIONES_MENU_BASE, OPCIONES_MENU_ENTRENADOR, OPCIONES_MENU_OBJETOS, RUTA_ENTRENADORES, RUTA_EVOLUCIONES, RUTA_OBJETOS, RUTA_PROGRAMONES
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

    # Init liga
    liga = LigaProgramon(datos)

    # Crear menus fijos independientes de entrenador jugador
    opciones_menu_inicio = []  # TODO: tal vez cargar desde datos en vez de liga
    for entrenador in liga.entrenadores:
        nombres_programones = [programon.nombre for programon in entrenador.programones]
        opcion = f'{entrenador.nombre}: {", ".join(nombres_programones)}'
        opciones_menu_inicio.append(opcion)
    menu_inicio = Menu(HEADER_MENU_INICIO, opciones_menu_inicio)

    menu_entrenador = Menu(HEADER_MENU_ENTRENADOR, OPCIONES_MENU_ENTRENADOR)
    menu_objetos = Menu(HEADER_MENU_OBJETOS, OPCIONES_MENU_OBJETOS)

    # Jugador selecciona su entrenador
    indice_jugador = menu_inicio.seleccionar_opcion() - 1
    print(f'Has seleccionado a: {liga.entrenadores[indice_jugador].nombre}')

    # Crear menu fijo dependiente de entrenador jugador
    opciones_menu_programones = []
    for programon in liga.entrenadores[indice_jugador].programones:
        opciones_menu_programones.append(programon.nombre)
    opciones_menu_programones += OPCIONES_MENU_BASE
    menu_programones = Menu(HEADER_MENU_PROGRAMONES, opciones_menu_programones)

    # Empaquetar menus
    MenusTuple = namedtuple('menus', ['inicio', 'entrenador', 'programones', 'objetos'])
    menus = MenusTuple(menu_inicio, menu_entrenador, menu_programones, menu_objetos)

    return liga, menus, indice_jugador


def menu_entrenar(menu_programones, liga, ind_jug):
    if liga.entrenadores[ind_jug].energia < ENERGIA_ENTRENAMIENTO:  # TODO: segun wsp si no hay suficiente energ se gasta igual
        print(f'Entrenar a un programon cuesta {ENERGIA_ENTRENAMIENTO}\
 de energia pero solo tienes {liga.entrenadores[ind_jug].energia}')
    else:
        liga.entrenadores[ind_jug].energia -= ENERGIA_ENTRENAMIENTO
        indice_programon = menu_programones.seleccionar_opcion() - 1
        liga.entrenadores[ind_jug].programones[indice_programon].entrenamiento()


def menu_objetos(menu_objetos, liga, indice_jugador):
    opcion = menu_objetos.seleccionar_opcion()
    if opcion == 1:
        liga.entrenadores[indice_jugador].crear_objeto('baya')
    elif opcion == 2:
        liga.entrenadores[indice_jugador].crear_objeto('pocion')
    elif opcion == 3:
        liga.entrenadores[indice_jugador].crear_objeto('caramelo')
    elif opcion == 4:
        pass
    elif opcion == 5:
        pass


def menu_usar_obj(menu_programones, liga, ind_jug):
    opciones_menu_usar_obj = []
    for objeto in liga.entrenadores[ind_jug].objetos:
        opciones_menu_usar_obj.append(objeto.nombre.capitalize())
    opciones_menu_usar_obj += OPCIONES_MENU_BASE
    menu_usar_obj = Menu(HEADER_MENU_USAR_OBJ, opciones_menu_usar_obj)

    ind_obj = menu_usar_obj.seleccionar_opcion() - 1
    ind_prog = menu_programones.seleccionar_opcion() - 1
    objeto_select = liga.entrenadores[ind_jug].objetos[ind_obj]
    objeto_select.aplicar(liga.entrenadores[ind_jug].programones[ind_prog])


def menu_entrenador(menus, liga, ind_jug):
    accion = menus.entrenador.seleccionar_opcion()
    if accion == 1:
        menu_entrenar(menus.programones, liga, ind_jug)
    elif accion == 2:
        liga.simular_ronda()  # TODO
    elif accion == 3:
        liga.resumen_campeonato()  # TODO
    elif accion == 4:
        menu_objetos(menus.objetos, liga, ind_jug)
    elif accion == 5:
        menu_usar_obj(menus.programones, liga, ind_jug)
    elif accion == 6:
        liga.entrenadores[ind_jug].estado_entrenador()  # TODO
    elif accion == 7:
        pass
    elif accion == 8:
        pass


def main():
    print('\nBienvenid@ al DCCampeonato Programon!\n')
    liga, menus, indice_jugador = setup()
    # Idea para el flujo: menu_entrenador función recursiva con caso base hay un campeón y lo retorna
    menu_entrenador(menus, liga, indice_jugador)


if __name__ == '__main__':
    main()
