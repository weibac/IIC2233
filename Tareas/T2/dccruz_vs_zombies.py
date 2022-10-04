from PyQt5.QtWidgets import QApplication

from frontend.ventana_juego import VentanaJuego
from frontend.ventana_test import VentanaTest


class DccCruzVsZombies(QApplication):
    def __init__(self, argv):
        super().__init__(argv)

        # Instanciar Frontend
        self.ventana_test = VentanaTest()
        self.ventana_juego = VentanaJuego()

        # Instanciar Backend

        # Conectar señales

    def iniciar(self):
        # self.ventana_test.show()
        self.ventana_juego.show()
