from PyQt5.QtWidgets import QApplication
from backend.logica_inicio import LogicaInicio
from backend.logica_juego import LogicaJuego

from frontend.ventana_inicio import VentanaInicio
from frontend.ventana_juego import VentanaJuego
from frontend.ventana_seleccion_escenario import VentanaSeleccionEscenario
from frontend.ventana_test import VentanaTest


class DccCruzVsZombies(QApplication):
    def __init__(self, argv):
        super().__init__(argv)

        # Instanciar Frontend
        # self.ventana_test = VentanaTest()
        self.ventana_inicio = VentanaInicio()
        self.ventana_seleccion_escenario = VentanaSeleccionEscenario()
        self.ventana_juego = VentanaJuego()

        # Instanciar Backend
        self.logica_inicio = LogicaInicio()
        self.logica_juego = LogicaJuego()

        # Conectar señales
        self.conectar_inicio()
        self.conectar_juego()

    def conectar_inicio(self):
        self.ventana_inicio.senal_enviar_login.connect(
            self.logica_inicio.comprobar_nombre)
        self.logica_inicio.senal_validez_nombre.connect(
            self.ventana_inicio.recibir_respuesta_login)
        self.logica_inicio.senal_abrir_seleccion_escenario.connect(
            self.ventana_seleccion_escenario.mostrar_ventana)
        self.ventana_seleccion_escenario.senal_iniciar_juego.connect(
            self.logica_juego.iniciar_juego)
        self.ventana_seleccion_escenario.senal_iniciar_juego.connect(
            self.ventana_juego.mostrar_ventana)

    def conectar_juego(self):
        # Señales para crear sprites
        self.logica_juego.senal_crear_sprite_zombie.connect(
            self.ventana_juego.crear_zombie_label)
        # Señales para actualizar sprites
        self.logica_juego.senal_actualizar_sprite_zombie.connect(
            self.ventana_juego.actualizar_zombie_label)

    def iniciar(self):
        # self.ventana_test.show()
        self.ventana_inicio.show()
