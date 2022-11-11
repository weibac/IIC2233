from PyQt5.QtWidgets import QApplication
from front.ventana_inicio import VentanaInicio
from cliente.back.cliente import LogicaInicio, Cliente
from aux_json import dict_json


class DccCardJitsu(QApplication):
    """
    Clase encargada de instanciar backend y frontend; y conectar señales.
    """
    def __init__(self, argv):
        super().__init__(argv)
        self.PARAMETROS = dict_json()

        # Instanciar Frontend
        self.ventana_inicio = VentanaInicio()

        # Instanciar Backend
        self.logica_inicio = LogicaInicio()
        self.cliente = Cliente(self.PARAMETROS['HOST'], self.PARAMETROS['PORT'])

        # Conectar señales
        self.conectar_inicio()

    def conectar_inicio(self):
        # self.ventana_inicio.senal_enviar_nombre.connect(
        #     self.logica_inicio.enviar_nombre)
        self.ventana_inicio.senal_enviar_nombre.connect(
            self.cliente.enviar_datos)
        self.logica_inicio.senal_validez_nombre.connect(
            self.ventana_inicio.recibir_respuesta_login)

    def iniciar(self):
        self.ventana_inicio.show()
