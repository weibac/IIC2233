
def input_valido(set_opciones, mensaje):
    valido = False
    inp = input(mensaje)
    while not valido:
        if not inp.isdigit():
            inp = input('Por favor introduce un número: ')
        elif int(inp) not in set_opciones:
            inp = input(f'Por favor selecciona uno de los números del menú {set_opciones}: ')
        else:
            valido = True
    return int(inp)


def menu_inicio():
    print('''
Bienvenido a Star Advanced!
Selecciona una opción:
[1] Nueva partida
[2] Cargar partida
[3] Ver ranking de puntajes
[0] Salir
''')
    return input_valido(set(range(0, 4)), 'Tu opción aquí: ')


def nueva_partida():
    print('\nHas seleccionado iniciar una nueva partida')
    x = input_valido(set(range(3, 16)), 'Ancho del tablero (min = 3, max = 15): ')
    y = input_valido(set(range(3, 16)), 'Largo del tablero (min = 3, max = 15): ')
    return (x, y)
