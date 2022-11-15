from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QLabel
from PyQt5 import uic

import os
from time import sleep

from aux_json import dict_json

# path_parametros = os.path.join(os.path.dirname(__file__), os.pardir,'parametros.json')
# with open(path_parametros,"r') as file:
#     p = json.load(file)

p = dict_json()
window_name, base_class = uic.loadUiType(os.path.join(*p['RUTA_UI_VENTANA_INICIO']))


class VentanaInicio(window_name, base_class):

    senal_enviar_nombre = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label_desconexion_repentina.setHidden(True)
        self.boton_entrar.clicked.connect(self.enviar_nombre)

    def enviar_nombre(self):
        nombre = self.line_edit_nombre.text()
        self.senal_enviar_nombre.emit({"comando": "validar nombre", "nombre": nombre})

    def recibir_nombre_invalido(self, datos: dict):
        self.line_edit_nombre.setText('')
        self.line_edit_nombre.setPlaceholderText(datos['motivo'])

    def recibir_nombre_valido(self, datos: dict):
        self.hide()

    def desconexion_repentina(self):
        self.label_desconexion_repentina.setHidden(False)
        self.label_desconexion_repentina.repaint()
