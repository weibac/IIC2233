from PyQt5.QtCore import pyqtSignal
from PyQt5 import uic

import parametros as p

window_name, base_class = uic.loadUiType(p.RUTA_UI_VENTANA_INICIO)


class VentanaInicio(window_name, base_class):

    senal_enviar_login = pyqtSignal(str)
    senal_abrir_ranking = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.conectar_botones()

    def conectar_botones(self):
        self.boton_jugar.clicked.connect(self.enviar_login)
        self.boton_ranking.clicked.connect(self.abrir_ranking)
        # self.boton_salir.clicked.connedt()

    def enviar_login(self):
        nombre = self.line_edit_username.text()
        self.senal_enviar_login.emit(nombre)
    
    def abrir_ranking(self):
        self.senal_abrir_ranking.emit()
        self.hide()

    def recibir_respuesta_login(self, valido, error):
        if valido:
            self.hide()
        elif error == 'vacio':
            self.line_edit_username.setText('')
            self.line_edit_username.setPlaceholderText('introduce un nombre')
        elif error == 'largo':
            self.line_edit_username.setText('')
            msg_error = '{} a {} caracteres por favor'
            msg_error = msg_error.format(p.MIN_CARACTERES, p.MAX_CARACTERES)
            self.line_edit_username.setPlaceholderText(msg_error)
        elif error == 'alfanum':
            self.line_edit_username.setText('')
            msg_error = 'el nombre puede contener solo letras y numeros'
            self.line_edit_username.setPlaceholderText(msg_error)
