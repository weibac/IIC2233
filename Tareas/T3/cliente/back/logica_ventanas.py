from PyQt5.QtCore import pyqtSignal, QObject


class LogicaVentanas(QObject):

    senal_nombre_invalido = pyqtSignal(dict)
    senal_nombre_valido = pyqtSignal(dict)

    senal_iniciar_cuenta = pyqtSignal(dict)

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
            print('Logica ventanas recibio datos con iniciar cuenta')
            self.senal_iniciar_cuenta.emit(datos)
