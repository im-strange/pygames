import pygame
import random
import math
import sys

pygame.init()
pygame.display.set_caption("Flappy Bird")

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BG_COLOR = pygame.Color("grey12")
FPS = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

class Bird:
    def __init__(self):
        self.color = "#dbae58"
        self.radius = 20
        self.x = self.radius
        self.y = SCREEN_HEIGHT - self.radius
        self.power = 40
        self.gravity = 20
        self.vx = 0
        self.vy = 0
        self.time = 1 / FPS

    def draw(self):
        pygame.draw.circle(screen, "white", (self.x, self.y), self.radius)
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius - 4)

    def update(self):
        self.vy += self.gravity * self.time
        self.y += (self.vy * self.time) + (0.5 * self.gravity * (self.time ** 2))

        # handle wall collision
        if self.y >= SCREEN_HEIGHT - self.radius:
            self.y = SCREEN_HEIGHT - self.radius

    def jump(self):
        self.y -= self.power

bird = Bird()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.jump()

    screen.fill(BG_COLOR)

    bird.draw()
    bird.update()

    pygame.display.update()
    clock.tick(FPS)