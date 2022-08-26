from juego import Partida
from tablero import print_tablero
from menus import input_valido, inicio_str
import sys



def menu_inicio():
    print(inicio_str)
    inp = input_valido(set(range(0, 4)), 'Tu opción aquí: ', 'int')
    if inp == 1:
        partida = Partida(*nueva_partida())
        print_tablero(partida.tablero_real)
        while partida.jugando:
            menu_juego(partida)

    elif inp == 0:
        sys.exit('\nGracias por jugar!')


def nueva_partida():
    print('\nHas seleccionado iniciar una nueva partida')
    nom = input_valido(None, 'Nombre de usuario (alfanumérico): ', 'username')
    x = input_valido(set(range(3, 16)), 'Ancho del tablero (min = 3, max = 15): ', 'int')
    y = input_valido(set(range(3, 16)), 'Largo del tablero (min = 3, max = 15): ', 'int')
    return nom, x, y


def menu_juego(partida):
    print('TODO: Aqui va tablero')
    coords = input_valido(partida.letras_num, 'Coordenadas (ej.: B10): ', 'coords')
    print(coords)

menu_inicio()