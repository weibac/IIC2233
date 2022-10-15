from PyQt5.QtCore import pyqtSignal
from PyQt5 import uic

import parametros as p

window_name, base_class = uic.loadUiType(p.RUTA_UI_VENTANA_SEL_ESCENARIO)


class VentanaSeleccionEscenario(window_name, base_class):

    senal_iniciar_juego = pyqtSignal(str, str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.conectar_botones()

    def conectar_botones(self):
        self.boton_inicio.clicked.connect(self.enviar_escenario)

    def enviar_escenario(self):
        escenario = ''
        if self.boton_jardin_abuela.isChecked():
            escenario = 'abuela'
        elif self.boton_salida_nocturna.isChecked():
            escenario = 'nocturna'
        self.senal_iniciar_juego.emit(self.nombre, escenario)
        self.hide()

    def mostrar_ventana(self, nombre):
        self.nombre = nombre
        self.show()
