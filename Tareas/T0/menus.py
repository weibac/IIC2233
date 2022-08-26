def input_valido(set_opciones, mensaje, check_mode):
    valido = False
    inp = input(mensaje)

    while not valido:
        if check_mode == 'int':        
            if not inp.isdigit():
                inp = input('Por favor introduce un número: ')
            elif int(inp) not in set_opciones:
                inp = input(f'Por favor selecciona uno de los números del menú {set_opciones}: ')
            else:
                inp = int(inp)
                valido = True
        elif check_mode == 'username':
            if not inp.isalnum():
                inp = input('Por favor usa un nombre que tenga solo letras o números: ')
            else:
                valido = True
        else:
            print(f'Hey! No tienes definido el parámetro {check_mode}')
    return inp




inicio_str = '''
Bienvenido a Star Advanced!
Selecciona una opción:
[1] Nueva partida
[2] Cargar partida
[3] Ver ranking de puntajes
[0] Salir
'''