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
    return [archivo[:-4] for archivo in os.listdir('partidas') if archivo != '.gitignore']


def cargar_datos_partida(nombre):
    ruta = os.path.join('partidas', f'{nombre}.txt')
    with open(ruta, mode='r', encoding='utf-8') as archivo:
        lines = [line.strip('\n') for line in archivo.readlines()]
        turno = int(lines[0])
        descubiertas = [tuple(fila.split(',')) for fila in lines[1].split(';')]
        tablero_real = [fila.split(',') for fila in lines[2].split(';')]
        tablero_visible = [fila.split(',') for fila in lines[3].split(';')]
    return turno, descubiertas, tablero_real, tablero_visible


def guardar_puntaje(puntaje, victoria, partd):
    data = [puntaje, partd.username, victoria, partd.turno, partd.dim_x, partd.dim_y]
    data = [str(a) for a in data]
    with open('puntajes.txt', mode='a', encoding='utf-8') as archivo:
        archivo.writelines(','.join(data) + '\n')


def cargar_puntajes():
    with open('puntajes.txt', mode='r', encoding='utf-8') as archivo:
        data = [line.strip('\n').split(',') for line in archivo.readlines()]
        return data