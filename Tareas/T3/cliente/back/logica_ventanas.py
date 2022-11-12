from PyQt5.QtCore import pyqtSignal, QObject


class LogicaVentanas(QObject):

    senal_nombre_invalido = pyqtSignal(dict)

    def __init__(self) -> None:
        super().__init__()

    def ejecutar_respuesta_servidor(self, datos: dict):
        """
        Se encarga de actuar seǵun los comandos recibidos del servidor.
        """
        comando = datos['comando']
        if comando == 'validar nombre':
            if datos['valido']:
                pass  # TODO
            else:
                self.senal_nombre_invalido.emit(datos)
