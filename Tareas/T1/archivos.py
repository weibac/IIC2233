import os
from typing import List


def cargar_archivo(ruta_ls: list) -> List[dict]:
    """
    Implementa lectura dinámica de CSV
    """
    lista_instancias = []
    ruta = os.path.join(*ruta_ls)
    with open(ruta, mode='r', encoding='utf-8') as archivo:
        lines = [line.strip('\n').split(',') for line in archivo.readlines()] # TODO: tal vez deindent linea abajo
    for a in range(len(lines)):
        for b in range(len(lines[0])):
            if ';' in lines[a][b]:
                lines[a][b] = lines[a][b].split(';')
    labels = lines[0]
    for a in range(1, len(lines)):
        atributos_instancia = {labels[b]: lines[a][b] for b in range(len(labels))}
        lista_instancias.append(atributos_instancia)
    return lista_instancias
