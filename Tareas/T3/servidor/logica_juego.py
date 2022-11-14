from PyQt5.QtCore import pyqtSignal, QObject


class LogicaJuego(QObject):

    senal_hablar_cliente = pyqtSignal(dict)

    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.jugador_1 = {
            'nombre': None,
            'id': None}
        self.jugador_2 = {
            'nombre': None,
            'id': None}
        self.nombres_ocupados = set()
        self.sala_llena = False

    def ejecutar_comando(self, datos):
        comando = datos['comando']

        if comando == 'validar nombre':
            respuesta = self.validar_nombre(datos['nombre'], datos['id'])

        return respuesta

    def validar_nombre(self, nombre, id):
        motivo = ''
        valido = False
        if self.sala_llena:
            motivo = 'Sorry, pero el juego está lleno :('
        elif not 0 < len(nombre) < 11:
            motivo = 'El nombre debe tener entre 1 y 10 caracteres'
        elif not nombre.isalnum():
            motivo = 'El nombre debe ser alfanumerico'
        elif nombre.upper() in self.nombres_ocupados:
            motivo = 'Ya hay alguien conectado con ese nombre'
            # TODO: Sacar nombres de desconectados
        # Si el nombre es valido
        if motivo == '':
            valido = True
            self.incorporar_jugador(nombre, id)
        respuesta = {'comando': 'validar nombre',
                     'valido': valido,
                     'motivo': motivo,
                     'jugador 1': self.jugador_1['nombre'],
                     'jugador 2': self.jugador_2['nombre'],
                     'iniciar cuenta': self.sala_llena}
        return respuesta

    def incorporar_jugador(self, nombre, id):
        self.nombres_ocupados.add(nombre.upper())
        if self.jugador_1['nombre'] is None and self.jugador_2['nombre'] is None:
            self.jugador_1['nombre'] = nombre
            self.jugador_1['id'] = id
        elif self.jugador_1['nombre'] is None:
            self.jugador_1['nombre'] = nombre
            self.jugador_1['id'] = id
            self.sala_llena = True
            avisar_otro_jug_cuenta = {
                'comando': 'iniciar cuenta',
                'id': self.jugador_2['id'],
                'jugador 1': self.jugador_1['nombre'],
                'jugador 2': self.jugador_2['nombre']}
            self.senal_hablar_cliente.emit(avisar_otro_jug_cuenta)
            print('senal hablar cliente emitida')
        elif self.jugador_2['nombre'] is None:
            self.jugador_2['nombre'] = nombre
            self.jugador_2['id'] = id
            self.sala_llena = True
            avisar_otro_jug_cuenta = {
                'comando': 'iniciar cuenta',
                'id': self.jugador_2['id'],
                'jugador 1': self.jugador_1['nombre'],
                'jugador 2': self.jugador_2['nombre']}
            self.senal_hablar_cliente.emit(avisar_otro_jug_cuenta)
            print('senal hablar cliente emitida')
