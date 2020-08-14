import pygame

class Juego:
    'Clase para algunas funciones del juego'

    # Funcion para saber si choca con alguna parte del cuerpo
    def is_colision(self,x1,y1,x2,y2,bsize):
        if x1 >= x2 and x1 <= x2 + bsize:
            if y1 >= y2 and y1 <= y2 + bsize:
                return True
        return False

    # Funcion para saber si choca con alguna pared del borde de la ventana
    def is_colision_pared(self, x, y):
        if x > 40 and x < 800:
            if y > 40 and y < 600:
                return False
        return True
