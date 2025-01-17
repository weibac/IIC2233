from PyQt5.QtWidgets import QApplication

from time import sleep

from front.ventana_inicio import VentanaInicio
from front.ventana_espera import VentanaEspera
from front.ventana_juego import VentanaJuego
from front.ventana_final import VentanaFinal
from front.ventana_chat import VentanaChat

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
        self.ventana_chat = VentanaChat()

        # Instanciar Backend
        self.logica_ventanas = LogicaVentanas()
        self.cliente = Cliente(self.PARAMETROS['HOST'], self.PARAMETROS['PORT'])

        # Conectar señales
        self.conectar_inicio()
        self.conectar_espera()
        self.conectar_juego()
        self.conectar_desconexion_repentina()
        self.conectar_chat()

    def conectar_inicio(self):
        self.ventana_inicio.senal_enviar_nombre.connect(
            self.cliente.enviar_datos)
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

    def conectar_juego(self):
        self.logica_ventanas.senal_ganar.connect(
            self.ventana_juego.terminar)
        self.logica_ventanas.senal_ganar.connect(
            self.ventana_final.iniciar_ventana)
        self.logica_ventanas.senal_perder.connect(
            self.ventana_juego.terminar)
        self.logica_ventanas.senal_perder.connect(
            self.ventana_final.iniciar_ventana)

    def conectar_desconexion_repentina(self):
        self.cliente.senal_desconexion_repentina.connect(
            self.ventana_inicio.desconexion_repentina)
        self.cliente.senal_desconexion_repentina.connect(
            self.ventana_espera.desconexion_repentina)
        self.cliente.senal_desconexion_repentina.connect(
            self.ventana_juego.desconexion_repentina)
        self.cliente.senal_desconexion_repentina.connect(
            self.ventana_final.desconexion_repentina)
        self.cliente.senal_desconexion_repentina.connect(
            self.ventana_chat.desconexion_repentina)
        self.cliente.senal_desconexion_repentina.connect(
            self.terminar)

    def conectar_chat(self):
        self.ventana_juego.senal_abrir_chat.connect(
            self.ventana_chat.iniciar_ventana)
        self.ventana_juego.senal_abrir_chat.connect(
            self.cliente.enviar_datos)
        self.ventana_chat.senal_enviar_mensaje_chat.connect(
            self.cliente.enviar_datos)
        self.logica_ventanas.senal_recibir_mensaje_chat.connect(
            self.ventana_chat.recibir_mensaje)

    def iniciar(self):
        self.ventana_inicio.show()

    def terminar(self):
        sleep(3)
        self.quit()
