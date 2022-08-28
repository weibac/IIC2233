
def input_valido(aux_revisar, mensaje, modo_revisar):
    valido = False
    inp = input(mensaje)

    while not valido:
        if modo_revisar == 'int':
            if not inp.isdigit():
                inp = input('Por favor introduce un número: ')
            elif int(inp) not in aux_revisar:
                inp = input(f'Por favor selecciona uno de los números del menú {aux_revisar}: ')
            else:
                inp = int(inp)
                valido = True

        elif modo_revisar == 'coords':
            letras = set(aux_revisar.letras_num.keys())
            letras_lower = {letra.lower() for letra in letras}
            numeros = {str(n) for n in aux_revisar.letras_num.values()}
            if not set(inp) <= (letras | letras_lower | numeros):
                inp = input('Por favor coloca solo letras y números: ')
            elif not inp[0].isalpha():
                inp = input('Por favor coloca la coordenada letra al principio: ')
            elif not inp[1:].isdigit():
                inp = input('Después de la letra, por favor coloca la coordenada número: ')
            else:
                inp = aux_revisar.interpretar_coords(inp)
                if inp in aux_revisar.descubiertas:
                    inp = input('Ya has descubierto ese sector. Prueba con otro: ')
                else:
                    valido = True

        elif modo_revisar == 'username':
            if not inp.isalnum():
                inp = input('Por favor usa un nombre que tenga solo letras o números: ')
            else:
                valido = True
        else:
            print(f'Hey! No tienes definido el parámetro {modo_revisar}')
    return inp


inicio_str = '''
Bienvenido a Star Advanced!
Selecciona una opción:
[1] Nueva partida
[2] Cargar partida
[3] Ver ranking de puntajes
[0] Salir
'''

juego_str = '''
Turno {}
Selecciona una opción:
[1] Descubrir sector
[2] Guardar partida
[3] Salir de la partida
[0] Salir
'''

perder_str = '''
Oh no! {}, te ha comido una bestia Nexus!
Tu puntaje en esta partida fue de: {}
Este era el tablero:
'''
