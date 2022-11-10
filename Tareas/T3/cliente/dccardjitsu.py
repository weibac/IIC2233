from PyQt5.QtWidgets import QApplication

from front.ventana_inicio import VentanaInicio
from cliente.back.logica import LogicaInicio


class DccCardJitsu(QApplication):
    def __init__(self, argv):
        super().__init__(argv)

        # Instanciar Frontend
        self.ventana_inicio = VentanaInicio()

        # Instanciar Backend
        self.logica_inicio = LogicaInicio()

        # Conectar señales
        self.conectar_inicio()

    def conectar_inicio(self):
        self.ventana_inicio.senal_enviar_nombre.connect(
            self.logica_inicio.enviar_nombre)
        self.logica_inicio.senal_validez_nombre.connect(
            self.ventana_inicio.recibir_respuesta_login)

    def iniciar(self):
        self.ventana_inicio.show()
