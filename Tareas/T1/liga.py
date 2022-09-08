from entrenadores import Entrenador

class LigaProgramon:
    def __init__(self, datos) -> None:
        self.entrenadores = [Entrenador(**datos.entrens[nom]) for nom in datos.entrens]
        self.perdedores = []
        self.ronda_actual = 0
        self.campeon = None

    def resumen_campeonato(self):
        pass

    def simular_ronda(self):
        pass
