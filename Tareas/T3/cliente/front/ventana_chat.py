from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QLabel, QVBoxLayout
from PyQt5 import uic

import os

from aux_json import dict_json


p = dict_json()
window_name, base_class = uic.loadUiType(os.path.join(*p['RUTA_UI_VENTANA_CHAT']))


class VentanaChat(window_name, base_class):

    senal_enviar_mensaje_chat = pyqtSignal(dict)
    i_msg = 0

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label_desconexion_repentina.setHidden(True)
        self.boton_enviar.clicked.connect(self.enviar_mensaje)
        self.v_layout_msgs = QVBoxLayout()
        self.scroll_contents_widget.setLayout(self.v_layout_msgs)
        self.labels_msg = {}

    def iniciar_ventana(self, datos):
        for label in self.labels_msg.values():
            self.v_layout_msgs.addWidget(label)
        # self.scroll_contents_widget.repaint()
        self.show()

    def enviar_mensaje(self):
        msg = self.line_edit.text()
        datos = {
            'comando': 'enviar mensaje chat',
            'msg': msg}
        self.senal_enviar_mensaje_chat.emit(datos)

    def recibir_mensaje(self, datos):
        msg = f"{datos['enviante']}: {datos['msg']}"
        self.labels_msg[self.i_msg] = QLabel(msg, self)
        self.v_layout_msgs.addWidget(self.labels_msg[self.i_msg])
        self.scroll_contents_widget.repaint()
        self.i_msg += 1

    def terminar(self, datos):
        self.hide()

    def desconexion_repentina(self):
        self.label_desconexion_repentina.setHidden(False)
        self.label_desconexion_repentina.repaint()
