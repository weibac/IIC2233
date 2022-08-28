from parametros import (AFINIDAD_HIT, AFINIDAD_INICIAL, AFINIDAD_PUBLICO_POP,
                        AFINIDAD_STAFF_POP, AFINIDAD_PUBLICO_ROCK,
                        AFINIDAD_STAFF_ROCK, AFINIDAD_PUBLICO_TRAP_CHILENO,
                        AFINIDAD_STAFF_TRAP_CHILENO, AFINIDAD_PUBLICO_REG,
                        AFINIDAD_STAFF_REG, AFINIDAD_ACCION_POP,
                        AFINIDAD_ACCION_ROCK, AFINIDAD_ACCION_TRAP_CHILENO,
                        AFINIDAD_ACCION_REG, AFINIDAD_MIN, AFINIDAD_MAX)


class Artista:
    def __init__(self, nombre, genero, dia_presentacion,
                 hit_del_momento):
        self.nombre = nombre
        self.hit_del_momento = hit_del_momento
        self.genero = genero
        self.dia_presentacion = dia_presentacion
        self._afinidad_con_publico = AFINIDAD_INICIAL
        self._afinidad_con_staff = AFINIDAD_INICIAL

    @property
    def afinidad_con_publico(self):
        # COMPLETAR
        return self._afinidad_con_publico
    
    @afinidad_con_publico.setter
    def afinidad_con_publico(self, value):
        if value > AFINIDAD_MAX:
            return AFINIDAD_MAX
        elif value > AFINIDAD_MIN:
            return AFINIDAD_MIN
        else:
            return value

    @property
    def afinidad_con_staff(self):
        # COMPLETAR
        return self._afinidad_con_staff
 
    @afinidad_con_staff.setter
    def afinidad_con_staff(self, value):
        if value > AFINIDAD_MAX:
            return AFINIDAD_MAX
        elif value > AFINIDAD_MIN:
            return AFINIDAD_MIN
        else:
            return value

    @property
    def animo(self):
        # COMPLETAR
        return int(self.afinidad_con_publico * 0.5) + int(self.afinidad_con_staff * 0.5)
    
    def recibir_suministros(self, suministro):
        # COMPLETAR
        if suministro.valor_de_satisfaccion < 0:
            print(f"{self.nombre} recibió {suministro.nombre} en malas condiciones.")
        else:
            print(f"{self.nombre} recibió un {suministro.nombre} a tiempo!")
        self.afinidad_con_staff += suministro.valor_de_satisfaccion

    def cantar_hit(self):
        # COMPLETAR
        print(f"{self.nombre} está tocando su hit: {self.hit_del_momento}!")
        self.afinidad_con_publico += AFINIDAD_HIT

    def __str__(self):
        # COMPLETAR
        return '''Nombre: {self.nombre}
Genero: {self.genero}
Animo: {self.animo}'''


class ArtistaPop(Artista):
    def __init__(self, nombre, hit_del_momento, genero, dia_presentacion):
        # COMPLETAR
        super().__init__(nombre, hit_del_momento, genero, dia_presentacion)
        self.accion = "Cambio de vestuario"
        self._afinidad_con_publico = AFINIDAD_PUBLICO_POP
        self._afinidad_con_staff = AFINIDAD_STAFF_POP

    def accion_especial(self):
        # COMPLETAR
        print(f"{self.nombre} hará un {self.accion}")
        self.afinidad_con_publico += AFINIDAD_ACCION_POP

    @property
    def animo(self):
        # COMPLETAR
        animo = super().animo
        if animo < 10:
            print(f"ArtistaPop peligrando en el concierto. Animo: {animo}")
        else:
            print(f"Animo de ArtistaPop: {animo}")
        return animo


class ArtistaRock(Artista):
    def __init__(self, nombre, hit_del_momento, genero, dia_presentacion):
        # OMPLETAR
        super().__init__(nombre, hit_del_momento, genero, dia_presentacion)
        self.accion = "Solo de guitarra"
        self._afinidad_con_publico = AFINIDAD_PUBLICO_ROCK
        self._afinidad_con_staff = AFINIDAD_STAFF_ROCK

    def accion_especial(self):
        # COMPLETAR
        print(f"{self.nombre} hará un {self.accion}")
        self.afinidad_con_publico += AFINIDAD_ACCION_ROCK

    @property
    def animo(self):
        # COMPLETAR
        animo = super().animo
        if animo < 10:
            print(f"ArtistaRock peligrando en el concierto. Animo: {animo}")
        else:
            print(f"Animo de ArtistaRock: {animo}")
        return animo


class ArtistaTrapChileno(Artista):
    def __init__(self, nombre, hit_del_momento, genero, dia_presentacion):
        # COMPLETAR
        super().__init__(nombre, hit_del_momento, genero, dia_presentacion)
        self.accion = "Malianteo"
        self._afinidad_con_publico = AFINIDAD_PUBLICO_TRAP_CHILENO
        self._afinidad_con_staff = AFINIDAD_STAFF_TRAP_CHILENO

    def accion_especial(self):
        # COMPLETAR
        print(f"{self.nombre} hará un {self.accion}")
        self.afinidad_con_publico += AFINIDAD_ACCION_TRAP_CHILENO

    @property
    def animo(self):
        # COMPLETAR
        animo = super().animo
        if animo < 10:
            print(f"ArtistaTrapChileno peligrando en el concierto. Animo: {animo}")
        else:
            print(f"Animo de ArtistaTrapChileno: {animo}")
        return animo


class ArtistaReggaeton(Artista):
    def __init__(self, nombre, hit_del_momento, genero, dia_presentacion):
        # COMPLETAR
        super().__init__(nombre, hit_del_momento, genero, dia_presentacion)
        self.accion = "Perrear"
        self._afinidad_con_publico = AFINIDAD_PUBLICO_REG
        self._afinidad_con_staff = AFINIDAD_STAFF_REG

    def accion_especial(self):
        # COMPLETAR
        print(f"{self.nombre} hará un {self.accion}")
        self.afinidad_con_publico += AFINIDAD_ACCION_REG

    @property
    def animo(self):
        # COMPLETAR
        animo = super().animo
        if animo < 10:
            print(f"ArtistaReggaeton peligrando en el concierto. Animo: {animo}")
        else:
            print(f"Animo de ArtistaReggaeton: {animo}")
        return animo