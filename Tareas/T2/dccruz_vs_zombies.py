from PyQt5.QtWidgets import QApplication

from frontend.ventana_test import VentanaTest


class DccCruzVsZombies(QApplication):
    def __init__(self, argv):
        super().__init__(argv)

        # Instanciar Frontend
        self.ventana_test = VentanaTest()

        # Instanciar Backend

        # Conectar señales

    def iniciar(self):
        self.ventana_test.show()
