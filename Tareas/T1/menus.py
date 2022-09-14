from typing import List


class Menu():
    def __init__(self, header: str, opciones: List[str]) -> None:
        self.header = header
        self.opciones = opciones
        self.opciones_dict = {a: self.opciones[a] for a in range(len(self.opciones))}
        self.largos_opciones = [len(opciones[ind]) + 4 + ind // 10 for ind in range(len(opciones))]
        self.ancho = max(self.largos_opciones)
        self.espacio_izq = int((self.ancho - len(self.header)) / 2)
        self.espacio_der = self.espacio_izq + 1

    def seleccionar_opcion(self) -> str:
        opciones = self.opciones_dict.keys()
        valido = False
        while not valido:
            print(self)
            inp = input('Por favor selecciona una opción: ')
            if not inp.isdigit():
                print('Las opciones pueden ser solo números\n')
            elif int(inp) not in opciones:
                print(f'Las opciones solo son las siguientes: {list(opciones)}\n')
            else:
                accion = self.opciones_dict[int(inp)]
                valido = True
        return accion

    def __str__(self) -> str:
        menu_str = ' ' * self.espacio_izq + self.header + ' ' * self.espacio_der + '\n' \
                 + '-' * self.ancho + '\n'
        for a in range(len(self.opciones)):
            menu_str += f'[{a}] {self.opciones_dict[a]}\n'
        return menu_str
