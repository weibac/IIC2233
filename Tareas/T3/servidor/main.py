from aux_json import dict_json
from servidor import Servidor
import sys

if __name__ == "__main__":
    PARAMETROS = dict_json()
    servidor = Servidor(PARAMETROS['HOST'], PARAMETROS['PORT'])

    try:
        while True:
            input("[Presione Ctrl+C para cerrar]".center(64, " ") + "\n")
    except KeyboardInterrupt:
        print("\n\n")
        print("Cerrando servidor...".center(80, " "))
        print("".center(82, "-"))
        print("".center(82, "-") + "\n")
        servidor.socket_servidor.close()
        sys.exit()
