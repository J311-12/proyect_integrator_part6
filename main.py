import os
import random
import readchar
import functools
from mapas import obtener_mapa_aleatorio

class Juego:
    def __init__(self, mapa, inicio, fin):
        self._mapa = mapa
        self._inicio = inicio
        self._fin = fin

    def __str__(self):
        return f"Mapa:\n{self._mapa}\nInicio: {self._inicio}\nFin: {self._fin}"

    def _es_movimiento_valido(self, x, y):
        if 0 <= x < len(self._mapa) and 0 <= y < len(self._mapa[0]):
            return self._mapa[x][y] != "#"
        return False

    def mover(self, direccion):
        x, y = self._inicio
        if direccion == "w" and self._es_movimiento_valido(x - 1, y):
            x -= 1
        elif direccion == "s" and self._es_movimiento_valido(x + 1, y):
            x += 1
        elif direccion == "a" and self._es_movimiento_valido(x, y - 1):
            y -= 1
        elif direccion == "d" and self._es_movimiento_valido(x, y + 1):
            y += 1

        self._inicio = (x, y)

        if self._inicio == self._fin:
            return True

        return False

    def jugar(self):
        while True:
            print(self)
            print("Presione 'w' para arriba, 's' para abajo, 'a' para izquierda, 'd' para derecha")
            direccion = readchar.readkey().lower()
            if self.mover(direccion):
                print("¡Has llegado al final!")
                break

if __name__ == "__main__":
    # Obtenemos la ruta completa del archivo utilizando os.path.join
    ruta_archivo = os.path.join(os.path.dirname(__file__), "mapas.txt")

    # Obtener mapa aleatorio desde el archivo "mapas.py"
    mapa_ejemplo = obtener_mapa_aleatorio()

    # Creando una instancia del juego con el mapa de ejemplo
    juego = Juego(mapa_ejemplo["mapa"], mapa_ejemplo["inicio"], mapa_ejemplo["fin"])
    juego.jugar()
