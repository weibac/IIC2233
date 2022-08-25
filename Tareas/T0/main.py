import tablero, menus, juego

inp = menus.menu_inicio()
if inp == 1:
    tablero.print_tablero(juego.crear_tableros(*menus.nueva_partida()))
    