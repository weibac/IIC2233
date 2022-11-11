"""
Esto puede que sirva pero en última instancia está mal.
El paquete inicial del largo del mensaje y cada paquete de 32 deben
ser enviados por separado, es decir, con distintos sendall() y recv()
"""


def codificar(msg: bytearray):
    # Inicio indicando el largo
    msg_codificado = bytearray(len(msg).to_bytes(4, 'big'))
    # Dividir por segmentos
    msg_segmentado = bytearray()
    seg_actual = 1
    for i in range(((len(msg) // 32) + 1) * 32):
        if i % 32 == 0:
            msg_segmentado.extend(seg_actual.to_bytes(4, 'little'))
            seg_actual += 1
        try:
            msg_segmentado.extend(msg[i].to_bytes(1, 'big'))
        except IndexError:
            msg_segmentado.extend(b'\x00')
    msg_codificado.extend(msg_segmentado)
    return msg_codificado


def decodificar(msg: bytearray):
    # Obtener largo original y sacar sus 4 bytes
    largo_original = int.from_bytes(msg[:4], 'big')
    msg = msg[4:]
    # Sacar los 4 bytes de número de cada segmento
    segmentos = (largo_original // 32) + 1
    msg_original = bytearray()
    for seg_actual in range(1, segmentos):
        inicio_bloque = ((seg_actual - 1) * 36) + 4
        msg_original.extend(msg[inicio_bloque:inicio_bloque + 32])
    # Último segmento: tratar el caso especial de no poner los \x00 del final
    inicio_bloque = ((segmentos - 1) * 36) + 4
    largo_bloque = largo_original % 32
    if largo_bloque == 0:
        msg_original.extend(msg[inicio_bloque:inicio_bloque + 32])
    else:
        msg_original.extend(msg[inicio_bloque:inicio_bloque + largo_bloque])
    return msg_original


if __name__ == "__main__":

    # Testear codificar
    print('Probando codificación.\n Por favor revisar manualmente.\n')
    msg_original = bytearray(b'\x03\x05\x08')
    msg_codificado = codificar(msg_original)
    print(f'Mensaje original: {msg_original}\n')
    print(f'Mensaje codificado: {msg_codificado}\n')

    # Testear decodificar
    print('Probando decodificación....\n')
    msg_original = bytearray()
    for i in range(250):
        msg_original.extend(i.to_bytes(1, 'big'))
    msg_decodificado = decodificar(codificar(msg_original))
    if msg_original == msg_decodificado:
        print('Mensage decodificado correctamente! :D\n')
        print(f'Mensaje original: {msg_original}\n')
        print(f'Mensaje decodificado: {msg_decodificado}')
    else:
        print('ERROR\n')
        print(f'Mensaje original: {msg_original}\n')
        print(f'Mensaje decodificado: {msg_decodificado}')
