def comprobar_nombre(self, nombre):
    respuesta = ''
    valido = False
    if not 0 < len(nombre) < 11:
        respuesta = 'El nombre debe tener entre 1 y 10 caracteres'
    elif not nombre.isalnum():
        respuesta = 'El nombre debe ser alfanumerico'
    if respuesta == '':
        valido = True
        self.senal_abrir_sala_espera.emit()
    self.senal_validez_nombre.emit(valido, respuesta)