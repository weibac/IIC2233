from PyQt5.QtCore import pyqtSignal, QTimer
from PyQt5 import uic

import os
from time import sleep

from aux_json import dict_json

p = dict_json()
window_name, base_class = uic.loadUiType(os.path.join(*p['RUTA_UI_VENTANA_ESPERA']))


class VentanaEspera(window_name, base_class):

    senal_usuario_vuelve = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.boton_volver.clicked.connect(self.volver)
        #  Timer actualizar cuenta regresiva
        self.tiempo_restante = p['CUENTA_REGRESIVA_INICIO']
        self.timer_cuenta = QTimer()
        self.timer_cuenta.setInterval(1000)
        self.timer_cuenta.timeout.connect(self.cuenta_regresiva)

    def volver(self):
        datos = {
            'comando': 'salir sala espera'
        }
        self.senal_usuario_vuelve.emit(datos)
        self.hide()

    def iniciar_ventana(self, datos: dict):
        self.show()
        if datos['iniciar cuenta']:
            self.iniciar_cuenta(datos)
        else:
            if datos['jugador 1'] is not None:
                self.label_jug_1.setText(datos['jugador 1'])
            if datos['jugador 2'] is not None:
                self.label_jug_2.setText(datos['jugador 2'])

    def iniciar_cuenta(self, datos):
        if datos['jugador 1'] is not None:
            self.label_jug_1.setText(datos['jugador 1'])
        if datos['jugador 2'] is not None:
            self.label_jug_2.setText(datos['jugador 2'])
        self.tiempo_restante = p['CUENTA_REGRESIVA_INICIO']
        self.timer_cuenta.start()

    def cuenta_regresiva(self):
        if self.tiempo_restante > 0:
            sleep(1)
            self.tiempo_restante -= 1
            self.label_timer.setText(str(self.tiempo_restante))
