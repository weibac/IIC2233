from PyQt5 import uic

import parametros as p

window_name, base_class = uic.loadUiType(p.RUTA_UI_VENTANA_POSRONDA)


class VentanaPosronda(window_name, base_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def mostrar(self):
        self.show()
