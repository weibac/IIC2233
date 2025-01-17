from PyQt5.QtCore import QObject, pyqtSignal

import socket
from threading import Thread

from aux_json import encriptar_datos_enviar, desencriptar_datos_recibidos


class Cliente(QObject):
    """
    Esta clase en gran parte copiada de la AF3
    """
    senal_manejar_respuesta = pyqtSignal(dict)
    senal_desconexion_repentina = pyqtSignal()

    def __init__(self, host, port):
        super().__init__()
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conectado = False
        self.iniciar_cliente()

    def iniciar_cliente(self):
        """
        Se encarga de conectar el socket
        """
        try:
            self.socket.connect((self.host, self.port))
            self.conectado = True
            self.comenzar_a_escuchar()

        except ConnectionError as e:
            print(f"\n- Todavía no se ha podido establecer conexión")
            self.socket.close()

    def comenzar_a_escuchar(self):
        """
        Instancia el Thread que escucha los mensajes del servidor
        """
        thread = Thread(target=self.escuchar_servidor, daemon=True)
        thread.start()

    def escuchar_servidor(self):
        """
        Recibe mensajes constantes desde el servidor
        """
        try:
            while self.conectado:
                datos = self.recibir_datos()
                if datos:
                    self.senal_manejar_respuesta.emit(datos)
                    print('senal manejar respuesta enviada')
        except IndexError:
            self.socket.close()
            self.conectado = False
            self.senal_desconexion_repentina.emit()
            print(f'ERROR: Se ha perdido conexión con el servidor')

    def recibir_datos(self):
        largo_mensaje = int.from_bytes(self.socket.recv(4), byteorder='big')
        if largo_mensaje % 32 == 0:
            n_segmentos = largo_mensaje // 32
        else:
            n_segmentos = (largo_mensaje // 32) + 1
        mensaje_recibido = bytearray()
        for i_seg in range(1, n_segmentos + 1):
            segmento = self.socket.recv(36)
            n_segmento = int.from_bytes(segmento[:4], byteorder='little')
            segmento = segmento[4:]
            if i_seg == n_segmentos and largo_mensaje % 32 != 0:
                largo_ultimo_seg = largo_mensaje - ((n_segmentos - 1) * 32)
                segmento = segmento[:largo_ultimo_seg]
            mensaje_recibido.extend(segmento)
        # Desencriptar
        datos = desencriptar_datos_recibidos(mensaje_recibido)
        print(datos)
        return datos

    def enviar_datos(self, datos: dict):
        msg = encriptar_datos_enviar(datos)
        largo_mensaje = len(msg)
        # Enviar el largo del mensaje
        self.socket.sendall(largo_mensaje.to_bytes(4, byteorder='big'))
        if largo_mensaje % 32 == 0:
            n_segmentos = largo_mensaje // 32
        else:
            n_segmentos = (largo_mensaje // 32) + 1
        for i_seg in range(1, n_segmentos + 1):
            segmento = bytearray()
            segmento.extend(i_seg.to_bytes(4, byteorder='little'))
            if i_seg == n_segmentos and largo_mensaje % 32 != 0:
                largo_ultimo_seg = largo_mensaje - ((n_segmentos - 1) * 32)
                for i_byte in range(32):
                    if i_byte + 1 > largo_ultimo_seg:
                        segmento.extend(b'\x00')
                    else:
                        segmento.extend(msg[0].to_bytes(1, byteorder='big'))
                        msg = msg[1:]
            else:
                for i_byte in range(32):
                    segmento.extend(msg[0].to_bytes(1, byteorder='big'))
                    msg = msg[1:]
            self.socket.sendall(segmento)
