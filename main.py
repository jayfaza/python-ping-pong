import pygame

pygame.init()

from src.platform import Platform
from src.ball import Ball
from src.config import WIN_W, WIN_H, FPS

screen = pygame.display.set_mode((WIN_W, WIN_H))
platforms = []
player1 = Platform(10, 100, 20, 100, 1)
player2 = Platform(10, 100, 480, 100, 2)
ball = Ball(30)

platforms.append(player1)
platforms.append(player2)

clock = pygame.time.Clock()

reset_timer = 0

is_run = True

while is_run:
    screen.fill((200, 200, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_run = False

    if reset_timer > 0:
        reset_timer -= 1
        if reset_timer == 0:
            ball.rect.x = WIN_W // 2
            ball.rect.y = WIN_H // 2
            ball.vx = -ball.vx
    else:
        result = ball.check_collides_with_walls()
        if result == 1:
            player1.score += 1
            reset_timer = FPS * 2
        elif result == 2:
            player2.score += 1
            reset_timer = FPS * 2

    ball.update(screen)

    for player in platforms:
        player.rect.top = max(0, player.rect.top)
        player.rect.bottom = min(WIN_H, player.rect.bottom)
        player.update(screen)
        if player.rect.colliderect(ball.rect):
            ball.vx = -ball.vx

    clock.tick(FPS)
    pygame.display.flip()
pygame.quit()
