from juego import Partida
from tablero import print_tablero
from menus import input_valido, inicio_str, juego_str, perder_str
from archivos import cargar_datos_partida, guardar_partida
import sys


def menu_inicio():
    print(inicio_str)
    inp = input_valido(set(range(0, 4)), 'Tu opción aquí: ', 'int')

    if inp == 1:
        partida = Partida(*nueva_partida())
        while partida.jugando:
            menu_juego(partida)

    elif inp == 2:
        nombre, turno, descubiertas, tablero_real, tablero_visible = cargar_datos_partida()
        if nombre:
            partida = Partida(nombre, len(tablero_real[0]), len(tablero_real))
            partida.turno = turno
            partida.descubiertas = descubiertas
            partida.tablero_real = tablero_real
            partida.tablero_visible = tablero_visible
            while partida.jugando:
                menu_juego(partida)

    elif inp == 0:
        sys.exit()


def nueva_partida():
    print('\nHas seleccionado iniciar una nueva partida')
    nom = input_valido(None, 'Nombre de usuario (alfanumérico): ', 'username')
    x = input_valido(set(range(3, 16)), 'Ancho del tablero (min = 3, max = 15): ', 'int')
    y = input_valido(set(range(3, 16)), 'Largo del tablero (min = 3, max = 15): ', 'int')
    print('')
    return nom, x, y


def menu_juego(partida):
    print_tablero(partida.tablero_visible)  
    print(juego_str.format(partida.turno))
    inp = input_valido(set(range(0, 4)), 'Tu opción aquí: ', 'int')

    if inp == 1:
        coords = input_valido(partida, 'Coordenadas (ej.: B10): ', 'coords')
        result = partida.probar_casilla(coords[0], coords[1])
        if result == 'bestia':
            print(perder_str.format(partida.username, partida.calcular_puntaje()))
            print_tablero(partida.tablero_real)

    elif inp == 2:
        print('Guardando partida...')
        guardar_partida(partida)
        print('Tu partida se ha guardado\n')


menu_inicio()
print('\nGracias por jugar!')
