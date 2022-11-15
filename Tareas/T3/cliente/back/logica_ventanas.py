from PyQt5.QtCore import pyqtSignal, QObject


class LogicaVentanas(QObject):

    senal_nombre_invalido = pyqtSignal(dict)
    senal_nombre_valido = pyqtSignal(dict)

    senal_iniciar_cuenta = pyqtSignal(dict)
    senal_parar_cuenta = pyqtSignal(dict)
    senal_iniciar_partida = pyqtSignal(dict)

    senal_ganar = pyqtSignal(dict)
    senal_perder = pyqtSignal(dict)

    senal_recibir_mensaje_chat = pyqtSignal(dict)

    def __init__(self) -> None:
        super().__init__()
        self.nombre = None

    def ejecutar_respuesta_servidor(self, datos: dict):
        """
        Se encarga de actuar según los comandos recibidos del servidor.
        """
        comando = datos['comando']
        if comando == 'validar nombre':
            if datos['valido']:
                self.senal_nombre_valido.emit(datos)
            else:
                print(f"nombre invalido. motivo: {datos['motivo']}")
                self.senal_nombre_invalido.emit(datos)
        elif comando == 'iniciar cuenta':
            self.senal_iniciar_cuenta.emit(datos)
        elif comando == 'el otro cliente se fue':
            self.senal_parar_cuenta.emit(datos)
        elif comando == 'iniciar partida':
            self.senal_iniciar_partida.emit(datos)
        elif comando == 'ganar':
            self.senal_ganar.emit(datos)
        elif comando == 'perder':
            self.senal_perder.emit(datos)
        elif comando == 'recibir mensaje chat':
            self.senal_recibir_mensaje_chat.emit(datos)
