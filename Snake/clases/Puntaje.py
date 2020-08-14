import pygame
from pygame.locals import *

class Puntaje:
    'Puntajes'

    def guardar_puntaje(self, puntajes):
        #Guardar el nuevo puntaje en el archivo
        f = open('archivos/resultados.txt', 'a')
        f.write(str(puntajes) + '\n')
        f.close()

    def obtener_puntaje(self):
        try:
            # Abrir el archivo de puntajes
            f = open('archivos/resultados.txt', 'r')
            puntajes = []
            for line in f:
                puntajes.append(int(line))
            puntajes.sort(reverse=True)
            f.close()
            return puntajes
        except IOError:
            pass

    def mostrar_puntaje(self, puntajes, ventana, color):
        # Muestra los 15 mejores puntajes en el submenu Puntajes
        ancho = 150
        fuenteTexto = pygame.font.Font(None, 30)

        top15 = []
        i = 1
        if puntajes:
            for puntaje in puntajes:
                if i <= 15:
                    top15.append({
                        'pos': str(i),
                        'puntos': str(puntaje),
                    })
                i += 1
            for p in top15:
                texto = fuenteTexto.render(p['pos'] + ' ****** ' \
                    + p['puntos'], True, color)
                ventana.blit(texto, (150, ancho))
                ancho += 30
        else:
            texto = fuenteTexto.render('No hay puntajes todavía', True, color)
            ventana.blit(texto, (150, ancho))
