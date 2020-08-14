import pygame
from pygame.locals import *

class Serpiente:
    'Clase para Serpiente'

    x = [500]  # Posicion x, y
    y = [300]
    paso = 44  # Velocidad de movimiento
    direccion = 0
    longitud = 3

    cantMaxLargo = 2
    cantLargo = 0

    def __init__(self, longitud):
        # Se cargan las imagenes para formar la serpiente
        self.imagenSnakeCab = pygame.image.load(
            "imagenes/snake/snake_cab_d.png")
        self.imagenSnake = pygame.image.load("imagenes/snake/snake.png")
        self.longitud = longitud

        # Alarga la serpiente
        for i in range(0, 2000):
            self.x.append(-100)
            self.y.append(-100)

        # Posicion inicial
        self.x[1] = 1*44
        self.x[2] = 2*44

    def actualizar(self):
        self.cantLargo += 1
        if self.cantLargo > self.cantMaxLargo:

            # actualizar posicion anterior
            for i in range(self.longitud - 1, 0, -1):
                self.x[i] = self.x[i-1]
                self.y[i] = self.y[i-1]

            # actualizar posicion de la cabeza
            if self.direccion == 0:
                self.x[0] += self.paso
            if self.direccion == 1:
                self.x[0] -= self.paso
            if self.direccion == 2:
                self.y[0] -= self.paso
            if self.direccion == 3:
                self.y[0] += self.paso

            self.cantLargo = 0


    def movimientoDerecha(self):
        self.imagenSnakeCab = pygame.image.load(
            "imagenes/snake/snake_cab_d.png")
        self.direccion = 0

    def movimientoIzquirda(self):
        self.imagenSnakeCab = pygame.image.load(
            "imagenes/snake/snake_cab_i.png")
        self.direccion = 1

    def movimientoArriba(self):
        self.imagenSnakeCab = pygame.image.load(
            "imagenes/snake/snake_cab_ar.png")
        self.direccion = 2

    def movimientoAbajo(self):
        self.imagenSnakeCab = pygame.image.load(
            "imagenes/snake/snake_cab_ab.png")
        self.direccion = 3

    def dibujar(self, superficie):
        superficie.blit(self.imagenSnakeCab, (self.x[0], self.y[0]))
        for i in range(1, self.longitud):
            superficie.blit(self.imagenSnake, (self.x[i], self.y[i]))
