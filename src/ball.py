import pygame
from src.config import WIN_W, WIN_H, BALL_POS_X, BALL_POS_Y, BALL_COLOR


class Ball:
    def __init__(self, radius) -> None:
        x = BALL_POS_X
        y = BALL_POS_Y
        self.vx = 4
        self.vy = 3
        diameter = radius * 2
        self.rect = pygame.Rect(x, y, diameter, diameter)
        self.surface = pygame.Surface((diameter, diameter), pygame.SRCALPHA)
        pygame.draw.circle(self.surface, BALL_COLOR, (radius, radius), radius)

    def display(self, scr):
        scr.blit(self.surface, (self.rect))

    def update(self, scr):
        self.rect.x += self.vx
        self.rect.y += self.vy
        self.display(scr)

    def check_collides_with_walls(self):
        if self.rect.top <= 0:
            self.vy = abs(self.vy)
        if self.rect.bottom >= WIN_H:
            self.vy = -abs(self.vy)
        if self.rect.right >= WIN_W:
            return 1
        if self.rect.left <= 0:
            return 2
        return None
