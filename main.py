import os
import random
import readchar
import functools
from mapas import mapas

class Juego:
    def __init__(self, mapa, inicio, fin):
        self.mapa = mapa
        self.inicio = inicio
        self.fin = fin

    def __str__(self):
        return f"Mapa:\n{self.mapa}\nInicio: {self.inicio}\nFin: {self.fin}"

    def mover(self, direccion):
        x, y = self.inicio
        if direccion == "w":
            x -= 1
        elif direccion == "s":
            x += 1
        elif direccion == "a":
            y -= 1
        elif direccion == "d":
            y += 1

        if self.mapa[x][y] != "#":
            self.inicio = (x, y)

        if self.inicio == self.fin:
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

class JuegoArchivo(Juego):
    def __init__(self, mapa):
        super().__init__(mapa["mapa"], mapa["inicio"], mapa["fin"])

def convertir_laberinto_a_matriz(laberinto_cadena):
    return list(map(list, laberinto_cadena.split('\n')))

def leer_mapa_desde_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()
    return functools.reduce(lambda x, y: x + y, lineas)

if __name__ == "__main__":
    # Obtenemos la ruta completa del archivo utilizando os.path.join
    ruta_archivo = os.path.join(os.path.dirname(__file__), "mapas.txt")

    # Leer el mapa desde el archivo y cargar las coordenadas
    mapa_cadena = leer_mapa_desde_archivo(ruta_archivo)

    # Convertir el laberinto de cadena a matriz
    mapa_ejemplo = convertir_laberinto_a_matriz(mapa_cadena)

    # Creando una instancia del juego con el mapa de ejemplo
    juego = Juego(mapa_ejemplo, (2, 1), (9, 1))
    juego.jugar()

    # Creando una instancia del juego leyendo un mapa desde un archivo
    juego_archivo = JuegoArchivo(mapas[0])  # Utilizamos el primer mapa de la lista mapas
    juego_archivo.jugar()
