from PyQt5.QtWidgets import QApplication

from time import sleep

from front.ventana_inicio import VentanaInicio
from front.ventana_espera import VentanaEspera
from front.ventana_juego import VentanaJuego
from front.ventana_final import VentanaFinal

from back.cliente import Cliente
from back.logica_ventanas import LogicaVentanas
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
        self.ventana_espera = VentanaEspera()
        self.ventana_juego = VentanaJuego()
        self.ventana_final = VentanaFinal()

        # Instanciar Backend
        self.logica_ventanas = LogicaVentanas()
        self.cliente = Cliente(self.PARAMETROS['HOST'], self.PARAMETROS['PORT'])

        # Conectar señales
        self.conectar_inicio()
        self.conectar_espera()
        self.conectar_desconexion_repentina()

    def conectar_inicio(self):
        # self.ventana_inicio.senal_enviar_nombre.connect(
        #     self.logica_inicio.enviar_nombre)
        self.ventana_inicio.senal_enviar_nombre.connect(
            self.cliente.enviar_datos)
        # self.logica_inicio.senal_validez_nombre.connect(
        #     self.ventana_inicio.recibir_respuesta_login)
        self.cliente.senal_manejar_respuesta.connect(
            self.logica_ventanas.ejecutar_respuesta_servidor)
        self.logica_ventanas.senal_nombre_invalido.connect(
            self.ventana_inicio.recibir_nombre_invalido)
        self.logica_ventanas.senal_nombre_valido.connect(
            self.ventana_inicio.recibir_nombre_valido)
        self.logica_ventanas.senal_nombre_valido.connect(
            self.ventana_espera.iniciar_ventana)

    def conectar_espera(self):
        self.logica_ventanas.senal_iniciar_cuenta.connect(
            self.ventana_espera.iniciar_cuenta)
        self.ventana_espera.senal_usuario_vuelve.connect(
            self.ventana_inicio.show)
        self.ventana_espera.senal_usuario_vuelve.connect(
            self.cliente.enviar_datos)
        self.logica_ventanas.senal_parar_cuenta.connect(
            self.ventana_espera.parar_cuenta)
        self.ventana_espera.senal_cuenta_termino.connect(
            self.cliente.enviar_datos)
        self.logica_ventanas.senal_iniciar_partida.connect(
            self.ventana_espera.recibir_inicio_partida)
        self.logica_ventanas.senal_iniciar_partida.connect(
            self.ventana_juego.iniciar_ventana)

    def conectar_desconexion_repentina(self):
        self.cliente.senal_desconexion_repentina.connect(
            self.ventana_inicio.desconexion_repentina)
        self.cliente.senal_desconexion_repentina.connect(
            self.ventana_espera.desconexion_repentina)
        # TODO: El resto de ventanas
        self.cliente.senal_desconexion_repentina.connect(
            self.terminar)

    def iniciar(self):
        self.ventana_inicio.show()

    def terminar(self):
        sleep(3)
        self.quit()
