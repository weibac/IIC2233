from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout


class VentanaTest(QWidget):

    def __init__(self):
        super().__init__()
        # Aspecto
        self.setGeometry(300, 300, 900, 600)
        self.setWindowTitle('DCCruz vs zombies alpha')

        self.crear_elementos()

    def crear_elementos(self):
        self.mensaje = QLabel('hola', self)
        vbox_test = QVBoxLayout()
        vbox_test.addStretch(1)
        vbox_test.addWidget(self.mensaje)
        vbox_test.addStretch(1)
        self.setLayout(vbox_test)
