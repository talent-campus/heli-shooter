"""
A ship in our game.
"""
import pygame
import random

from .helper import load_image


class Ship(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.image = load_image("ship.png")
        self.image = pygame.transform.scale(self.image, (70, 50))
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = random.randrange(50, 250)
        self.vx = 0
        self.game = game

    def update(self):
        self.rect.x += -8
        if self.rect.x < -50:
            self.kill()
            self.game.mobgen()
