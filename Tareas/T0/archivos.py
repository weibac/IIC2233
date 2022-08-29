# encoding UTF-8 pls
import os
from menus import input_valido


def guardar_partida(partida):
    ruta = os.path.join('partidas', f'{partida.username}.txt')
    with open(ruta, mode='w', encoding='utf-8') as archivo:
        lines = [str(partida.turno)]
        lines.append(';'.join([f'{coord[0]},{coord[1]}' for coord in partida.descubiertas]))
        lines.append(';'.join([','.join(fila) for fila in partida.tablero_real]))
        lines.append(';'.join([','.join(fila) for fila in partida.tablero_visible]))
        for line in lines:
            archivo.writelines(line + '\n')


def cargar_datos_partida():
    partidas = [archivo[:-4] for archivo in os.listdir('partidas')]
    partidas_dict = {a + 1:partidas[a] for a in range(len(partidas))}
    if partidas == []:
        print('No hay partidas para cargar\n')  # TODO: Quedo feo esto
        return False, False, False, False, False
    else:
        str_partidas_out = ''
        for a in range(len(partidas)):
            str_partidas_out += f'[{a + 1}] {partidas[a]}\n'
        str_partidas_out += '[0] Volver atrás'                  # TODO 
        print(f'Selecciona una de las partidas guardadas:\n{str_partidas_out}')
        inp = input_valido(set(partidas_dict.keys()), 'Tu elección: ', 'int')
        nombre = partidas_dict[inp]

        ruta = os.path.join('partidas', f'{nombre}.txt')
        with open(ruta, mode='r', encoding='utf-8') as archivo:
            lines = [line.strip('\n') for line in archivo.readlines()]
            turno = int(lines[0])
            descubiertas = [tuple(fila.split(',')) for fila in lines[1].split(';')]
            tablero_real = leer_tablero_archivo(lines[2])
            tablero_visible = leer_tablero_archivo(lines[3])
 
        return nombre, turno, descubiertas, tablero_real, tablero_visible


def leer_tablero_archivo(tablero_str):
    tablero = [fila.split(',') for fila in tablero_str.split(';')]
    return tablero
