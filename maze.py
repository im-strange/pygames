import pygame
import random
import sys

pygame.init()
pygame.display.set_caption("maze")

SCREEN_WIDTH, SCREEN_HEIGHT, WALL_WIDTH, WALL_HEIGHT = 500, 500, 25, 25
BG_COLOR, MAZE_COLOR, PLAYER_COLOR, END_COLOR = pygame.Color("grey12"), "#3c3c3b", (200, 200, 200), "green"
PELLET_COLOR = "lightblue"
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

def generate_cells(rows, cols):
    cells = []
    for row in range(rows):
        sub = []
        for col in range(cols):
            num = random.randint(0, 4)
            sub.append(num)
        cells.append(sub)

    cells[0][0] = 0
    return cells

def draw_maze(cells):
    rects = []
    pellets = []
    for row in range(len(cells)):
        for col in range(len(cells)):
            item = cells[row][col]
            x_pos = col * WALL_WIDTH
            y_pos = row * WALL_WIDTH
            if item == 1:
                block = pygame.Rect(x_pos, y_pos, WALL_WIDTH, WALL_HEIGHT)
                rects.append(block)
                pygame.draw.rect(screen, MAZE_COLOR, block)
            elif item == 4:
                pellet = pygame.Rect(x_pos, y_pos, WALL_WIDTH, WALL_HEIGHT)
                index = (row, col)
                pellets.append((pellet, index))
                pygame.draw.circle(screen, PELLET_COLOR, pellet.center, 4)
    return rects, pellets

cells = generate_cells(WALL_HEIGHT, WALL_WIDTH)
rects, pellets = draw_maze(cells)

player_speed = 3
player_radius = 10
player_x, player_y = player_radius/2, player_radius/2
player_width, player_height = 15, 15
player_xdir, player_ydir = 0, 0

end_width, end_height = 25, 25
end_x, end_y = SCREEN_WIDTH - end_width, SCREEN_HEIGHT - end_height
end_rect = pygame.Rect(end_x, end_y, end_width, end_height)

while True:
    player = pygame.Rect(player_x, player_y, player_width, player_height)
    keys = pygame.key.get_pressed()

    for rect in rects:
        if rect.colliderect(player):
            if keys[pygame.K_LEFT]:
                player_x = rect.right
                player_xdir = 0
            if keys[pygame.K_RIGHT]:
                player_x = rect.left - player_height
                player_xdir = 0
            if keys[pygame.K_UP]:
                player_y = rect.bottom
                player_ydir = 0
            if keys[pygame.K_DOWN]:
                player_y = rect.top - player_height
                player_ydir = 0

    for item in range(len(pellets)):
        pellet, index = pellets[item][0], pellets[item][1]
        if pellet.colliderect(player):
            cells[index[0]][index[1]] = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player_xdir = 1
            elif event.key == pygame.K_LEFT:
                player_xdir = -1
            elif event.key == pygame.K_UP:
                player_ydir = -1
            elif event.key == pygame.K_DOWN:
                player_ydir = 1
            print(player_x, player_y)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player_xdir = 0
            elif event.key == pygame.K_LEFT:
                player_xdir = 0
            elif event.key == pygame.K_UP:
                player_ydir = 0
            elif event.key == pygame.K_DOWN:
                player_ydir = 0
            print(player_x, player_y)

    player_x += player_xdir * player_speed
    player_y += player_ydir * player_speed

    if player_x >= SCREEN_WIDTH - player_width:
        player_x = SCREEN_WIDTH - player_width
    if player_x < 0:
        player_x = 0
    if player_y >= SCREEN_HEIGHT - player_width:
        player_y = SCREEN_HEIGHT - player_width
    if player_y < 0:
        player_y = 0

    screen.fill(BG_COLOR)
    draw_maze(cells)
    pygame.draw.circle(screen, PLAYER_COLOR, player.center, player_radius)
    pygame.draw.rect(screen, END_COLOR, end_rect)

    pygame.display.update()
    clock.tick(60)