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


def encontrar_partidas():
    return [archivo[:-4] for archivo in os.listdir('partidas')]


def cargar_datos_partida(nombre):
    ruta = os.path.join('partidas', f'{nombre}.txt')
    with open(ruta, mode='r', encoding='utf-8') as archivo:
        lines = [line.strip('\n') for line in archivo.readlines()]
        turno = int(lines[0])
        descubiertas = [tuple(fila.split(',')) for fila in lines[1].split(';')]
        tablero_real = leer_tablero_archivo(lines[2])
        tablero_visible = leer_tablero_archivo(lines[3])
    return turno, descubiertas, tablero_real, tablero_visible


def leer_tablero_archivo(tablero_str):  # TODO: LLEVAR A CARGAR_DATOS_PARTIDA
    tablero = [fila.split(',') for fila in tablero_str.split(';')]
    return tablero


def guardar_puntaje(puntaje, victoria, partd):
    data = [str(a) for a in [puntaje, victoria, partd.username, partd.dim_x, partd.dim_y]]
    with open('puntajes.txt', mode='a', encoding='utf-8') as archivo:
        archivo.writelines(','.join(data) + '\n')
