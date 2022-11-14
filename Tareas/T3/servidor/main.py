from aux_json import dict_json
from servidor import Servidor
import sys

if __name__ == "__main__":
    PARAMETROS = dict_json()
    servidor = Servidor(PARAMETROS['HOST'], PARAMETROS['PORT'])

    # Conectar señales
    servidor.logica_juego.senal_hablar_cliente.connect(
        servidor.pre_enviar_datos)

    try:
        while True:
            msg = "[Presione Ctrl+C para cerrar]".center(80, " ") + "\n" + "".center(80, "-") + "\n"
            input(msg)
    except KeyboardInterrupt:
        print("\n\n")
        print("Cerrando servidor...".center(80, " "))
        print("".center(80, "-"))
        print("".center(80, "-") + "\n")
        servidor.socket_servidor.close()
        sys.exit()
