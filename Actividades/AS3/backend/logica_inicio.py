from PyQt5.QtCore import QObject, pyqtSignal

import parametros as p


class LogicaInicio(QObject):

    senal_respuesta_validacion = pyqtSignal(bool, set)
    senal_abrir_juego = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def comprobar_usuario(self, usuario, contrasena):
        # COMPLETAR
        set_respuesta = set()
        valido = False
        if not usuario.isalnum():
            set_respuesta.add('usuario')
        if contrasena in p.CONTRASENAS_PROHIBIDAS:
            set_respuesta.add('contraseña')
        if set_respuesta == set():
            valido = True
            self.senal_abrir_juego.emit(usuario)
        self.senal_respuesta_validacion.emit(valido, set_respuesta)
