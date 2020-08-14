import pygame
from pygame.locals import *
import random

class Comida:
    'Clase para comida'

    x = 0  # Posicion x, y
    y = 0
    i = 0
    frutas = {}

    def __init__(self, x, y):
        # Se cargan las imagenes de las distinas comidas
        self.imgManzana = pygame.image.load("imagenes/comida/manzana.png")
        self.imgUvas = pygame.image.load("imagenes/comida/uvas.png")
        self.imgFrutilla = pygame.image.load("imagenes/comida/frutilla.png")
        self.imgNaranja = pygame.image.load("imagenes/comida/naranja.png")
        self.imgBanana = pygame.image.load("imagenes/comida/banana.png")

        # Coordenadas de la comida
        self.x = x * 44
        self.y = y * 44

        self.i = 0

        '''Diccionario de las comidas, que a su vez contiene un diccionario
        con la imagen y el puntaje asignado'''
        punto_fruta = random.randint(-500, 500)
        self.frutas = {
            0: {'img': self.imgManzana, 'puntaje': punto_fruta},
            1: {'img': self.imgUvas, 'puntaje': punto_fruta},
            2: {'img': self.imgFrutilla, 'puntaje': punto_fruta},
            3: {'img': self.imgNaranja, 'puntaje': punto_fruta},
            4: {'img': self.imgBanana, 'puntaje': punto_fruta}
        }

    def dibujar(self, superficie):
        superficie.blit(self.frutas[self.i]['img'], (self.x, self.y))
