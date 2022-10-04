from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QPixmap
import parametros as p


class VentanaTest(QWidget):

    def __init__(self):
        super().__init__()
        # Aspecto
        self.setGeometry(30, 30, p.ANCHO_PANTALLA, p.ALTO_PANTALLA)
        self.setWindowTitle('DCCruz vs zombies alpha')

        self.crear_elementos()

    def crear_elementos(self):
        # Fondo
        self.fondo = QLabel()
        pixeles_fondo = QPixmap(p.RUTA_FONDO_DIA)
        self.fondo.setPixmap(pixeles_fondo)

        vbox_test = QVBoxLayout()
        vbox_test.addWidget(self.fondo)
        self.setLayout(vbox_test)
