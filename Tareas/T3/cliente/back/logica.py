from PyQt5.QtCore import QObject, pyqtSignal

import socket
from threading import Thread, Lock

from aux_json import empaquetar_datos_enviar, desempaquetar_datos_recibidos


class LogicaInicio(QObject):

    senal_validez_nombre = pyqtSignal(bool, str)
    senal_abrir_sala_espera = pyqtSignal()

    def __init__(self):
        super().__init__()

    def enviar_nombre(self):
        pass

    def recibir_respuesta_nombre(self):
        pass


class Cliente(QObject):
    """
    Esta clase en gran parte copiada de la AF3
    """

    def __init__(self, host, port):
        super().__init__()
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.lock_recibir = Lock()
        self.conectado = False
        self.iniciar_cliente()

    def iniciar_cliente(self):
        """
        Se encarga de conectar el socket
        """
        try:
            self.socket_cliente.connect((self.host, self.port))
            self.conectado = True
            self.comenzar_a_escuchar()

        except ConnectionError as e:
            print(f"\n-ERROR: El servidor no está inicializado. {e}-")
        except ConnectionRefusedError as e:
            print(f"\n-ERROR: No se pudo conectar al servidor.{e}-")

    def comenzar_a_escuchar(self):
        """
        Instancia el Thread que escucha los mensajes del servidor
        """
        thread = Thread(target=self.escuchar_servidor, daemon=True)
        thread.start()

    def escuchar_servidor(self):
        """
        Recibe mensajes constantes desde el servidor y responde.
        """
        while True:
            datos = desempaquetar_datos_recibidos(self.socket.recv(4096))
            with self.lock_recibir:
                self.procesar_datos_recibidos(datos)

    def procesar_mensaje_recibido(self, datos: dict):
        """
        Se encarga de procesar los mensajes del servidor.
        """
        comando = datos['comando']
        if comando == '':


    def enviar_datos(self, datos: dict):
        msg = empaquetar_datos_enviar(datos)
        self.socket.sendall(msg)
