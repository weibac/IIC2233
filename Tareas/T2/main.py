import sys

from dccruz_vs_zombies import DccCruzVsZombies

if __name__ == '__main__':
    def hook(type_, value, traceback):
        print(type_)
        print(traceback)
    sys.__excepthook__ = hook

    juego = DccCruzVsZombies(sys.argv)
    juego.iniciar()
    sys.exit(juego.exec())
