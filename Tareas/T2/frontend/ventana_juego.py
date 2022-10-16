from PyQt5.QtWidgets import QWidget, QLabel, QButtonGroup
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QPixmap
from PyQt5 import uic

import parametros as p

window_name, base_class = uic.loadUiType(p.RUTA_UI_VENTANA_JUEGO)

"""
Hacer cuadraditos clickeables en QTDesigner para cada casilla
"""


class VentanaJuego(window_name, base_class):

    senal_quiere_planta = pyqtSignal(str, int, int)

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Dicts assets sprites
        self.assets_girasoles = {item[0]: QPixmap(item[1]) for item in p.SPRITES_GIRASOL.items()}
        self.assets_lanzag = {item[0]: QPixmap(item[1]) for item in p.SPRITES_LANZAG.items()}
        self.assets_lanzag_h = {item[0]: QPixmap(item[1]) for item in p.SPRITES_LANZAG_H.items()}
        self.assets_papas = {item[0]: QPixmap(item[1]) for item in p.SPRITES_PAPA.items()}
        self.assets_zombies = {item[0]: QPixmap(item[1]) for item in p.SPRITES_ZOMBIES.items()}

        # Dicts labels
        self.labels_girasoles = {}
        self.labels_lanzag = {}
        self.labels_lanzag_h = {}
        self.labels_papas = {}
        self.labels_zombies = {}

        # Tienda
        self.botones_tienda = QButtonGroup(self)
        self.botones_tienda.addButton(self.boton_girasol)
        self.botones_tienda.addButton(self.boton_lanzag)
        self.botones_tienda.addButton(self.boton_lanzag_h)
        self.botones_tienda.addButton(self.boton_girasol)

        self.quiere_planta = None

    def mostrar_ventana(self, nombre, escenario):
        # Poner fondo escenario
        if escenario == 'abuela':
            pixeles_fondo_escenario = QPixmap(p.RUTA_FONDO_DIA)
        elif escenario == 'nocturna':
            pixeles_fondo_escenario = QPixmap(p.RUTA_FONDO_NOCHE)
        self.fondo_escenario.setPixmap(pixeles_fondo_escenario)
        self.show()

    def crear_planta_label(self, planta, id, x_casilla, y_casilla):
        p_label = QLabel(self)
        p_label.setGeometry((246 + x_casilla * 42), (157 + y_casilla * 75),
                            p.ANCHO_PLANTA, p.ALTO_PLANTA)
        p_label.setScaledContents(True)
        p_label.setVisible(True)
        if planta == 'girasol':
            p_label.setPixmap(self.assets_girasoles[1])
            self.labels_girasoles[id] = p_label
        elif planta == 'lanzag':
            p_label.setPixmap(self.assets_lanzag[1])
            self.labels_lanzag[id] = p_label
        elif planta == 'lanzag_h':
            p_label.setPixmap(self.assets_lanzag_h[1])
            self.labels_lanzag_h[id] = p_label
        elif planta == 'papa':
            p_label.setPixmap(self.assets_papa[1])
            self.labels_papa[id] = p_label

    def crear_zombie_label(self, id: int, apariencia: tuple, posicion: tuple):
        z_label = QLabel(self)
        z_label.setGeometry(*posicion, p.ANCHO_ZOMBIE, p.ALTO_ZOMBIE)
        z_label.setPixmap(self.assets_zombies[apariencia])
        z_label.setScaledContents(True)
        z_label.setVisible(True)
        self.labels_zombies[id] = z_label

    def actualizar_zombie_label(self, id: int, apariencia: tuple, posicion: tuple):
        self.labels_zombies[id].setPixmap(self.assets_zombies[apariencia])
        self.labels_zombies[id].move(*posicion)

    def mousePressEvent(self, event):
        if 246 <= event.x() <= 246 + 420 and 157 <= event.y() <= 157 + 125 \
                and event.button() == Qt.LeftButton:
            if self.boton_girasol.isChecked():
                quiere_planta = 'girasol'
            elif self.boton_lanzag.isChecked():
                quiere_planta = 'lanzag'
            elif self.boton_lanzag_h.isChecked():
                quiere_planta = 'lanzag_h'
            elif self.boton_papa.isChecked():
                quiere_planta = 'papa'
            x_casilla = (event.x() - 246) // 42
            y_casilla = (event.y() - 157) // 75
            self.senal_quiere_planta.emit(quiere_planta, x_casilla, y_casilla)
