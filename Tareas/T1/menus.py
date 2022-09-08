from email import header
from typing import List

class Menu():
    def __init__(self, header: str, ancho: int, opciones: List[str]) -> None:
        self.header = header
        self.ancho = ancho
        self.espacio_izq = int((self.ancho - len(self.header)) / 2)
        self.espacio_der = self.espacio_izq + 1
        self.opciones = opciones
        self.opciones_dict = {a: self.opciones[a] for a in range(len(self.opciones))}
    
    def __str__(self) -> str:
        menu_str = ' ' * self.espacio_izq + self.header + ' ' * self.espacio_der + '\n' \
                 + '-' * self.ancho + '\n'
        for a in range(len(self.opciones)):
            menu_str += f'[{a}] {self.opciones_dict[a]}\n'
        menu_str += '\n'
        return menu_str