
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
            elif len(inp) > 8:
                inp = input('Por favor usa un nombre de 8 o menos letras o números: ')
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
[0] Salir al menú de inicio
'''

salir_str = '''
Quieres guardar la partida?
[1] Si
[2] No
[0] No quiero salir
'''


def end_str(victoria):
    if victoria:
        end_str = 'Victoria! {}, has encontrado a todas las bestias!'
    else:
        end_str = 'Oh no! {}, te ha comido una bestia Nexus!'
    end_str += '''
Tu puntaje en esta partida fue de: {}
Este era el tablero (las bestias están marcadas con N):
'''
    return end_str


def partidas_str(partidas):
    str_partidas_out = 'Selecciona una de las partidas guardadas:\n'
    for a in range(len(partidas)):
        str_partidas_out += f'[{a + 1}] {partidas[a]}\n'
    str_partidas_out += '[0] Volver atrás'
    return str_partidas_out


def ranking_str(puntajes):
    ranking_str = '''Ranking de las 10 mejores partidas:
 N° Puntaje  Nombre    Resultado  Turnos  Dimensiones tablero (x*y)
'''
    puntajes.sort(key=por_puntaje)
    if len(puntajes) > 10:
        puntajes = puntajes[10]
    n = 1
    for p in puntajes:
        victoria = 'Victoria' if p[2] == 'True' else 'Derrota'
        dimensiones = f'{p[4]}*{p[5]}'
        ranking_str += f'{n:4}{p[0]:^9}{p[1]:10}{victoria:11}{p[3]:^8}{dimensiones:25}\n'
        n += 1
    return ranking_str


def por_puntaje(p):
    return -int(p[0])
