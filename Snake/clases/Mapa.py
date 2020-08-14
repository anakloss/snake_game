import pygame
from pygame.locals import *

class Mapa:
    'Clase para leer y crear mapa desde archivo txt'

    def __init__(self):
        # Se carga la imagen del bloque de la pared
        self.imagenBloque = pygame.image.load("imagenes/bloque.png")
        self.rect_bloque = self.imagenBloque.get_rect()

        # Abre el archivo para crear el mapa
        self.mapa = open('archivos/mapa.txt', 'r')
        self.mapa = self.mapa.readlines()

        # Quita el ultimo caracter
        for i in range(len(self.mapa)):
            self.mapa[i] = self.mapa[i][:-1]

        for i in range(len(self.mapa)):
            self.mapa[i] = self.listarCadena(self.mapa[i])

        self.fila = len(self.mapa)
        self.columna = len(self.mapa[0])

    # Covierte una cadena en una lista.
    def listarCadena(self, cadena):
        lista = []
        for i in range(len(cadena)):
            if cadena[i] == ".":
                lista.append(0)     # Espacios donde no van bloques
            if cadena[i] == "#":
                lista.append(1)     # Donde si van bloques
        return lista

    def dibujar(self, superficie):
        for f in range(self.fila):
            for c in range(self.columna):
                if self.mapa[f][c] == 1:
                    superficie.blit(self.imagenBloque, (self.rect_bloque.w*c,
                        self.rect_bloque.h*f))
