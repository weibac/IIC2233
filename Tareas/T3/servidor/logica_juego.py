

class LogicaJuego:
    def __init__(self, parent):
        self.parent = parent
        self.jugador_1 = None
        self.jugador_2 = None
        self.nombres_ocupados = set()
        self.sala_llena = False

    def ejecutar_comando(self, datos):
        comando = datos['comando']

        if comando == 'validar nombre':
            respuesta = self.validar_nombre(datos['nombre'])

        return respuesta

    def validar_nombre(self, nombre):
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
            self.incorporar_jugador(nombre)
        respuesta = {'comando': 'validar nombre',
                     'valido': valido,
                     'motivo': motivo}
        return respuesta

    def incorporar_jugador(self, nombre):
        self.nombres_ocupados.add(nombre.upper())
        if self.jugador_1 is None and self.jugador_2 is None:
            self.jugador_1 = nombre
        elif self.jugador_1 is None:
            self.jugador_1 = nombre
            self.sala_llena = True
            self.cuenta_regresiva_inicio()
        elif self.jugador_2 is None:
            self.jugador_2 = nombre
            self.sala_llena = True
            self.cuenta_regresiva_inicio()
        
    def cuenta_regresiva_inicio(self):
        pass

