# Rutas archivos
RUTA_ENTRENADORES = ('datos', 'entrenadores.csv')
RUTA_PROGRAMONES = ('datos', 'programones.csv')
RUTA_EVOLUCIONES = ('datos', 'evoluciones.csv')
RUTA_OBJETOS = ('datos', 'objetos.csv')

# Menus
OPCIONES_MENU_BASE = ['Volver', 'Salir']
HEADER_MENU_ENTRENADOR = 'Menú entrenador'
OPCIONES_MENU_ENTRENADOR = ['Entrenar programon', 'Simular ronda', 'Resumen campeonato',
                            'Crear objeto', 'Utilizar objeto', 'Estado entrenador',
                            'Volver', 'Salir']
HEADER_MENU_OBJETOS = 'Menú objetos'
OPCIONES_MENU_OBJETOS = ['Baya', 'Poción', 'Caramelo', 'Volver', 'Salir']
HEADER_MENU_INICIO = 'Menú inicio: Selecciona a tu entrenador!'
HEADER_MENU_USAR_OBJ = 'Objetos disponibles:'
HEADER_MENU_PROGRAMONES = 'Elige uno de tus programones:'


# Entrenadores
MIN_ENERGIA = 0
MAX_ENERGIA = 100

# Niveles programones
MIN_NIVEL = 1
MAX_NIVEL = 100
MIN_EXPERIENCIA = 0
MAX_EXPERIENCIA = 100
ENERGIA_ENTRENAMIENTO = 20
MIN_AUMENTO_ENTRENAMIENTO = 2  # TODO: REBALANCEAR
MAX_AUMENTO_ENTRENAMIENTO = 5  # TODO: REBALANCEAR
MIN_AUMENTO_EXPERIENCIA = 100  # TODO: REBALANCEAR
MAX_AUMENTO_EXPERIENCIA = 100  # TODO: REBALANCEAR
# TODO: Dicen por wsp que en una issue dicen que los aumentos
# son distintos para cada atributo programon (ex.: ataque, defensa)

# Megaevolución programones
MEGA_VIDA = 52
MEGA_ATAQUE = 38
MEGA_DEFENSA = 50
MEGA_VELOCIDAD = 40

# Lucha  programones
MIN_VIDA = 1
MAX_VIDA = 255
MIN_ATAQUE = 5
MAX_ATAQUE = 190
MIN_DEFENSA = 5
MAX_DEFENSA = 250
MIN_VELOCIDAD = 5
MAX_VELOCIDAD = 200
ORDEN_VENTAJAS = ['fuego', 'planta', 'agua']
PONDERACIONES_LUCHA = (0.2, 0.3, 0.15, 0.15, 0.2, 40)
AUMENTAR_ATAQUE_FUEGO = 38
AUMENTAR_VIDA_PLANTA = 52
AUMENTAR_VELOCIDAD_AGUA = 40

# Objetos
PROB_EXITO_BAYA = 0.75
GASTO_ENERGIA_BAYA = 20
MIN_AUMENTO_BAYA = 1
MAX_AUMENTO_BAYA = 10
PROB_EXITO_POCION = 0.75
GASTO_ENERGIA_POCION = 20
MIN_AUMENTO_POCION = 1
MAX_AUMENTO_POCION = 7
PROB_EXITO_CARAMELO = 0.9
GASTO_ENERGIA_CARAMELO = 30
AUMENTO_DEFENSA = 10
