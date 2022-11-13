from PyQt5.QtCore import QObject, pyqtSignal
import socket
from threading import Thread, Lock

from aux_json import encriptar_datos_enviar, desencriptar_datos_recibidos


class Cliente(QObject):
    """
    Esta clase en gran parte copiada de la AF3
    """
    senal_manejar_respuesta = pyqtSignal(dict)

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
        except ConnectionError as error:
            print(f'ERROR: Se ha perdido conexión con el servidor')
            # TODO: Reemplazar por algo con las ventanas

    # def recibir_datos(self):
    #     largo_mensaje = int.from_bytes(self.socket.recv(4), byteorder='big')
    #     mensaje_recibido = bytearray()
    #     # Recibir hasta el penúltimo segmento
    #     for _ in range(max(largo_mensaje // 32, 1)):
    #         segmento = self.socket.recv(36)
    #         n_segmento = int.from_bytes(segmento[:4], byteorder='little')
    #         print(f'recibido segmento n°{n_segmento}')
    #         mensaje_recibido.extend(segmento[4:])
    #     # Recibir el último segmento
    #     segmento = self.socket.recv(36)
    #     n_segmento = int.from_bytes(segmento[:4], byteorder='little')
    #     largo_ultimo_seg = n_segmento * 32 - largo_mensaje
    #     print(f'recibido segmento n°{n_segmento}. Es el último.')
    #     mensaje_recibido.extend(segmento[4:4 + largo_ultimo_seg])
    #     # Desencriptar
    #     datos = desencriptar_datos_recibidos(mensaje_recibido)
    #     # Enviarle los datos a logica_ventanasd
    #     self.senal_manejar_respuesta.emit(datos)

    def recibir_datos(self):
        largo_mensaje = int.from_bytes(self.socket.recv(4), byteorder='big')
        print(f'largo mensaje: {largo_mensaje}')
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
                print(f'recibido segmento n°{n_segmento}. Era el ultimo')
            else:
                print(f'recibido segmento n°{n_segmento}')
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
            print(f'largo: {len(segmento)} contenido:{segmento}')
            self.socket.sendall(segmento)

    # def enviar_datos(self, datos: dict):
    #     msg = encriptar_datos_enviar(datos)
    #     # Enviar el largo del mensaje
    #     self.socket.sendall(len(msg).to_bytes(4, byteorder='big'))
    #     # Separar por segmentos y enviarlos
    #     i_seg = 1
    #     segmento_actual = bytearray(i_seg.to_bytes(4, byteorder='little'))
    #     for i in range(1, (((len(msg) // 32) + 1) * 32) + 1):
    #         try:
    #             segmento_actual.extend(msg[i - 1].to_bytes(1, byteorder='big'))
    #         except IndexError:
    #             segmento_actual.extend(b'\x00')
    #         if i % 32 == 0:
    #             self.socket.sendall(segmento_actual)
    #             i_seg += 1
    #             segmento_actual = bytearray(i_seg.to_bytes(4, byteorder='little'))
