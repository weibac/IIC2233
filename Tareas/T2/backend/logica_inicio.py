from PyQt5.QtCore import QObject, pyqtSignal

import parametros as p


class LogicaInicio(QObject):

    senal_validez_nombre = pyqtSignal(bool, str)
    senal_abrir_seleccion_escenario = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def comprobar_nombre(self, nombre):
        respuesta = ''
        valido = False
        if nombre == '':
            respuesta = 'vacio'
        elif not p.MIN_CARACTERES <= len(nombre) <= p.MAX_CARACTERES:
            respuesta = 'largo'
        elif not nombre.isalnum():
            respuesta = 'alfanum'
        # Si el nombre es valido
        if respuesta == '':
            valido = True
            self.senal_abrir_seleccion_escenario.emit(nombre)
        self.senal_validez_nombre.emit(valido, respuesta)
