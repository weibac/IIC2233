from time import sleep
from threading import Thread

from centro_urbano import CentroUrbano

from parametros import ENERGIA_RECOLECTOR, ORO_RECOLECTADO, \
    TIEMPO_RECOLECCION, TIEMPO_CONSTRUCCION, ORO_CHOZA


# Completar
class Recolector(Thread):

    def __init__(self, nombre: str, centro_urbano: CentroUrbano) -> None:
        self.nombre = nombre
        self.centro_urbano = centro_urbano
        self.energia = ENERGIA_RECOLECTOR
        self.oro = 0
        # Completar
        super().__init__()
        self.daemon = True

    def run(self) -> None:
        self.trabajar()
        self.ingresar_oro()
        self.dormir()

    def log(self, mensage: str) -> None:
        print(f"El recolector {self.nombre}: {mensage}")

    def trabajar(self) -> None:
        # Completar
        self.log('ha empezado su trabajo')
        self.oro += ORO_RECOLECTADO
        self.log(f'ha recolectado {ORO_RECOLECTADO} monedas de oro')
        self.energia -= 1
        sleep(TIEMPO_RECOLECCION)
        self.log(f'ha terminado su trabajo de recolección')

    def ingresar_oro(self) -> None:
        # Completar
        self.centro_urbano.lock_oro.acquire()
        self.centro_urbano.oro += self.oro
        self.oro = 0
        self.log('ha depositado su oro')
        self.log(f'ahora hay {self.centro_urbano.oro} de oro en el centro urbano')
        self.centro_urbano.lock_oro.release()

    def dormir(self) -> None:
        self.log("ha terminado su turno, procede a mimir")


# Completar
class Constructor(Thread):

    def __init__(self, nombre, centro_urbano: CentroUrbano) -> None:
        self.nombre = nombre
        self.centro_urbano = centro_urbano
        # Completar
        super().__init__()
        self.daemon = True

    def run(self) -> None:
        while self.retirar_oro():
            self.centro_urbano.lock_chozas.acquire()
            self.log("está construyendo una choza de bárbaros")
            sleep(TIEMPO_CONSTRUCCION)
            self.construir_choza()
            self.centro_urbano.lock_chozas.release()
        self.log("terminó su trabajo por el día")

    def log(self, mensage: str) -> None:
        print(f"El constructor {self.nombre}: {mensage}")

    def retirar_oro(self) -> bool:
        # Completar
        self.centro_urbano.lock_chozas.acquire()
        if self.centro_urbano.oro >= ORO_CHOZA:
            self.centro_urbano.oro -= ORO_CHOZA
            self.log(f'ha retirado {ORO_CHOZA} de oro y ahora queda {self.centro_urbano.oro}')
            self.centro_urbano.lock_chozas.release()
            return True
        else:
            self.log(f'los {self.centro_urbano.oro} de oro disponibles no son suficientes')
            self.centro_urbano.lock_chozas.release()
            return False

    def construir_choza(self) -> None:
        # Completar
        self.centro_urbano.chozas += 1
        self.log(f'ha construido una choza. Ahora hay {self.centro_urbano.chozas} chozas')
