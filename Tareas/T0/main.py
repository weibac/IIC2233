from juego import Partida
from tablero import print_tablero
import sys
import menus


def menu_inicio():
    print(menus.inicio_str)
    inp = menus.input_valido(set(range(0, 4)), 'Tu opción aquí: ')
    if inp == 1:
        game = Partida(nueva_partida())
        print_tablero(game.tablero_real)
    
    elif inp == 0:
        sys.exit('\nGracias por jugar!')


def nueva_partida():
    print('\nHas seleccionado iniciar una nueva partida')
    x = menus.input_valido(set(range(3, 16)), 'Ancho del tablero (min = 3, max = 15): ')
    y = menus.input_valido(set(range(3, 16)), 'Largo del tablero (min = 3, max = 15): ')
    return (x, y)

menu_inicio()