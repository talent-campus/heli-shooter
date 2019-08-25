"""
A bullet of another color in our game.
"""
import pygame

from ..helper import load_image, BLUE


class Ebullet(pygame.sprite.Sprite):
    def __init__(self, x, y, vx, vy):
        super().__init__()
        self.image = load_image("bullet.png").convert_alpha()
        self.image.set_colorkey(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vx = vx
        self.vy = vy

    def update(self):
        if self.rect.right < 0:
            self.kill()
        self.rect.x += self.vx
        self.rect.y += self.vy
