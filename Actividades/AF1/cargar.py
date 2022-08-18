from collections import namedtuple
from curses import raw

# --- EXPLICACION --- #
# los datos vienen en este orden el el .csv:
# nombre,categoria,tiempo_preparacion,precio,ingrediente_1,...,ingrediente_n
def cargar_platos(ruta_archivo: str) -> list:
    r = open(ruta_archivo, 'r')
    raw_lines = r.readlines()
    r.close()
    
    Plato = namedtuple('Plato_type', ['nombre', 'categoria', 'tiempo_prep' ,'precio' ,'ingredientes'])

    platos_ls = [line.strip('\n').split(',') for line in raw_lines]
    platos_named_tuple = []
    for line in platos_ls:
        line[2] = int(line[2])
        line[3] = int(line[3])
        line[4] = line[4].split(';')
        platos_named_tuple.append(Plato(*tuple(line))) # * es para unpack arguments
    
    return platos_named_tuple

    



# --- EXPLICACION --- #
# los datos vienen en este orden el el .csv:
# nombre,cantidad
def cargar_ingredientes(ruta_archivo: str) -> dict:
    r = open(ruta_archivo, 'r')
    raw_lines = r.readlines()
    r.close()

    ingredientes_ls = [line.strip('\n').split(',') for line in raw_lines]
    ingredientes_ls = [ingredientes_ls[0], int(ingredientes_ls[1])]
    
    ingredientes_dict = {ingredientes_ls[i][0] : ingredientes_ls[i][1] for i in range len(ingredientes_ls)}

    return ingredientes_dict
