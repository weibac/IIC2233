from PyQt5.QtCore import pyqtSignal
from PyQt5 import uic

import os

from aux_json import dict_json


p = dict_json()
window_name, base_class = uic.loadUiType(os.path.join(*p['RUTA_UI_VENTANA_JUEGO']))


class VentanaJuego(window_name, base_class):

    senal_abrir_chat = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label_desconexion_repentina.setHidden(True)
        self.boton_chat.clicked.connect(self.abrir_chat)

    def iniciar_ventana(self, datos):
        # TODO
        self.show()

    def abrir_chat(self):
        datos = {'comando': 'abrio chat'}
        self.senal_abrir_chat.emit(datos)

    def terminar(self, datos):
        self.hide()

    def desconexion_repentina(self):
        self.label_desconexion_repentina.setHidden(False)
        self.label_desconexion_repentina.repaint()
