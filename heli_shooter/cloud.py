"""
A cloud on the sky in our game.
"""
import pygame

from .helper import load_image, BLUE


class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = load_image("cloud.png")
        self.image.set_colorkey(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 40
        self.vx = -2

    def update(self):
        self.rect.x += self.vx
        if self.rect.x < -200:
            self.rect.x = 400
