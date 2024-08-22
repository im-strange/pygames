import pygame

screen = None
block_size = None

def setup(screen_var, block_size_var):
    global screen, block_size
    screen = screen_var
    block_size = block_size_var

class I_SHAPE:
    def __init__(self):
        self.color = "skyblue"
        self.x, self.y = block_size * 7, block_size

    def draw(self):
        self.body = [
            pygame.Rect(self.x, self.y, block_size, block_size),
            pygame.Rect(self.x, self.y + block_size, block_size, block_size),
            pygame.Rect(self.x, self.y + block_size * 2, block_size, block_size)
        ]
        for block in self.body:
            pygame.draw.rect(screen, self.color, block)
        self.y += block_size

class L_SHAPE:
    def __init__(self):
        self.color = "orange"
        self.x, self.y = block_size * 7, block_size

    def draw(self):
        self.body = [
            pygame.Rect(self.x, self.y, block_size, block_size),
            pygame.Rect(self.x, self.y + block_size, block_size, block_size),
            pygame.Rect(self.x, self.y + block_size * 2, block_size, block_size),
            pygame.Rect(self.x + block_size, self.y + block_size * 2, block_size, block_size)
        ]
        for block in self.body:
            pygame.draw.rect(screen, self.color, block)
        self.y += block_size

class J_SHAPE:
    def __init__(self):
        self.color = "pink"
        self.x, self.y = block_size * 7, block_size

    def draw(self):
        self.body = [
            pygame.Rect(self.x, self.y, block_size, block_size),
            pygame.Rect(self.x, self.y + block_size, block_size, block_size),
            pygame.Rect(self.x, self.y + block_size * 2, block_size, block_size),
            pygame.Rect(self.x - block_size, self.y + block_size * 2, block_size, block_size)
        ]
        for block in self.body:
            pygame.draw.rect(screen, self.color, block)
        self.y += block_size