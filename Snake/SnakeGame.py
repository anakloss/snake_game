import pygame, sys
from pygame.locals import *
from random import randint
import time
from clases import *


class SnakeGame:
    'Clase para armar la estructura del juego'

    ancho = 875
    alto = 680
    jugador = 0
    comida = 0
    puntaje = 0

    # Colores
    cesped = (117, 181, 92)
    objeto = (30, 40, 30)
    objeto2 = (65, 140, 100)
    objetoClaro = (80, 115, 80)

    def __init__(self):
        self.corriendo = True
        self.ventana = None
        self.juego = Juego()
        self.mapa = Mapa()
        self.jugador = Serpiente(3)
        self.comida = Comida(5, 5)
        self.puntaje = 0

    # Inicializa lo necesario para la ventana del juego
    def on_init(self):
        pygame.init()
        self.corriendo = True

        # Crea la ventana con el alto y ancho especificado
        self.ventana = pygame.display.set_mode(
            (self.ancho, self.alto), pygame.HWSURFACE)

        # Se le da un titulo a la ventana
        pygame.display.set_caption("Snake Game")
        self.imgSnakeInicio = pygame.image.load("imagenes/snake_header.png")

        # Define la fuentes deseadas
        fuenteTitulo = pygame.font.Font("PressStart2P.ttf", 60)
        self.fuenteCred = pygame.font.Font("PressStart2P.ttf", 15)
        fuenteMenu = pygame.font.Font("PressStart2P.ttf", 25)
        self.fuentePuntaje = pygame.font.Font("PressStart2P.ttf",
            30, bold=True)

        # Render para las fuentes
        self.textoTitulo = fuenteTitulo.render("Snake Game",
            True, self.objeto2)
        self.creditos = self.fuenteCred.render("Creditos: Ana Kloss",
            True, self.objeto)
        self.textoJugar = fuenteMenu.render("Jugar", True, self.objeto)
        self.textoTop10 = fuenteMenu.render("Puntajes", True, self.objeto)
        self.textoSalir = fuenteMenu.render("Salir", True, self.objeto)
        self.instruccionMenu = self.fuenteCred.render(
            "Presione Z para seleccionar", True, self.objeto)
        self.instruccionMenu2 = self.fuenteCred.render(
            "Presione X para volver al menu", True, self.objeto)
        self.textoFin = fuenteMenu.render("Fin del juego", True, self.objeto)

        self.tituloTop10 = fuenteMenu.render("Mejores puntajes", True,
            self.objeto)

    # Funcion para actualizar la pantalla continuamente
    def on_bucle(self):
        puntaje = Puntaje()
        self.jugador.actualizar()
        self.textoPuntaje = self.fuentePuntaje.render("Puntaje: %s" %
            self.puntaje, True, (0, 0, 0), self.objeto2)

        # la serpiente come la comida?
        for i in range(0, self.jugador.longitud):
            if self.juego.is_colision(self.comida.x, self.comida.y,
                self.jugador.x[i], self.jugador.y[i], 44):
                self.comida.x = randint(2, 9) * 44
                self.comida.y = randint(2, 9) * 44
                self.puntaje += self.comida.frutas[self.comida.i]['puntaje']

                self.comida.i = randint(0, 4)
                self.jugador.longitud += 1

        # la serpiente choca con ella misma?
        for i in range(2, self.jugador.longitud):
            if self.juego.is_colision(self.jugador.x[0], self.jugador.y[0],
                self.jugador.x[i], self.jugador.y[i], 40):
                self.corriendo = False

            # la serpiente choca con la pared?
            if self.juego.is_colision_pared(self.jugador.x[0],
                    self.jugador.y[0]):
                self.corriendo = False

        if not self.corriendo:
            puntaje.guardar_puntaje(self.puntaje)

    # Funcion para pantalla inicial
    def on_pantalla_ini(self, seleccion):
        self.ventana.fill((self.cesped))

        if seleccion == 0:
            # Jugar
            pygame.draw.rect(self.ventana, self.objetoClaro,
                (110, 240, 220, 50))
        elif seleccion == 1:
            # puntajes
            pygame.draw.rect(self.ventana, self.objetoClaro,
                (110, 290, 220, 50))
        elif seleccion == 2:
            # salir
            pygame.draw.rect(self.ventana, self.objetoClaro,
                (110, 340, 220, 50))

        self.ventana.blit(self.imgSnakeInicio, (0, 0))
        self.ventana.blit(self.textoTitulo, (230, 150))
        self.ventana.blit(self.creditos, (500, 220))
        self.ventana.blit(self.textoJugar, (120, 250))
        self.ventana.blit(self.textoTop10, (120, 300))
        self.ventana.blit(self.textoSalir, (120, 350))
        self.ventana.blit(self.instruccionMenu, (30, 650))
        pygame.display.flip()

    def on_puntajes(self):
        puntaje = Puntaje()
        puntajes_leidos = puntaje.obtener_puntaje()

        self.ventana.fill((self.cesped))
        self.ventana.blit(self.tituloTop10, (120, 100))
        puntaje.mostrar_puntaje(puntajes_leidos, self.ventana, self.objeto)
        self.ventana.blit(self.instruccionMenu2, (250, 600))
        pygame.display.flip()

    # Funcion para dibujar en la pantalla
    def on_hacer(self):
        self.ventana.fill((self.cesped))
        self.mapa.dibujar(self.ventana)
        self.jugador.dibujar(self.ventana)
        self.comida.dibujar(self.ventana)
        self.ventana.blit(self.textoPuntaje, (10, 5))

        if self.corriendo == False:
            self.ventana.blit(self.textoFin, (250, 150))
            self.ventana.blit(self.instruccionMenu2, (250, 600))

        pygame.display.flip()

    def on_limpiar(self):
        pygame.quit()
        sys.exit()

    def on_accion_serpiente(self):
        # Se dan las ordenes con las flechas para mover la serpiente
        # Se cierra al presionar 'esc'
        while self.corriendo:
            pygame.event.pump()
            keys = pygame.key.get_pressed()

            if (keys[K_LEFT]):
                self.jugador.movimientoIzquirda()
            if (keys[K_RIGHT]):
                self.jugador.movimientoDerecha()
            if (keys[K_UP]):
                self.jugador.movimientoArriba()
            if (keys[K_DOWN]):
                self.jugador.movimientoAbajo()
            if (keys[K_ESCAPE]):
                self.corriendo = False
                pygame.quit()
                sys.exit()

            self.on_bucle()
            self.on_hacer()

            # Tiempo de movimiento de la serpiente
            time.sleep(50.0 / 1000.0);

    # Funcion para ejecutar el juego
    def on_ejecutar(self):
        # Inicializa
        self.on_init()

        fase = 0
        selecMenu = 0

        while True:
            if fase == 0:
                self.on_pantalla_ini(selecMenu)
            elif fase == 1:
                self.on_accion_serpiente()
            elif fase == 2:
                self.on_puntajes()
            elif fase == 3:
                self.on_limpiar()

            for evento in pygame.event.get():
                if evento.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == KEYDOWN:
                    if fase == 0:
                        if evento.key == K_UP:
                            selecMenu -= 1
                        elif evento.key == K_DOWN:
                            selecMenu += 1

                        if evento.key == K_z:
                            if selecMenu == 0:
                                # Jugar
                                fase = 1
                            elif selecMenu == 1:
                                # Puntajes
                                fase = 2
                            elif selecMenu == 2:
                                # Salir
                                fase = 3

                    elif fase == 1:
                        if evento.key == pygame.K_x:
                            fase = 0
                            self.on_init()
                    elif fase == 2:
                        if evento.key == pygame.K_x:
                            fase = 0
                            self.on_init()

        self.on_limpiar()

if __name__ == "__main__":
    snakeGame = SnakeGame()
    snakeGame.on_ejecutar()
