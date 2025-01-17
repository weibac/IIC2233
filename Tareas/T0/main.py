from juego import Partida
from tablero import print_tablero
from menus import input_valido, inicio_str, juego_str, end_str, partidas_str, ranking_str, salir_str
from archivos import guardar_partida, encontrar_partidas, cargar_datos_partida
from archivos import guardar_puntaje, cargar_puntajes
from sys import exit


def menu_inicio():
    print(inicio_str)
    inp = input_valido(set(range(0, 4)), 'Tu opción aquí: ', 'int')

    if inp == 1:
        partida = Partida(*nueva_partida())
        jugar(partida)

    elif inp == 2:
        partidas = encontrar_partidas()
        if partidas == []:
            print('No hay partidas para cargar\n')
        else:
            partidas_dict = {a + 1: partidas[a] for a in range(len(partidas))}
            print(partidas_str(partidas))
            inp = input_valido(set(partidas_dict.keys() | {0}), 'Tu elección: ', 'int')
            if inp == 0:
                menu_inicio()
            else:
                nombre = partidas_dict[inp]
                turno, descubiertas, tablero_real, tablero_visible = cargar_datos_partida(nombre)
                partida = Partida(nombre, len(tablero_real[0]), len(tablero_real))
                partida.turno = turno
                partida.descubiertas = descubiertas
                partida.tablero_real = tablero_real
                partida.tablero_visible = tablero_visible
                jugar(partida)

    elif inp == 3:
        puntajes = cargar_puntajes()
        print(ranking_str(puntajes))

    elif inp == 0:
        exit('\nGracias por jugar!')


def nueva_partida():
    print('\nHas seleccionado iniciar una nueva partida')
    nom = input_valido(None, 'Nombre de usuario (alfanumérico máx. 16 caracteres): ', 'username')
    x = input_valido(set(range(3, 16)), 'Ancho del tablero (min = 3, max = 15): ', 'int')
    y = input_valido(set(range(3, 16)), 'Largo del tablero (min = 3, max = 15): ', 'int')
    print('')
    return nom, x, y


def menu_juego(partida):
    print_tablero(partida.tablero_visible)
    print(juego_str.format(partida.turno))
    inp = input_valido(set(range(0, 3)), 'Tu opción aquí: ', 'int')

    if inp == 1:
        coords = input_valido(partida, 'Coordenadas (ej.: B10): ', 'coords')
        print('')
        partida.probar_casilla(coords[0], coords[1])
        partida.turno += 1
        print('')

    elif inp == 2:
        print('Guardando partida...')
        guardar_partida(partida)
        print('Tu partida se ha guardado\n')

    elif inp == 0:
        print(salir_str)
        inp = input_valido(set(range(0, 3)), 'Tu opción aquí: ', 'int')
        if inp == 1:
            guardar_partida(partida)
            print('Tu partida se ha guardado\n')
            menu_inicio()
        elif inp == 2:
            menu_inicio()


def jugar(partida):
    while partida.jugando:
        menu_juego(partida)
    puntaje = partida.calcular_puntaje()
    victoria = partida.sin_bestias <= partida.descubiertas
    guardar_puntaje(puntaje, victoria, partida)
    print(end_str(victoria).format(partida.username, puntaje))
    print_tablero(partida.tablero_real)
    print('\nPartida guardada. Volviendo al menu de inicio...\n')
    menu_inicio()


while True:
    menu_inicio()
