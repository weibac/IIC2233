import json
from os import path

from cripto import encriptar, desencriptar


def dict_json():  # Adaptada de la AF3
    """
    Lee parametros.json y retorna su diccionario correspondiente
    """
    ruta = path.join(path.dirname(__file__), 'parametros.json')
    with open(ruta, "r", encoding="UTF-8") as archivo:
        diccionario_data = json.load(archivo)
    return diccionario_data


def encriptar_datos_enviar(datos):
    """
    Serializa y encripta los datos para su envío
    """
    datos_serializados = json.dumps(datos)
    return encriptar(bytearray(datos_serializados.encode('utf-8')))


def desencriptar_datos_recibidos(msg):
    """
    Desencripta y deserializa los datos recibidos
    """
    msg_desencriptado = desencriptar(msg)
    return json.loads(msg_desencriptado.decode('utf-8'))
