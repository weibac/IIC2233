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
        self.terminaron_de_contar = 0
        self.jugando = False

    def ejecutar_comando(self, datos: dict):
        comando = datos['comando']

        if comando == 'validar nombre':
            respuesta = self.validar_nombre(datos['nombre'], datos['id'])
        elif comando == 'salir sala espera':
            respuesta = self.respuesta_usuario_sale(datos)
        elif comando == 'cuenta termino':
            respuesta = self.cuenta_termino(datos)

        if 'log_yn' not in respuesta.keys():
            respuesta['log_yn'] = False

        return respuesta

    def validar_nombre(self, nombre, id_cliente):
        motivo = ''
        valido = False
        if self.sala_llena:
            motivo = 'Sorry, pero el juego está lleno :('
            self.parent.log(f'cliente id {id_cliente}', 'quiere entrar s espera',
                            'no entra (estaba llena)')
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
            self.incorporar_jugador(nombre, id_cliente)
            self.parent.log(f'cliente id {id_cliente}', 'quiere entrar s espera',
                            'y entra (no estaba llena)')
        respuesta = {'comando': 'validar nombre',
                     'valido': valido,
                     'motivo': motivo,
                     'jugador 1': self.jugador_1['nombre'],
                     'jugador 2': self.jugador_2['nombre'],
                     'iniciar cuenta': self.sala_llena,
                     'log_yn': True,
                     'log_msg': [f'cliente id {id_cliente}',
                                 f'ingresa nombre {nombre}', f'valido? {valido}']}
        if self.sala_llena:
            respuesta['log_yn'] = False
        return respuesta

    def respuesta_usuario_sale(self, datos):
        """
        Maneja los casos donde un usuario apreta el botón volver en la sala de espera.
        """
        # Esto (respuesta) se envia de vuelta al cliente que se fue
        respuesta = datos
        # Y esto otro (datos cambiado) al otro cliente
        if respuesta['id'] == self.jugador_1['id']:
            self.nombres_ocupados.remove(self.jugador_1['nombre'])
            self.jugador_1 = {
                'nombre': None,
                'id': None}
            datos['id'] = self.jugador_2['id']
            datos['comando'] = 'el otro cliente se fue'
            datos['quien se fue'] = 'jugador 1'
        elif respuesta['id'] == self.jugador_2['id']:
            self.nombres_ocupados.remove(self.jugador_2['nombre'])
            self.jugador_2 = {
                'nombre': None,
                'id': None}
            datos['id'] = self.jugador_1['id']
            datos['comando'] = 'el otro cliente se fue'
            datos['quien se fue'] = 'jugador 2'
        self.parent.pre_enviar_datos(datos)
        return respuesta

    def incorporar_jugador(self, nombre, id_cliente):
        self.nombres_ocupados.add(nombre.upper())
        if self.jugador_1['nombre'] is None and self.jugador_2['nombre'] is None:
            self.jugador_1['nombre'] = nombre
            self.jugador_1['id'] = id_cliente
        elif self.jugador_1['nombre'] is None:
            self.jugador_1['nombre'] = nombre
            self.jugador_1['id'] = id_cliente
            self.sala_llena = True
            avisar_otro_jug_cuenta = {
                'comando': 'iniciar cuenta',
                'id': self.jugador_2['id'],
                'jugador 1': self.jugador_1['nombre'],
                'jugador 2': self.jugador_2['nombre']}
            self.parent.pre_enviar_datos(avisar_otro_jug_cuenta)
        elif self.jugador_2['nombre'] is None:
            self.jugador_2['nombre'] = nombre
            self.jugador_2['id'] = id_cliente
            self.sala_llena = True
            avisar_otro_jug_cuenta = {
                'comando': 'iniciar cuenta',
                'id': self.jugador_1['id'],
                'jugador 1': self.jugador_1['nombre'],
                'jugador 2': self.jugador_2['nombre']}
            self.parent.pre_enviar_datos(avisar_otro_jug_cuenta)

    def cuenta_termino(self, datos: dict):
        respuesta = datos
        if self.terminaron_de_contar == 1:
            self.terminaron_de_contar = 0
            respuesta['comando'] = 'iniciar partida'
            respuesta_otro_jug = {'comando': 'iniciar partida'}
            if respuesta['id'] == self.jugador_1['id']:
                respuesta_otro_jug['id'] = self.jugador_2['id']
            elif respuesta['id'] == self.jugador_2['id']:
                respuesta_otro_jug['id'] = self.jugador_1['id']
            self.parent.log('partida', 'inicia',
                            f'entre {self.jugador_1["nombre"]} id {self.jugador_1["id"]} \
                             y {self.jugador_2["nombre"]} id {self.jugador_2["id"]}')
            self.parent.pre_enviar_datos(respuesta_otro_jug)
        else:
            self.terminaron_de_contar += 1
        return respuesta

    def desconexion_repentina(self, id_cliente):
        if id_cliente == self.jugador_1['id'] and self.jugando:
            pass  # TODO jugador 2 gana
        elif id_cliente == self.jugador_2['id'] and self.jugando:
            pass  # TODO jugador 1 gana
