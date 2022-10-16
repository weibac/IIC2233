from PyQt5.QtWidgets import QLabel, QHBoxLayout
from PyQt5.QtCore import pyqtSignal
from PyQt5 import uic

import parametros as p

window_name, base_class = uic.loadUiType(p.RUTA_UI_VENTANA_RANKING)


class VentanaRanking(window_name, base_class):

    senal_volver = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.boton_volver.clicked.connect(self.volver)

        with open('puntajes.txt', 'r') as r:
            lines = r.readlines()

        for a in range(len(lines)):
            lines[a] = lines[a].split(',')
            lines[a][1] = int(lines[a][1])

        def por_puntaje(jug):
            return -1 * jug[1]

        lines.sort(key=por_puntaje)
        lines = lines[:5]

        for line in lines:
            nombre = QLabel(self)
            nombre.setText(line[0])
            puntaje = QLabel(self)
            puntaje.setText(f'{line[1]} puntos')
            fila = QHBoxLayout()
            fila.addWidget(nombre)
            fila.addStretch(1)
            fila.addWidget(puntaje)
            self.verticalLayout_2.addLayout(fila)

    def mostrar_ventana(self):
        self.show()

    def volver(self):
        self.senal_volver.emit()
        self.hide()
