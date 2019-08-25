"""
A bullet being shot in the game.
"""
import pygame

from ..helper import load_image, BLUE


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, vx, vy):
        super().__init__()
        self.image = load_image("bullet.png")
        self.image.convert_alpha()
        self.image.set_colorkey(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vx = vx
        self.vy = vy

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        if self.rect.right > 400 + 10:
            self.kill()
