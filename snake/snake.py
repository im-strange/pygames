import pygame
import random
import math
import sys

# initialize
pygame.init()
pygame.display.set_caption("Snake")

# constants
screen_width, screen_height = 500, 500
bg_color = pygame.Color("grey12")
fps = 10
block_size = 20

# classes
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

class Snake:
    def __init__(self):
        self.color = "green"
        self.block_size = block_size
        self.x = block_size
        self.y = block_size
        self.xdir = 1
        self.ydir = 0
        self.body = [
            pygame.Rect(self.x, self.y, self.block_size, self.block_size),
        ]
        self.head = pygame.Rect(self.x + block_size, self.y, self.block_size, self.block_size)

    def update(self):
        self.body.append(self.head)
        for block in self.body:
            pygame.draw.rect(screen, self.color, block)

        for i in range(0, len(self.body) - 1):
            self.body[i].x, self.body[i].y = self.body[i+1].x, self.body[i+1].y

        self.head.x += self.xdir * self.block_size
        self.head.y += self.ydir * self.block_size
        self.body.remove(self.head)

        # handle wall collision
        if self.head.x > screen_width:
            self.head.x = 0
        if self.head.x < 0:
            self.head.x = screen_width
        if self.head.y > screen_height:
            self.head.y = 0
        if self.head.y < 0:
            self.head.y = screen_height


class Apple:
    def __init__(self):
        self.color = "red"
        self.x = int(random.randint(0, screen_width) / block_size) * block_size
        self.y = int(random.randint(0, screen_height) / block_size) * block_size
        self.rect = pygame.Rect(self.x, self.y, block_size, block_size)
        print(self.x, self.y)

    def update(self):
        pygame.draw.rect(screen, self.color, self.rect)

#main loop
def main():
    snake = Snake()
    apple = Apple()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    snake.ydir = 1
                    snake.xdir = 0
                if event.key == pygame.K_UP:
                    snake.ydir = -1
                    snake.xdir = 0
                if event.key == pygame.K_LEFT:
                    snake.xdir = -1
                    snake.ydir = 0
                if event.key == pygame.K_RIGHT:
                    snake.xdir = 1
                    snake.ydir = 0

        # background color
        screen.fill(bg_color)

        # snake
        apple.update()
        snake.update()

        # when apple was eaten
        if snake.head.x == apple.x and snake.head.y == apple.y:
            snake.body.append(pygame.Rect(snake.body[-1].x, snake.body[-1].y, block_size, block_size))
            apple = Apple()

        # update screen
        pygame.display.update()
        clock.tick(fps)

if __name__ == "__main__":
    main()