from PyQt5.QtCore import pyqtSignal
from PyQt5 import uic

import os
from aux_json import dict_json

p = dict_json()
window_name, base_class = uic.loadUiType(os.path.join(*p['RUTA_UI_VENTANA_ESPERA']))


class VentanaEspera(window_name, base_class):

    senal_usuario_vuelve = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.boton_volver.clicked.connect(self.volver)

    def volver(self):
        datos = {
            'comando': 'salir sala espera'
        }
        self.senal_usuario_vuelve.emit(datos)
        self.hide()

    def iniciar_ventana(self, datos: dict):
        self.show()
