import tablero, menus, juego

inp = menus.menu_inicio()
if inp == 1:
    
    game = juego.Partida(*menus.nueva_partida())
    tablero.print_tablero(game.tablero_real)
    