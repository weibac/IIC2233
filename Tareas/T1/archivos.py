import os
from typing import List, Dict


def archivo_a_lista(ruta_ls: tuple) -> List[Dict[str, str]]:
    """
    Implementa lectura dinámica de CSV
    """
    ruta = os.path.join(*ruta_ls)
    with open(ruta, mode='r', encoding='utf-8') as archivo:
        lines = [line.strip('\n').split(',') for line in archivo.readlines()]
    for a in range(len(lines)):
        for b in range(len(lines[0])):
            if ';' in lines[a][b]:
                lines[a][b] = lines[a][b].split(';')
    labels = lines[0]
    lista_instancias = []
    for a in range(1, len(lines)):
        atributos_instancia = {labels[b]: lines[a][b] for b in range(len(labels))}
        lista_instancias.append(atributos_instancia)
    return lista_instancias


def lista_a_dict(lista_instancias: List[Dict[str, str]]) -> Dict[str, Dict[str, str]]:
    dict_instancias = dict()
    for a in range(len(lista_instancias)):
        dict_instancias[lista_instancias[a]['nombre']] = lista_instancias[a]  # TODO: es hardcoding?
    return dict_instancias


def cargar_archivo(ruta_ls: tuple) -> Dict[str, Dict[str, str]]:
    return lista_a_dict(archivo_a_lista(ruta_ls))
