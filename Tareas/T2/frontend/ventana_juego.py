from PyQt5.QtWidgets import QWidget, QLabel, QButtonGroup
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPixmap
from PyQt5 import uic

import parametros as p

window_name, base_class = uic.loadUiType(p.RUTA_UI_VENTANA_JUEGO)

"""
Hacer cuadraditos clickeables en QTDesigner para cada casilla
"""


class VentanaJuego(window_name, base_class):

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
        self.labels_lanzag_hielo = {}
        self.labels_papas = {}
        self.labels_zombies = {}

        # Tienda
        self.botones_tienda = QButtonGroup(self)
        self.botones_tienda.addButton(self.boton_girasol)
        self.botones_tienda.addButton(self.boton_lanzag)
        self.botones_tienda.addButton(self.boton_lanzag_h)
        self.botones_tienda.addButton(self.boton_girasol)
        

        self.quiere_comprar = None

    def mostrar_ventana(self, nombre, escenario):
        # Poner fondo escenario
        if escenario == 'abuela':
            pixeles_fondo_escenario = QPixmap(p.RUTA_FONDO_DIA)
        elif escenario == 'nocturna':
            pixeles_fondo_escenario = QPixmap(p.RUTA_FONDO_NOCHE)
        self.fondo_escenario.setPixmap(pixeles_fondo_escenario)
        self.show()

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
        print(f'zombie {id} movido a {posicion}')
    
    def mousePressEvent(self, event):
        if event.x 
