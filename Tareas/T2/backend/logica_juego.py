from PyQt5.QtCore import QObject, pyqtSignal, QTimer

from backend.elementos_juego import Lanzaguizantes, Zombie, Proyectil, Planta
from aparicion_zombies import intervalo_aparicion
import parametros as p


class LogicaJuego(QObject):

    senal_crear_sprite_zombie = pyqtSignal(int, tuple, tuple)
    senal_actualizar_sprite_zombie = pyqtSignal(int, tuple, tuple)

    def __init__(self):
        super().__init__()

        self.ronda = 0

        # Dicts elementos
        self.plantas = {}
        self.lanzaguisantes = {}
        self.proyectiles = {}
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

    def crear_lanzaguisante(self):
        lanzag = Lanzaguizantes()
        lanzag.timer_disparo.timeout.connect(self.disparo)
        self.lanzaguisantes[lanzag.id] = lanzag
        self.lanzaguisantes[lanzag.id].timer_disparo.start()


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
        print('zombie corriendo')
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
