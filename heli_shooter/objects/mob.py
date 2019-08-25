"""
A mob in our game.
"""
import pygame
import random

from ..helper import load_image


class Mob(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.i1 = load_image("loon.png")
        self.i1 = pygame.transform.scale(self.i1, [30, 50])

        self.image = self.i1

        self.rect = self.image.get_rect()
        x = 400
        y = random.randrange(50, 270)
        self.rect.x = x
        self.rect.y = y
        self.shot_delay = 500
        self.last = pygame.time.get_ticks()

    def update(self):
        if self.rect.right <= 0:
            self.rect.x = 370
            self.rect.y = random.randrange(30, 250)
            self.vx = random.randrange(-6, -1)

        self.rect.x += -2
