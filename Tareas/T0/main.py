import tablero, menus, juego, sys

inp = menus.menu_inicio()
if inp == 1:
    game = juego.Partida(*menus.nueva_partida())
    tablero.print_tablero(game.tablero_real)
    
elif inp == 0:
    sys.exit('\nVuelve pronto!')