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
        # Boton volver
        self.label_boton.mousePressEvent = self.volver
        self.label_desconexion_repentina.setHidden(True)

    def iniciar_ventana(self, datos):
        comando = datos['comando']
        if comando == 'ganar':
            self.label_mensaje.setText('Felicidades! Ganaste!')
        elif comando == 'perder':
            self.label_mensaje.setText('Pucha, perdiste :(')
        self.show()

    def volver(self, arg):
        datos = {'comando': 'salir sala espera'}
        self.senal_usuario_vuelve.emit(datos)
        self.hide()

    def desconexion_repentina(self):
        self.label_desconexion_repentina.setHidden(False)
        self.label_desconexion_repentina.repaint()
