from PyQt5.QtWidgets import QApplication
from backend.logica_inicio import LogicaInicio

from frontend.ventana_inicio import VentanaInicio
from frontend.ventana_juego import VentanaJuego
from frontend.ventana_seleccion_escenario import VentanaSeleccionEscenario
from frontend.ventana_test import VentanaTest


class DccCruzVsZombies(QApplication):
    def __init__(self, argv):
        super().__init__(argv)

        # Instanciar Frontend
        self.ventana_test = VentanaTest()
        self.ventana_inicio = VentanaInicio()
        self.ventana_seleccion_escenario = VentanaSeleccionEscenario()
        self.ventana_juego = VentanaJuego()

        # Instanciar Backend
        self.logica_inicio = LogicaInicio()

        # Conectar señales
        self.conectar_inicio()

    def conectar_inicio(self):
        self.ventana_inicio.senal_enviar_login.connect(
            self.logica_inicio.comprobar_nombre)
        self.logica_inicio.senal_validez_nombre.connect(
            self.ventana_inicio.recibir_respuesta_login)
        self.logica_inicio.senal_abrir_seleccion_escenario.connect(
            self.ventana_seleccion_escenario.mostrar_ventana)
        self.ventana_seleccion_escenario.senal_enviar_escenario.connect(
            self.ventana_juego.mostrar_ventana)

    def iniciar(self):
        # self.ventana_test.show()
        self.ventana_inicio.show()
