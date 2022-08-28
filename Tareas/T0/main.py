from juego import Partida
from tablero import print_tablero
from menus import input_valido, inicio_str, juego_str
import sys


def menu_inicio():
    print(inicio_str)
    inp = input_valido(set(range(0, 4)), 'Tu opción aquí: ', 'int')
    if inp == 1:
        partida = Partida(*nueva_partida())
        while partida.jugando:
            menu_juego(partida)

    elif inp == 0:
        sys.exit('\nGracias por jugar!')


def nueva_partida():
    print('\nHas seleccionado iniciar una nueva partida')
    nom = input_valido(None, 'Nombre de usuario (alfanumérico): ', 'username')
    x = input_valido(set(range(3, 16)), 'Ancho del tablero (min = 3, max = 15): ', 'int')
    y = input_valido(set(range(3, 16)), 'Largo del tablero (min = 3, max = 15): ', 'int')
    print('')
    return nom, x, y


def menu_juego(partida):
    print_tablero(partida.tablero_visible)  
    print(juego_str)
    inp = input_valido(set(range(0, 4)), 'Tu opción aquí: ', 'int')
    if inp == 1:
        coords = input_valido(partida.letras_num, 'Coordenadas (ej.: B10): ', 'coords')
        result = partida.probar_casilla(*partida.interpretar_coords(coords))
        if result == 'bestia':
            print('Oh no! Te ha comido una bestia Nexus!')
            print('Este era el tablero esta ronda:')
            print_tablero(partida.tablero_real)
            print(f'Tu puntaje esta ronda fue de: {partida.calcular_puntaje()}')

menu_inicio()
