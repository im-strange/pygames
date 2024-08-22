import pygame
import random
import sys
from shapes import *

# initialize
pygame.init()
pygame.display.set_caption("Tetris")

# constants
screen_width, screen_height = 600, 600
bg_color = pygame.Color("grey12")
fps = 5
block_size = 25

# screen
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

setup(
    screen_var = screen,
    block_size_var = block_size
)

# main loop
def main():
    shapes = [I_SHAPE(), L_SHAPE(), J_SHAPE()]
    random_shape = random.choice(shapes)
    blocks = []

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # background
        screen.fill(bg_color)

        # shapes
        random_shape.draw()

        # update
        pygame.display.update()
        clock.tick(fps)

if __name__ == "__main__":
    main()