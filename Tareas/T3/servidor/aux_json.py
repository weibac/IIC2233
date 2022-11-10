import json
from os import path

from cripto import encriptar, desencriptar
from codificacion import codificar, decodificar


def dict_json():  # Adaptada de la AF3
    """
    Lee parametros.json y retorna su diccionario correspondiente
    """
    ruta = path.join(path.dirname(__file__), 'parametros.json')
    with open(ruta, "r", encoding="UTF-8") as archivo:
        diccionario_data = json.load(archivo)
    return diccionario_data


def empaquetar_datos_enviar(datos):
    datos_serializados = json.dumps(datos)
    return codificar(encriptar(datos_serializados))


def desempaquetar_datos_recibidos(msg):
    msg_desencriptado = desencriptar(decodificar(msg))
    return json.loads(msg_desencriptado)
