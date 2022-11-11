from aux_json import dict_json
from servidor import Servidor

if __name__ == "__main__":
    PARAMETROS = dict_json()
    servidor = Servidor(PARAMETROS['HOST'], PARAMETROS['PORT'])
