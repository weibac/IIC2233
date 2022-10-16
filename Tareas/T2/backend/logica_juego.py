from PyQt5.QtCore import QObject, pyqtSignal, QTimer

from backend.elementos_juego import Girasol, Lanzaguisantes, LanzaguisantesH, Papa, Zombie, \
 Proyectil
from aparicion_zombies import intervalo_aparicion
import parametros as p
import random


class LogicaJuego(QObject):

    senal_crear_sprite_zombie = pyqtSignal(int, tuple, tuple)
    senal_actualizar_sprite_zombie = pyqtSignal(int, tuple, tuple)
    senal_respuesta_compra_planta = pyqtSignal(str, int, int, int)
    senal_actualizar_soles = pyqtSignal(int)
    senal_perder = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.ronda = 0
        self._soles = p.SOLES_INICIALES

        self.casillas = [['' for _ in range(10)] for _ in range(2)]

        # Dicts elementos
        self.girasoles = {}
        self.lanzags = {}
        self.lanzags_h = {}
        self.papas = {}
        self.proyectiles = {}
        self.proyectiles_h = {}
        self.zombies = {}

        # Timers
        self.timers_lanzag = {}
        self.timers_lanzag_h = {}

        # self.timer_creacion_sol = QTimer()
        # self.timer_creacion_sol.setInterval()

        self.timer_creacion_zombie = QTimer()
        self.timer_creacion_zombie.timeout.connect(self.crear_zombie)
        self.timer_actualizar = QTimer()
        self.timer_actualizar.setInterval(p.TICK)
        self.timer_actualizar.timeout.connect(self.actualizar_elementos)

    @property
    def soles(self):
        return self._soles

    @soles.setter
    def soles(self, value):
        self._soles = value
        self.senal_actualizar_soles.emit(self._soles)

    def iniciar_juego(self, nombre, escenario):
        self.nombre = nombre
        self.escenario = escenario
        if escenario == 'abuela':
            self.ponderador = p.PONDERADOR_DIURNO
        elif escenario == 'nocturna':
            self.ponderador = p.PONDERADOR_NOCTURNO
        self.nueva_ronda()

    def nueva_ronda(self):
        self.ronda += 1
        self.zombies_arriba = 0
        self.zombies_abajo = 0
        self.timer_creacion_zombie.setInterval(
            int(intervalo_aparicion(self.ronda, self.ponderador) * 1000))

    def comenzar_tiempo(self):
        # Comenzar todos los timers
        # Incluyendo los de las entidades
        self.timer_actualizar.start()
        self.timer_creacion_zombie.start()

    def pausar(self):
        self.timer_actualizar.stop()
        self.timer_creacion_zombie.stop()

    def crear_zombie(self):
        if self.zombies_arriba < p.N_ZOMBIES and self.zombies_abajo < p.N_ZOMBIES:
            if random.random() < 0.5:
                zombie = Zombie('arriba')
                self.zombies_arriba += 1
            else:
                zombie = Zombie('abajo')
                self.zombies_abajo += 1
        elif self.zombies_arriba < p.N_ZOMBIES:
            zombie = Zombie('arriba')
            self.zombies_arriba += 1
        elif self.zombies_abajo < p.N_ZOMBIES:
            zombie = Zombie('abajo')
            self.zombies_abajo += 1
        if self.zombies_arriba < p.N_ZOMBIES or self.zombies_abajo < p.N_ZOMBIES:
            self.zombies[zombie.id] = zombie
            apariencia, ubicacion = self.datos_sprite_zombie(zombie.id)
            self.senal_crear_sprite_zombie.emit(zombie.id, apariencia, ubicacion)

    def revisar_comprar_planta(self, planta, x_casilla, y_casilla):
        if planta == 'girasol':
            costo = p.COSTO_GIRASOL
        elif planta == 'lanzag':
            costo = p.COSTO_LANZAGUISANTE
        elif planta == 'lanzag_h':
            costo = p.COSTO_LANZAGUISANTE_HIELO
        elif planta == 'papa':
            costo = p.COSTO_PAPA
        if self.casillas[y_casilla][x_casilla] != '':
            self.senal_respuesta_compra_planta.emit('casilla ocupada', 0, 0, 0)
        elif costo > self.soles:
            self.senal_respuesta_compra_planta.emit('soles insuficientes', 0, 0, 0)
        else:
            if planta == 'girasol':
                girasol = Girasol()
                id = girasol.id
                self.girasoles[id] = girasol
            elif planta == 'lanzag':
                lanzag = Lanzaguisantes()
                id = lanzag.id
                timer = QTimer()
                timer.setInterval(p.INTERVALO_DISPARO)
                timer.start()
                self.lanzags[id] = lanzag
                self.timers_lanzag[id] = timer
            elif planta == 'lanzag_h':
                lanzag_h = LanzaguisantesH()
                id = lanzag_h.id
                timer = QTimer()
                timer.setInterval(p.INTERVALO_DISPARO)
                timer.start()
                self.lanzags_h[id] = lanzag_h
                self.timers_lanzag_h[id] = timer
            elif planta == 'papa':
                papa = Papa()
                id = papa.id
                self.papas[id] = papa
            self.casillas[y_casilla][x_casilla] = (planta, id)
            self.soles -= costo
            self.senal_respuesta_compra_planta.emit(planta, id, x_casilla, y_casilla)

    def disparo(id):
        pass

    def actualizar_elementos(self):
        # self.correr_plantas
        # self.correr_proyectiles
        self.correr_zombies()

    def correr_zombies(self):
        for id in range(len(self.zombies)):
            self.correr_zombie(id)

    def correr_zombie(self, id):
        if self.zombies[id].estado == 'Cam':
            self.zombies[id].x -= self.zombies[id].paso
            self.zombies[id].frame_caminar = (self.zombies[id].frame_caminar + 1) % 2
            if self.zombies[id].x <= 240:
                self.pausar()
                self.senal_perder.emit()
        elif self.zombies[id].estado == 'Com':
            # hacer daño
            # cambiar sprite
            pass
        self.actualizar_frontend_zombie(id)

    def actualizar_frontend_zombie(self, id):
        apariencia, ubicacion = self.datos_sprite_zombie(id)
        self.senal_actualizar_sprite_zombie.emit(id, apariencia, ubicacion)

    def datos_sprite_zombie(self, id):
        zombie = self.zombies[id]
        if zombie.estado == 'Cam':
            apariencia = (zombie.tipo, zombie.estado, zombie.frame_caminar + 1)
        elif zombie.estado == 'Com':
            apariencia = (zombie.tipo, zombie.estado, zombie.frame_comer + 1)
        ubicacion = (int(zombie.x), int(zombie.y))
        return apariencia, ubicacion
