from PyQt5.QtCore import pyqtSignal
from PyQt5 import uic

import os
import json

path_parametros = os.path.join(os.path.dirname(__file__), os.pardir, 'parametros.json')
with open(path_parametros, 'r') as file:
    p = json.load(file)
window_name, base_class = uic.loadUiType(os.path.join(*p['RUTA_UI_VENTANA_INICIO']))


class VentanaInicio(window_name, base_class):

    senal_enviar_login = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
