import pygame
import random
import sys

# Constants
WIDTH, HEIGHT = 400, 600
LANE_WIDTH = WIDTH // 3
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (50, 50, 50)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

class Motorcycle:
    def __init__(self):
        self.width = 40
        self.height = 70
        self.lane = 1  # Start in the middle lane (0, 1, 2)
        self.x = self.calculate_x()
        self.y = HEIGHT - 100
        self.color = BLUE

    def calculate_x(self):
        return (self.lane * LANE_WIDTH) + (LANE_WIDTH // 2) - (self.width // 2)

    def move_left(self):
        if self.lane > 0:
            self.lane -= 1
            self.x = self.calculate_x()

    def move_right(self):
        if self.lane < 2:
            self.lane += 1
            self.x = self.calculate_x()

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        # Simple motorcycle details
        pygame.draw.rect(screen, BLACK, (self.x + 5, self.y - 10, 30, 20)) # Helmet

class Car:
    def __init__(self, speed):
        self.width = 50
        self.height = 90
        self.lane = random.randint(0, 2)
        self.x = (self.lane * LANE_WIDTH) + (LANE_WIDTH // 2) - (self.width // 2)
        self.y = -self.height
        self.speed = speed
        self.color = RED

    def update(self):
        self.y += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Moto Highway Dodge")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 30)

    moto = Motorcycle()
    cars = []
    score = 0
    car_speed = 5
    spawn_timer = 0
    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if not game_over:
                    if event.key == pygame.K_LEFT:
                        moto.move_left()
                    if event.key == pygame.K_RIGHT:
                        moto.move_right()
                else:
                    if event.key == pygame.K_r:
                        main() # Restart

        if not game_over:
            # Spawn cars
            spawn_timer += 1
            if spawn_timer > 60: # Every ~1 second
                cars.append(Car(car_speed))
                spawn_timer = 0
                # Increase speed slightly over time
                car_speed += 0.1

            # Update cars
            for car in cars[:]:
                car.update()
                # Check collision
                moto_rect = pygame.Rect(moto.x, moto.y, moto.width, moto.height)
                car_rect = pygame.Rect(car.x, car.y, car.width, car.height)
                if moto_rect.colliderect(car_rect):
                    game_over = True

                # Remove off-screen cars and update score
                if car.y > HEIGHT:
                    cars.remove(car)
                    score += 1

        # Drawing
        screen.fill(GRAY)
        
        # Draw road lanes
        for i in range(1, 3):
            pygame.draw.line(screen, WHITE, (i * LANE_WIDTH, 0), (i * LANE_WIDTH, HEIGHT), 5)
        
        # Draw dashed lines (moving effect could be added, but keeping it basic)
        
        moto.draw(screen)
        for car in cars:
            car.draw(screen)

        # Draw Score
        score_text = font.render(f"Puntuación: {score}", True, YELLOW)
        screen.blit(score_text, (10, 10))

        if game_over:
            msg = font.render("GAME OVER! Presiona R para reiniciar", True, WHITE)
            screen.blit(msg, (WIDTH // 2 - msg.get_width() // 2, HEIGHT // 2))

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
