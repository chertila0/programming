import math
import pygame
from pygame.locals import *

# Параметры окна
WIDTH = 800
HEIGHT = 600
FPS = 60

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Gear:
    def __init__(self, x, y, radius, teeth):
        self.x = x
        self.y = y
        self.radius = radius
        self.teeth = teeth
        self.angle = 0

    def draw(self, screen):
        # Нарисуем окружность
        pygame.draw.circle(screen, BLACK, (int(self.x), int(self.y)), self.radius, 1)

        # Нарисуем зубы шестеренки
        for i in range(self.teeth):
            angle = i * 2 * math.pi / self.teeth + self.angle
            x_tooth = self.x + self.radius * math.cos(angle)
            y_tooth = self.y + self.radius * math.sin(angle)
            pygame.draw.line(screen, BLACK, (x_tooth, y_tooth),
                             (x_tooth + 10 * math.cos(angle), y_tooth + 10 * math.sin(angle)))

    def update(self, dt):
        self.angle += 0.001 * dt  # Скорость вращения можно настроить

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    gear1 = Gear(WIDTH // 2, HEIGHT // 2, 100, 20)  # Центральная шестерня
    gear2 = Gear(gear1.x + gear1.radius + 50, gear1.y, 75, 15)  # Шестеренка справа

    running = True
    while running:
        dt = clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        # Обновление состояния шестеренок
        gear1.update(dt)
        gear2_angle = gear1.angle * gear1.teeth / gear2.teeth
        gear2.angle = gear2_angle

        # Очистка экрана
        screen.fill(WHITE)

        # Отрисовка шестеренок
        gear1.draw(screen)
        gear2.draw(screen)

        # Обновление экрана
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()