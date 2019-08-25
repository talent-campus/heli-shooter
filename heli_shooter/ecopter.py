"""
A helicopter flying in the sky in our game.
"""
import pygame
import random

from .ebullet import Ebullet
from .helper import load_image


class Ecopter(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.image = load_image("ecopter.png")
        self.image = pygame.transform.scale(self.image, [60, 50])
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = random.randrange(50, 250)
        self.vx = -7
        self.last = pygame.time.get_ticks()
        self.game = game

    def update(self):
        self.vy = random.randrange(-3, 3)
        self.rect.x += self.vx
        self.rect.y += self.vy
        if self.rect.x < 0:
            self.kill()
            self.game.mobgen()

        now = pygame.time.get_ticks()
        if now - self.last > 600:
            self.last = now
            ebullet = Ebullet(self.rect.centerx, self.rect.top, -10, 0)
            self.game.all_sprites.add(ebullet)
            self.game.ebullets.add(ebullet)
