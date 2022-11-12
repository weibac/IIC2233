

class LogicaJuego:
    def __init__(self, parent):
        self.parent = parent
        self.jugador_1 = None
        self.jugador_2 = None
        self.nombres = []

    def ejecutar_comando(self, datos):
        comando = datos['comando']

        if comando == 'validar nombre':
            respuesta = self.validar_nombre(datos['nombre'])

        return respuesta

    def validar_nombre(self, nombre):
        motivo = ''
        valido = False
        if not 0 < len(nombre) < 11:
            motivo = 'El nombre debe tener entre 1 y 10 caracteres'
        elif not nombre.isalnum():
            motivo = 'El nombre debe ser alfanumerico'
        elif nombre in self.nombres:
            motivo = 'Ya hay alguien conectado con ese nombre'  
            # TODO: Sacar nombres de desconectados
        if motivo == '':
            valido = True
        respuesta = {'comando': 'validar nombre',
                     'valido': valido,
                     'motivo': motivo}
        return respuesta
