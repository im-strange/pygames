import pygame
import random
import math
import sys

# initialize pygame
pygame.init()
pygame.display.set_caption("Pong")
pop_sound = pygame.mixer.Sound("pop-sound.mp3")

# constants
SCREEN_WIDTH, SCREEN_HEIGHT = 700, 500
BG_COLOR, LIGHT_GREY = pygame.Color("grey12"), (200, 200, 200)
FPS = 60

# screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# game rects
ball = pygame.Rect(SCREEN_WIDTH / 2 - 10, SCREEN_HEIGHT / 2 - 10, 20, 20)
opponent = pygame.Rect(0, SCREEN_HEIGHT / 2 - 70, 10, 140)
player = pygame.Rect(SCREEN_WIDTH - 10, SCREEN_HEIGHT / 2 - 70, 10, 140)

# add text
def add_text(text, position, size, color, bold=False, italic=False):
    font_size = size
    font = pygame.font.Font(None, font_size)
    font.set_italic(italic)
    font.set_bold(bold)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, position)

# score animation
class FallingScore:
    def __init__(self, ball_x, ball_y, x_dir=0):
        self.color = "#dbae58"
        self.x_dir = x_dir
        self.x = ball_x
        self.y = ball_y
        self.gravity = 1500
        self.power = 200
        self.angle = math.radians(45)
        self.vx = math.cos(self.angle) * self.power * self.x_dir
        self.vy = -math.sin(self.angle) * self.power
        self.time = 1 / FPS

    def fall(self):
        add_text("+1", (self.x, self.y), 40, self.color, bold=True)
        self.x += self.vx * self.time
        self.y += (self.vy * self.time) + (0.5 * self.gravity * self.time**2)
        self.vy += self.gravity * self.time

# main loop
def main():
    ball_vx = random.randint(4, 5)
    ball_vy = random.randint(4, 5)
    player_speed = 0
    opponent_speed = 20

    player_score = 0
    opponent_score = 0
    player_field_middle = SCREEN_WIDTH - SCREEN_WIDTH / 4
    opponent_field_middle = SCREEN_WIDTH / 4

    falling_scores = []
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    player_speed += 7
                if event.key == pygame.K_UP:
                    player_speed -= 7
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    player_speed -= 7
                if event.key == pygame.K_UP:
                    player_speed += 7

        # opponent
        if opponent.top < ball.top:
            opponent.top += opponent_speed
        if opponent.bottom > ball.bottom:
            opponent.bottom -= opponent_speed

        # controls
        player.y += player_speed

        # ball animation
        ball.x += ball_vx
        ball.y += ball_vy

        # handle wall
        if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
            ball_vy *= -1
            pop_sound.play()
        if ball.left <= 0 or ball.right >= SCREEN_WIDTH:
            game_over = True

        if player.top <= 0:
            player.top = 0
        if player.bottom >= SCREEN_HEIGHT:
            player.bottom = SCREEN_HEIGHT

        if opponent.top <= 0:
            opponent.top = 0
        if opponent.bottom >= SCREEN_HEIGHT:
            opponent.bottom = SCREEN_HEIGHT

        # handle collision
        if ball.colliderect(player):
            ball_vx *= -1
            player_score += 1
            score_object =  FallingScore(ball.x, ball.y, x_dir=-1)
            falling_scores.append(score_object)
            pop_sound.play()

        if ball.colliderect(opponent):
            ball_vx *= -1
            opponent_score += 1
            score_object = FallingScore(ball.x, ball.y, x_dir=1)
            falling_scores.append(score_object)
            pop_sound.play()

        # update background color
        screen.fill(BG_COLOR)

        # middle line
        pygame.draw.line(screen, "#6c757d", (SCREEN_WIDTH / 2, 0), (SCREEN_WIDTH / 2, SCREEN_HEIGHT), 5)

        # texts
        add_text(f"{opponent_score}", (opponent_field_middle, 20), 50, "white")
        add_text(f"{player_score}", (player_field_middle, 20), 50, "white")

        # draw rects
        pygame.draw.ellipse(screen, LIGHT_GREY, ball)
        pygame.draw.rect(screen, LIGHT_GREY, player)
        pygame.draw.rect(screen, LIGHT_GREY, opponent)

        # falling scores
        for score in falling_scores:
            score.fall()
            if score.y > SCREEN_HEIGHT:
                falling_scores.remove(score)

        # update screen
        pygame.display.update()
        clock.tick(FPS)

    print("game over")

if __name__ == "__main__":
    main()