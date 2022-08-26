
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
            letras = set(aux_revisar.keys())
            numeros = set(aux_revisar.values())
            if not set(inp.split()) <= letras | numeros | {' '}:
                inp = input('Por favor coloca solo letras, numeros y espacios: ')           
            else:
                inp = inp.strip(' ')
                inp = join([c for c in inp if (c != ' ') or (' ' not in inp)]).split(' ')
                if inp[0] <= letras and inp[1] <= numeros \
                or inp[1] <= letras and inp[0] <= numeros:
                    valido = True
                else:
                    inp = input('Parece que mezclaste letras y numeros. Intenta de nuevo: ')

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