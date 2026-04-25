import pygame
from random import randint
from src.config import WIN_W

PLATFORM_COLOR = (255, 255, 255)


class Platform:
    def __init__(self, w, h, x, y, player) -> None:
        self.player = player
        self.rect = pygame.Rect(x, y, w, h)
        self.speed = 5
        self.surface = pygame.Surface((w, h))
        self.surface.fill(PLATFORM_COLOR)
        self.font = pygame.font.SysFont(None, 30)
        self.color = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.score = 0

    def display(self, scr, score):
        scr.blit(self.surface, self.rect)
        if self.player == 1:
            scr.blit(score, (10, 10))
        else:
            scr.blit(score, (WIN_W - 120, 10))

    def update(self, scr):
        self.handle_events()
        score_rendered = self.render_score_text()
        self.display(scr, score_rendered)

    def handle_events(self):
        keys = pygame.key.get_pressed()
        if self.player == 1:
            if keys[pygame.K_w]:
                self.rect.y -= self.speed
            elif keys[pygame.K_s]:
                self.rect.y += self.speed
        if self.player == 2:
            if keys[pygame.K_UP]:
                self.rect.y -= self.speed
            if keys[pygame.K_DOWN]:
                self.rect.y += self.speed

    def render_score_text(self):
        if self.player == 1:
            return self.font.render(f"Player 1: {str(self.score)}", True, self.color)
        else:
            return self.font.render(f"Player 2: {str(self.score)}", True, self.color)
