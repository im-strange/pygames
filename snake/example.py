import pygame
import sys
import random

pygame.init()
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 500
BLOCK_SIZE = 25

screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
pygame.display.set_caption("snake")
clock = pygame.time.Clock()

class Snake:
    def __init__(self):
        self.x, self.y = BLOCK_SIZE, BLOCK_SIZE
        self.x_dir = 1
        self.y_dir = 0
        self.body = [pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)]
        self.head = pygame.Rect(self.x - BLOCK_SIZE, self.y, BLOCK_SIZE, BLOCK_SIZE)
        self.dead = False

    def update(self):
        global apple
        for square in self.body:
            if self.head.x == square.x and self.head.y == square.y:
                self.dead = True
            if self.head.x not in range(0, SCREEN_WIDTH) or self.head.y not in range(0, SCREEN_HEIGHT):
                self.dead = True

        if self.dead:
            self.x, self.y = BLOCK_SIZE, BLOCK_SIZE
            self.x_dir = 1
            self.y_dir = 0
            self.body = [pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)]
            self.head = pygame.Rect(self.x - BLOCK_SIZE, self.y, BLOCK_SIZE, BLOCK_SIZE)
            self.dead = False
            apple = Apple()

        self.body.append(self.head)
        for i in range(0, len(self.body) - 1):
            self.body[i].x, self.body[i].y = self.body[i+1].x, self.body[i+1].y

        self.head.x += self.x_dir * BLOCK_SIZE
        self.head.y += self.y_dir * BLOCK_SIZE
        self.body.remove(self.head)

class Apple:
    def __init__(self):
        self.x = int(random.randint(0, SCREEN_WIDTH) / BLOCK_SIZE) * BLOCK_SIZE
        self.y = int(random.randint(0, SCREEN_HEIGHT) / BLOCK_SIZE) * BLOCK_SIZE
        self.rect = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)

    def update(self):
        pygame.draw.rect(screen, "red", self.rect)
def draw_grid():
    for x in range(0, SCREEN_HEIGHT, BLOCK_SIZE):
        for y in range(0, SCREEN_WIDTH, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, "#3c3c3b", rect, 1)

draw_grid()
snake = Snake()
apple = Apple()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                snake.y_dir = 1
                snake.x_dir = 0
            elif event.key == pygame.K_UP:
                snake.y_dir = -1
                snake.x_dir = 0
            elif event.key == pygame.K_RIGHT:
                snake.y_dir = 0
                snake.x_dir = 1
            if event.key == pygame.K_LEFT:
                snake.y_dir = 0
                snake.x_dir = -1

    snake.update()
    screen.fill("black")
    apple.update()
    draw_grid()
    pygame.draw.rect(screen, "green", snake.head)

    for square in snake.body:
        pygame.draw.rect(screen, "green", square)

    if snake.head.x == apple.x and snake.head.y == apple.y:
        snake.body.append(pygame.Rect(square.x, square.y, BLOCK_SIZE, BLOCK_SIZE))
        apple = Apple()

    pygame.display.update()
    clock.tick(10)

