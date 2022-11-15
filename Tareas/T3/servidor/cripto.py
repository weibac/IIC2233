from collections import deque


def encriptar(msg: bytearray) -> bytearray:
    # Repartir en grupos a, b, c
    bytes_a = bytearray()
    bytes_b = bytearray()
    bytes_c = bytearray()
    i = 0
    for _ in msg:
        mod = i % 3
        if mod == 0:
            bytes_a.extend(msg[i].to_bytes(1, 'big'))
        elif mod == 1:
            bytes_b.extend(msg[i].to_bytes(1, 'big'))
        elif mod == 2:
            bytes_c.extend(msg[i].to_bytes(1, 'big'))
        i += 1
    # Calcular suma
    len_b = len(bytes_b)
    if len_b % 2 == 0:
        mitad = (len_b // 2) - 1
        central = bytes_b[mitad:mitad + 2]
        suma_central = int(central[0]) + int(central[1])
    else:
        central = bytes_b[(len_b - 1) // 2]
        suma_central = int(central)
    suma = int(bytes_a[0]) + suma_central + int(bytes_c[-1])
    # Hacer operaciones según resultado suma
    out_array = bytearray()
    if suma % 2 == 0:
        out_array += b'\x00' + bytes_c + bytes_a + bytes_b
    else:
        out_array += b'\x01' + bytes_a + bytes_c + bytes_b
    return out_array


def desencriptar(msg: bytearray) -> bytearray:
    # Completar con el proceso de desencriptación
    # Obtener largos a, b y c
    len_original = len(msg) - 1  # Sin el \x00 o \x01 del principio
    if len_original % 3 == 0:
        len_a = len_original // 3
        len_b = len_original // 3
        len_c = len_original // 3
    elif len_original % 3 == 1:
        len_a = (len_original // 3) + 1
        len_b = len_original // 3
        len_c = len_original // 3
    elif len_original % 3 == 2:
        len_a = (len_original // 3) + 1
        len_b = (len_original // 3) + 1
        len_c = len_original // 3
    # Separar a, b y c
    if msg[0] == 0:  # cab
        bytes_c = msg[1:len_c + 1]
        bytes_a = msg[len_c + 1:len_c + len_a + 1]
        bytes_b = msg[len_c + len_a + 1:]
    elif msg[0] == 1:  # acb
        bytes_a = msg[1:len_a + 1]
        bytes_c = msg[len_a + 1:len_a + len_c + 1]
        bytes_b = msg[len_a + len_c + 1:]
    # Juntar a, b y c
    out_array = bytearray()
    bytes_a = deque(bytes_a)
    bytes_b = deque(bytes_b)
    bytes_c = deque(bytes_c)
    for i in range(len_original):
        if i % 3 == 0:
            out_array.extend(bytes_a.popleft().to_bytes(1, 'big')) if bytes_a else None
        elif i % 3 == 1:
            out_array.extend(bytes_b.popleft().to_bytes(1, 'big')) if bytes_b else None
        elif i % 3 == 2:
            out_array.extend(bytes_c.popleft().to_bytes(1, 'big')) if bytes_c else None
    return out_array


if __name__ == "__main__":
    # Testear encriptar
    msg_original = bytearray(b'\x05\x08\x03\x02\x04\x03\x05\x09\x05\x09\x01')
    msg_esperado = bytearray(b'\x01\x05\x02\x05\x09\x03\x03\x05\x08\x04\x09\x01')

    msg_encriptado = encriptar(msg_original)
    if msg_encriptado != msg_esperado:
        print("[ERROR] Mensaje escriptado erroneamente")
        # Adiciones para debug
        print(f'Mensaje original: {msg_original}')
        print(f'Mensaje esperado: {msg_esperado}')
        print(f'Mensaje obtenido: {msg_encriptado}')
    else:
        print("[SUCCESSFUL] Mensaje escriptado correctamente")

    # Testear desencriptar
    msg_desencriptado = desencriptar(msg_esperado)
    if msg_desencriptado != msg_original:
        print("[ERROR] Mensaje descencriptado erroneamente")
        # Adiciones para debug
        print(f'Mensaje original: {msg_original}')
        print(f'Mensaje esperado: {msg_esperado}')
        print(f'Mensaje obtenido: {msg_desencriptado}')
    else:
        print("[SUCCESSFUL] Mensaje descencriptado correctamente")
