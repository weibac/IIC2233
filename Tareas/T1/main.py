from parametros import ENERGIA_ENTRENAMIENTO, HEADER_MENU_ENTRENADOR, HEADER_MENU_FIN_PARTIDA, HEADER_MENU_INICIO, HEADER_MENU_OBJETOS, HEADER_MENU_PROGRAMONES, HEADER_MENU_USAR_OBJ, OPCIONES_MENU_BASE, OPCIONES_MENU_ENTRENADOR, OPCIONES_MENU_FIN_PARTIDA, OPCIONES_MENU_OBJETOS, RUTA_ENTRENADORES, RUTA_EVOLUCIONES, RUTA_OBJETOS, RUTA_PROGRAMONES
from menus import Menu
from liga import LigaProgramon
from archivos import cargar_archivo
from collections import namedtuple
from sys import exit


def main():
    datos = cargar_datos()
    print('\nBienvenid@ al DCCampeonato Programon!\n')
    liga = LigaProgramon(datos)
    while liga.ronda_actual < 4:
        # TODO: La liga se reinicia cada vez que se llega al menu incio
        # liga = LigaProgramon(datos)
        menus = menus_fijos(liga)
        menu_inicio(menus, liga)


def menu_inicio(menus, liga):
    # Jugador selecciona su entrenador
    opcion = menus[0].seleccionar_opcion()
    if opcion == len(menus[0].opciones):
        salir()
    else:
        indice_jugador = opcion - 1
        print(f'Has seleccionado a: {liga.entrenadores[indice_jugador].nombre}\n')

    # Crear y empaquetar menu fijo dependiente de entrenador jugador (menu_programones)
    opciones_menu_programones = []
    for programon in liga.entrenadores[indice_jugador].programones:
        opciones_menu_programones.append(programon.nombre)
    opciones_menu_programones += OPCIONES_MENU_BASE
    menu_programones = Menu(HEADER_MENU_PROGRAMONES, opciones_menu_programones)

    # Re-Empaquetar menus
    MenusTuple = namedtuple('menus', ['inicio', 'fin', 'entrenador', 'objetos', 'programones'])
    menus = MenusTuple(*menus, menu_programones)

    # Flujo
    menu_entrenador(menus, liga, indice_jugador)


def menu_entrenador(menus, liga, indice_jugador):
    accion = None
    while accion != 7:
        accion = menus.entrenador.seleccionar_opcion()
        if accion == 1:
            menu_entrenar(menus.programones, liga, indice_jugador)
        elif accion == 2:
            menu_simular_ronda(menus, liga, indice_jugador)
        elif accion == 3:
            liga.resumen_campeonato()
        elif accion == 4:
            menu_objetos(menus.objetos, liga, indice_jugador)
        elif accion == 5:
            menu_usar_obj(menus.programones, liga, indice_jugador)
        elif accion == 6:
            liga.entrenadores[indice_jugador].estado_entrenador()
        elif accion == 7:
            pass
        elif accion == 8:
            salir()


def menus_fijos(liga):
    # Crear menus fijos independientes de entrenador jugador
    opciones_menu_inicio = []  # TODO: tal vez cargar desde datos en vez de liga
    for entrenador in liga.entrenadores:
        nombres_programones = [programon.nombre for programon in entrenador.programones]
        opcion = f'{entrenador.nombre}: {", ".join(nombres_programones)}'
        opciones_menu_inicio.append(opcion)
    opciones_menu_inicio.append('Salir')
    menu_inicio = Menu(HEADER_MENU_INICIO, opciones_menu_inicio)
    menu_fin = Menu(HEADER_MENU_FIN_PARTIDA, OPCIONES_MENU_FIN_PARTIDA)
    menu_entrenador = Menu(HEADER_MENU_ENTRENADOR, OPCIONES_MENU_ENTRENADOR)
    menu_objetos = Menu(HEADER_MENU_OBJETOS, OPCIONES_MENU_OBJETOS)

    # Empaquetar menus
    menus = (menu_inicio, menu_fin, menu_entrenador, menu_objetos)
    return menus


def cargar_datos():
    # Cargar archivos a base datos (named tuple)
    entrenadores = cargar_archivo(RUTA_ENTRENADORES)
    programones = cargar_archivo(RUTA_PROGRAMONES)
    evoluciones = cargar_archivo(RUTA_EVOLUCIONES)
    objetos = cargar_archivo(RUTA_OBJETOS)
    DatosTuple = namedtuple('datos_archivos', ['entrens', 'progmnes', 'evols', 'objs'])  # TODO: Tal vez poner los nombres enteros
    datos = DatosTuple(entrenadores, programones, evoluciones, objetos)
    return datos


def menu_usar_obj(menu_programones, liga, ind_jug):
    # Construir menu lista objetos
    opciones_menu_usar_obj = []
    for objeto in liga.entrenadores[ind_jug].objetos:
        opciones_menu_usar_obj.append(objeto.nombre.capitalize())
    opciones_menu_usar_obj += OPCIONES_MENU_BASE
    menu_usar_obj = Menu(HEADER_MENU_USAR_OBJ, opciones_menu_usar_obj)
    # Usuario selecciona un objeto, volver o salir
    opcion = revisar_volver_salir(menu_usar_obj)
    if opcion == 'volver':
        pass
    else:
        ind_obj = opcion - 2
        menu_sel_prog_obj(menu_programones, liga, ind_jug, ind_obj)


def menu_sel_prog_obj(menu_programones, liga, ind_jug, ind_obj): # TODO: Volver solo un paso atrás
    opcion = revisar_volver_salir(menu_programones)
    if opcion == 'volver':
        pass
    else:
        # Usar objeto
        ind_prog = opcion
        objeto_seleccionado = liga.entrenadores[ind_jug].objetos[ind_obj]
        objeto_seleccionado.aplicar(liga.entrenadores[ind_jug].programones[ind_prog])
        liga.entrenadores[ind_jug].objetos.remove(objeto_seleccionado)
        print('')


def menu_objetos(menu_objetos, liga, indice_jugador):
    opcion = menu_objetos.seleccionar_opcion()
    print('')
    if opcion == 1:
        liga.entrenadores[indice_jugador].crear_objeto('baya')
    elif opcion == 2:
        liga.entrenadores[indice_jugador].crear_objeto('pocion')
    elif opcion == 3:
        liga.entrenadores[indice_jugador].crear_objeto('caramelo')
    elif opcion == 4:
        pass
    elif opcion == 5:
        salir()


def menu_simular_ronda(menus, liga, indice_jugador):
    opcion = revisar_volver_salir(menus.programones)
    if opcion == 'volver':
        pass
    else:
        indice_programon = opcion
        usuario_perdio = liga.simular_ronda(indice_jugador, indice_programon)
        if usuario_perdio:
            print(f'Oh no! {liga.entrenadores[indice_jugador].nombre}, te han derrotado!\n')
            menu_fin(menus.fin)
        else:
            print(f'{liga.entrenadores[indice_jugador].nombre}, has superado esta ronda! :D\n')


def menu_entrenar(menu_programones, liga, ind_jug):
    if liga.entrenadores[ind_jug].energia < ENERGIA_ENTRENAMIENTO:  # TODO: segun wsp si no hay suficiente energ se gasta igual
        print(f'Entrenar a un programon cuesta {ENERGIA_ENTRENAMIENTO}\
 de energia pero solo tienes {liga.entrenadores[ind_jug].energia}')
    else:
        opcion = revisar_volver_salir(menu_programones)
        if opcion == 'volver':
            pass
        else:
            indice_programon = opcion
            liga.entrenadores[ind_jug].programones[indice_programon].entrenamiento()
            liga.entrenadores[ind_jug].energia -= ENERGIA_ENTRENAMIENTO
            print('')


def revisar_volver_salir(menu):
    opcion = menu.seleccionar_opcion() - 1
    if opcion == len(menu.opciones) - 2:
        return 'volver'
    elif opcion == len(menu.opciones) - 1:
        salir()
    else:
        return opcion


def menu_fin(menu_fin):
    accion = menu_fin.seleccionar_opcion()
    if accion == 2:
        salir()


def salir():  # TODO: Preguntar si segur@ salir
    exit('Gracias por jugar!')




if __name__ == '__main__':
    main()
