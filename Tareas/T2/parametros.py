import os


# Dimensiones
ANCHO_PANTALLA_JUEGO = 900

ANCHO_ZOMBIE = 40
ALTO_ZOMBIE = 100

ANCHO_PLANTA = 30
ALTO_PLANTA = 60

# Tiempo maestro (ms)
TICK = 20
# Los intervalos están en milisegundos
INTERVALO_DISPARO = 2000
INTERVALO_SOLES_GIRASOL = 20000
INTERVALO_TIEMPO_MORDIDA = 5000

# El daño y la vida tienen las mismas medidas
DANO_PROYECTIL = 5
DANO_MORDIDA = 5
VIDA_PLANTA = 100
VIDA_ZOMBIE = 80

# Soles iniciales por ronda
SOLES_INICIALES = 250
# Número de soles generados por planta
CANTIDAD_SOLES = 2
# Número de soles agregados a la cuenta por recolección
SOLES_POR_RECOLECCION = 50
# Número de soles agregados a la cuenta por Cheatcode
SOLES_EXTRA = 25

# Ponderadores de escenarios
PONDERADOR_NOCTURNO = 0.8
PONDERADOR_DIURNO = 0.9

# El zombie normal debe demorarse 50000 ms en llegar al final
TIEMPO_LLEGAR_ZOMBIE = 50000
VELOCIDAD_ZOMBIE = (ANCHO_PANTALLA_JUEGO - 100) / TIEMPO_LLEGAR_ZOMBIE  # Pixeles / ms
# Puntaje por eliminar zombie
PUNTAJE_ZOMBIE_DIURNO = 50
PUNTAJE_ZOMBIE_NOCTURNO = 100
# Porcentaje de ralentización
RALENTIZAR_ZOMBIE = 0.25
# Número de zombies por carril
N_ZOMBIES = 7


# Costo por avanzar de ronda
COSTO_AVANZAR = 500
# Costo tiendas
COSTO_LANZAGUISANTE = 50
COSTO_LANZAGUISANTE_HIELO = 100
COSTO_GIRASOL = 50
COSTO_PAPA = 75

# Caracteres de nombre usuario
MIN_CARACTERES = 3
MAX_CARACTERES = 15


# RUTAS
# uis
RUTA_UI_VENTANA_INICIO = os.path.join('frontend', 'assets',  'ventana_inicio.ui')
RUTA_UI_VENTANA_RANKING = os.path.join('frontend', 'assets', 'ventana_ranking.ui')
RUTA_UI_VENTANA_SEL_ESCENARIO = os.path.join('frontend', 'assets',  'ventana_sel_escenario.ui')
RUTA_UI_VENTANA_JUEGO = os.path.join('frontend', 'assets',  'ventana_juego.ui')
# fondos
RUTA_FONDO_DIA = os.path.join('sprites', 'Fondos', 'jardinAbuela.png')
RUTA_FONDO_NOCHE = os.path.join('sprites', 'Fondos', 'salidaNocturna.png')
RUTA_FONDO_MENU = os.path.join('sprites', 'Fondos', 'fondoMenu.png')
# Dicts sprites

SPRITES_GIRASOL = {
    1: os.path.join('sprites', 'Plantas', 'girasol_1.png'),
    2: os.path.join('sprites', 'Plantas', 'girasol_2.png')
}
SPRITES_LANZAG = {
    1: os.path.join('sprites', 'Plantas', 'lanzaguisantes_1.png'),
    2: os.path.join('sprites', 'Plantas', 'lanzaguisantes_2.png'),
    3: os.path.join('sprites', 'Plantas', 'lanzaguisantes_3.png')
}
SPRITES_LANZAG_H = {
    1: os.path.join('sprites', 'Plantas', 'lanzaguisantesHielo_1.png'),
    2: os.path.join('sprites', 'Plantas', 'lanzaguisantesHielo_2.png'),
    3: os.path.join('sprites', 'Plantas', 'lanzaguisantesHielo_3.png')
}
SPRITES_PAPA = {
    1: os.path.join('sprites', 'Plantas', 'papa_1.png'),
    2: os.path.join('sprites', 'Plantas', 'papa_2.png'),
    3: os.path.join('sprites', 'Plantas', 'papa_3.png')
}
SPRITES_ZOMBIES = {
    ('Wkr', 'Cam', 1): os.path.join('sprites', 'Zombies', 'Caminando', 'zombieNicoWalker_1.png'),
    ('Wkr', 'Cam', 2): os.path.join('sprites', 'Zombies', 'Caminando', 'zombieNicoWalker_2.png'),
    ('Wkr', 'Com', 1): os.path.join('sprites', 'Zombies', 'Comiendo', 'zombieNicoComiendo_1.png'),
    ('Wkr', 'Com', 2): os.path.join('sprites', 'Zombies', 'Comiendo', 'zombieNicoComiendo_2.png'),
    ('Wkr', 'Com', 3): os.path.join('sprites', 'Zombies', 'Comiendo', 'zombieNicoComiendo_3.png'),
    ('Rnr', 'Cam', 1): os.path.join('sprites', 'Zombies', 'Caminando', 'zombieHernanRunner_1.png'),
    ('Rnr', 'Cam', 2): os.path.join('sprites', 'Zombies', 'Caminando', 'zombieHernanRunner_2.png'),
    ('Rnr', 'Com', 1): os.path.join('sprites', 'Zombies', 'Comiendo', 'zombieHernanComiendo_1.png'),
    ('Rnr', 'Com', 2): os.path.join('sprites', 'Zombies', 'Comiendo', 'zombieHernanComiendo_2.png'),
    ('Rnr', 'Com', 3): os.path.join('sprites', 'Zombies', 'Comiendo', 'zombieHernanComiendo_3.png')
}
