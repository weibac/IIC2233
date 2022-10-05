from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import uic

import parametros as p

window_name, base_class = uic.loadUiType(p.RUTA_UI_VENTANA_JUEGO)


class VentanaJuego(window_name, base_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def mostrar_ventana(self, nombre, escenario):
        self.nombre = nombre
        # Poner fondo escenario
        if escenario == 'abuela':
            pixeles_fondo_escenario = QPixmap(p.RUTA_FONDO_DIA)
        elif escenario == 'nocturna':
            pixeles_fondo_escenario = QPixmap(p.RUTA_FONDO_NOCHE)
        self.fondo_escenario.setPixmap(pixeles_fondo_escenario)
        self.show()
