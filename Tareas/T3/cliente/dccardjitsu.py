from PyQt5.QtWidgets import QApplication

from front.ventana_inicio import VentanaInicio


class DccCardJitsu(QApplication):
    def __init__(self, argv):
        super().__init__(argv)

        # Instanciar Frontend
        self.ventana_inicio = VentanaInicio()

        # Instanciar Backend

        # Conectar señales

    def iniciar(self):
        self.ventana_inicio.show()
