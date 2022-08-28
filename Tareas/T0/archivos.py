# encoding UTF-8 pls
import os


def guardar_partida(partida):
    ruta = os.path.join('partidas', f'{partida.username}.txt')
    with open(ruta, mode='w', encoding='utf-8') as archivo:
        lines = [str(partida.turno)]
        lines.append(';'.join([f'{coord[0]},{coord[1]}' for coord in partida.descubiertas]))
        lines.append(';'.join([','.join(fila) for fila in partida.tablero_real]))
        lines.append(';'.join([','.join(fila) for fila in partida.tablero_visible]))
        for line in lines:
            archivo.writelines(line + '\n')
