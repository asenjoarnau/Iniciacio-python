import pygame
import random
import sys

# Inicializar Pygame
pygame.init()

# Configuraciones de la pantalla
ANCHO = 300
ALTO = 600
ANCHO_CARRIL = ANCHO // 3
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Moto vs Coches")
reloj = pygame.time.Clock()

# Colores
GRIS = (85, 85, 85)
BLANCO = (255, 255, 255)
CIAN = (0, 255, 255) # Color de nuestra moto
ROJO = (255, 0, 0)   # Color de los coches enemigos

# Variables del Jugador (Moto)
jugador_ancho = 40
jugador_alto = 70
carril_jugador = 1  # 0: Izq, 1: Centro, 2: Der
jugador_y = ALTO - 100

# Variables del Juego
puntuacion = 0
velocidad_enemigo = 5
enemigos = []
fuente = pygame.font.SysFont(None, 36)

def generar_enemigo():
    carril = random.randint(0, 2)
    # Centrar el coche en el carril elegido
    x = (carril * ANCHO_CARRIL) + (ANCHO_CARRIL // 2) - (jugador_ancho // 2)
    y = -100
    enemigos.append(pygame.Rect(x, y, jugador_ancho, jugador_alto))

# Bucle principal del juego
jugando = True
while jugando:
    # 1. Manejo de Eventos (Controles)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False
            pygame.quit()
            sys.exit()
        
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT and carril_jugador > 0:
                carril_jugador -= 1
            if evento.key == pygame.K_RIGHT and carril_jugador < 2:
                carril_jugador += 1

    # Calcular posición X exacta del jugador según el carril
    jugador_x = (carril_jugador * ANCHO_CARRIL) + (ANCHO_CARRIL // 2) - (jugador_ancho // 2)
    rect_jugador = pygame.Rect(jugador_x, jugador_y, jugador_ancho, jugador_alto)

    # 2. Lógica y Movimiento
    # Generar enemigos aleatoriamente
    if random.random() < 0.02: 
        generar_enemigo()

    # Mover enemigos y contar puntos
    for enemigo in enemigos[:]:
        enemigo.y += velocidad_enemigo
        
        # Si el coche enemigo sale de la pantalla por abajo, lo esquivaste
        if enemigo.y > ALTO:
            enemigos.remove(enemigo)
            puntuacion += 1
            # Aumentar un poco la dificultad cada 5 puntos
            if puntuacion % 5 == 0:
                velocidad_enemigo += 0.5

        # Detección de colisión
        if rect_jugador.colliderect(enemigo):
            print(f"¡Game Over! Puntuación final: {puntuacion}")
            jugando = False

    # 3. Dibujar en pantalla (Gráficos)
    pantalla.fill(GRIS) # Fondo de la carretera

    # Dibujar líneas de los carriles
    pygame.draw.line(pantalla, BLANCO, (ANCHO_CARRIL, 0), (ANCHO_CARRIL, ALTO), 2)
    pygame.draw.line(pantalla, BLANCO, (ANCHO_CARRIL * 2, 0), (ANCHO_CARRIL * 2, ALTO), 2)

    # Dibujar jugador (Moto CIAN)
    pygame.draw.rect(pantalla, CIAN, rect_jugador)

    # Dibujar enemigos (Coches ROJOS)
    for enemigo in enemigos:
        pygame.draw.rect(pantalla, ROJO, enemigo)

    # Dibujar puntuación
    texto_puntos = fuente.render(f"Puntos: {puntuacion}", True, BLANCO)
    pantalla.blit(texto_puntos, (10, 10))

    # Actualizar pantalla y controlar los FPS
    pygame.display.flip()
    reloj.tick(60) # 60 cuadros por segundo

pygame.quit()