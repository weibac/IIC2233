from PyQt5.QtCore import pyqtSignal
from PyQt5 import uic

import os

from aux_json import dict_json


p = dict_json()
window_name, base_class = uic.loadUiType(os.path.join(*p['RUTA_UI_VENTANA_FINAL']))


class VentanaFinal(window_name, base_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
