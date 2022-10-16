from PyQt5.QtCore import QObject, pyqtSignal, QTimer

from backend.elementos_juego import Girasol, Lanzaguisantes, LanzaguisantesH, Papa, Zombie, \
 Proyectil
from aparicion_zombies import intervalo_aparicion
import parametros as p


class LogicaJuego(QObject):

    senal_crear_sprite_zombie = pyqtSignal(int, tuple, tuple)
    senal_actualizar_sprite_zombie = pyqtSignal(int, tuple, tuple)
    senal_respuesta_compra_planta = pyqtSignal(str, int, int, int)

    def __init__(self):
        super().__init__()

        self.ronda = 0
        self.soles = 200  # TEST

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
        # self.timer_creacion_zombie = QTimer()
        # self.timer_creacion_zombie.setInterval()
        # self.timer_creacion_sol = QTimer()
        # self.timer_creacion_sol.setInterval()

        self.timer_actualizar = QTimer()
        self.timer_actualizar.setInterval(p.TICK)
        self.timer_actualizar.timeout.connect(self.actualizar_elementos)

    def iniciar_juego(self, nombre, escenario):
        self.nombre = nombre
        self.escenario = escenario
        self.crear_zombie()
        self.crear_zombie()
        self.comenzar_tiempo()  # TODO sacar esto solo para test

    def comenzar_tiempo(self):
        # Comenzar todos los timers
        # Incluyendo los de las entidades
        self.timer_actualizar.start()

    def crear_zombie(self):
        zombie = Zombie()
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
                self.lanzags[id] = lanzag
            elif planta == 'lanzag_h':
                lanzag_h = LanzaguisantesH()
                id = lanzag_h.id
                self.lanzags_h[id] = lanzag_h
            elif planta == 'papa':
                papa = Papa()
                id = papa.id
                self.papas[id] = papa
            self.casillas[y_casilla][x_casilla] = (planta, id)
            self.soles -= costo
            self.senal_respuesta_compra_planta.emit(planta, id, x_casilla, y_casilla)

    def disparo(id):
        pass

    def pausar(self):
        # Parar todos los timers
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
