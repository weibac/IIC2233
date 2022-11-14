import socket
import threading
from sys import exit

from aux_json import encriptar_datos_enviar, desencriptar_datos_recibidos
from logica_juego import LogicaJuego


class Servidor:
    """
    Esta clase en gran parte copiada de los apuntes de la semana 9, tercer jupyter notebook.
    El resto en su mayoría fue copiado de la AF3.
    """
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sockets = {}
        self.logica_juego = LogicaJuego(self)
        self.id_cliente = 0
        print('-' * 80)
        self.bind_and_listen()
        self.accept_connections()

    def bind_and_listen(self):
        """
        Enlaza el socket creado con el host y puerto indicado.

        Primero, se enlaza el socket y luego queda esperando
        por conexiones entrantes.
        """
        self.socket_servidor.bind((self.host, self.port))
        self.socket_servidor.listen()
        self.log(f"Servidor escuchando en {self.host}:{self.port}...")

    def accept_connections(self):
        """
        Inicia el thread que aceptará clientes.
        """
        thread = threading.Thread(target=self.accept_connections_thread, daemon=True)
        thread.start()

    def accept_connections_thread(self):
        """
        Es arrancado como thread para aceptar clientes.

        Cada vez que aceptamos un nuevo cliente, iniciamos un
        thread nuevo encargado de manejar el socket para ese cliente.
        """
        self.log("Servidor aceptando conexiones...")

        try:
            client_socket, direccion = self.socket_servidor.accept()
            self.log(f'Usuario con cliente de direccion {direccion} ha sido aceptad@')
            listening_client_thread = threading.Thread(
                target=self.listen_client_thread,
                args=(self.id_cliente, client_socket),
                daemon=True)
            listening_client_thread.start()
            self.sockets[self.id_cliente] = client_socket
            self.id_cliente += 1
        except ConnectionError as error:
            self.log(f'Se ha producido un error de conexión: {error}')

    def listen_client_thread(self, id_cliente, client_socket):
        """
        Es ejecutado como thread que escuchará a un cliente en particular.
        Llama a recibir_datos para recibir los datos, y luego llama a logica_juego.ejecutar_comando
        para para obtener la respuesta del servidor. Luego la envía.
        """
        self.log(f"Empezando a escuchar al cliente de id {id_cliente}...")
        try:
            datos = self.recibir_datos(client_socket)
            if not datos:
                raise ConnectionResetError
            # Responder según los datos
            respuesta = self.logica_juego.ejecutar_comando(datos)
            print(respuesta)
            if respuesta:
                self.enviar_datos(respuesta, client_socket)
        except ConnectionError as error:
            self.log(f'Ocurrió un error de conexión con el cliente: {error}')
            # TODO desconexión repentina

    # def recibir_datos(self, client_socket):
    #     largo_mensaje = int.from_bytes(client_socket.recv(4), byteorder='big')
    #     print(f'largo mensaje: {largo_mensaje}')
    #     mensaje_recibido = bytearray()
    #     # Recibir hasta el penúltimo segmento
    #     for _ in range(max(largo_mensaje // 32, 1)):
    #         segmento = client_socket.recv(36)  # TODO: Aparentemente recibe más veces de las que debería.
    #         n_segmento = int.from_bytes(segmento[:4], byteorder='little')
    #         print(f'recibido segmento n°{n_segmento}')
    #         mensaje_recibido.extend(segmento[4:])
    #     # Recibir el último segmento
    #     segmento = client_socket.recv(36)
    #     n_segmento = int.from_bytes(segmento[:4], byteorder='little')
    #     largo_ultimo_seg = n_segmento * 32 - largo_mensaje
    #     print(f'recibido segmento n°{n_segmento}. Es el último.')
    #     mensaje_recibido.extend(segmento[4:4 + largo_ultimo_seg])
    #     # Desencriptar
    #     datos = desencriptar_datos_recibidos(mensaje_recibido)
    #     print(datos)
    #     return datos

    def recibir_datos(self, client_socket):
        """
        Recibe los datos implementando el sistema de codificación especificado en el enunciado.
        Llama a desencriptar_datos_recibidos del módulo aux_json.
        """
        largo_mensaje = int.from_bytes(client_socket.recv(4), byteorder='big')
        if largo_mensaje % 32 == 0:
            n_segmentos = largo_mensaje // 32
        else:
            n_segmentos = (largo_mensaje // 32) + 1
        mensaje_recibido = bytearray()
        for i_seg in range(1, n_segmentos + 1):
            segmento = client_socket.recv(36)
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

    def enviar_datos(self, datos: dict, client_socket):
        """
        Recibe los datos de respuesta implementando
        el sistema de codificación especificado en el enunciado.
        Llama a encriptar_datos_enviar del módulo aux_json.
        """
        msg = encriptar_datos_enviar(datos)
        largo_mensaje = len(msg)
        # Enviar el largo del mensaje
        client_socket.sendall(largo_mensaje.to_bytes(4, byteorder='big'))
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
            client_socket.sendall(segmento)

    # def enviar_datos(self, datos: dict, client_socket):
    #     msg = encriptar_datos_enviar(datos)
    #     # Enviar el largo del mensaje
    #     client_socket.sendall(len(msg).to_bytes(4, byteorder='big'))
    #     # Separar por segmentos y enviarlos
    #     i_seg = 1
    #     segmento_actual = bytearray(i_seg.to_bytes(4, byteorder='little'))
    #     for i in range(1, (((len(msg) // 32) + 1) * 32) + 1):
    #         try:
    #             segmento_actual.extend(msg[i - 1].to_bytes(1, byteorder='big'))
    #         except IndexError:
    #             segmento_actual.extend(b'\x00')
    #         if i % 32 == 0:
    #             client_socket.sendall(segmento_actual)
    #             i_seg += 1
    #             segmento_actual = bytearray(i_seg.to_bytes(4, byteorder='little'))

    def log(self, texto: str):
        print(f'| {texto: ^76s} |')
        print('-' * 80)
