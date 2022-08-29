from juego import Partida
from tablero import print_tablero
from menus import input_valido, inicio_str, juego_str, end_str, partidas_str, ranking_str
from archivos import guardar_partida, encontrar_partidas, cargar_datos_partida
from archivos import guardar_puntaje, cargar_puntajes
import sys


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
            partidas_dict = {a + 1:partidas[a] for a in range(len(partidas))}
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


def nueva_partida(): # TODO: Tal vez mover a menus.py
    print('\nHas seleccionado iniciar una nueva partida')
    nom = input_valido(None, 'Nombre de usuario (alfanumérico máx. 16 caracteres): ', 'username')
    x = input_valido(set(range(3, 16)), 'Ancho del tablero (min = 3, max = 15): ', 'int')
    y = input_valido(set(range(3, 16)), 'Largo del tablero (min = 3, max = 15): ', 'int')
    print('')
    return nom, x, y


def menu_juego(partida):
    print_tablero(partida.tablero_visible)  
    print(juego_str.format(partida.turno))
    inp = input_valido(set(range(0, 4)), 'Tu opción aquí: ', 'int')

    if inp == 1:
        coords = input_valido(partida, 'Coordenadas (ej.: B10): ', 'coords')  # TODO: 0 para volver
        print('')
        partida.probar_casilla(coords[0], coords[1])

    elif inp == 2:
        print('Guardando partida...')
        guardar_partida(partida)
        print('Tu partida se ha guardado\n')


def jugar(partida):
    while partida.jugando:
        menu_juego(partida)

    # Una vez que acaba el juego TODO: volver a menu inicio (o preguntar si)
    puntaje = partida.calcular_puntaje()
    victoria = len(partida.descubiertas) + partida.bestias >= partida.casillas
    guardar_puntaje(puntaje, victoria, partida)
    print(end_str(victoria).format(partida.username, puntaje))
    print_tablero(partida.tablero_real)


menu_inicio()
print('\nGracias por jugar!')
