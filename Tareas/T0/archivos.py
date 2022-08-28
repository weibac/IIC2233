# encoding UTF-8 pls
import os


def guardar_partida(partida):
    ruta = os.path.join('partidas', f'{partida.username}.txt')
    with open(ruta, mode='w', encoding='utf-8') as archivo:
        lines = [partida.turno, partida.descubiertas]
        lines.append([fila.join(',') for fila in partida.tablero_real].join(';'))
        lines.append([fila.join(',') for fila in partida.tablero_visible].join(';'))  
        archivo.writelines(lines)