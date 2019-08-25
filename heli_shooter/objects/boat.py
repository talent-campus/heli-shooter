"""
A boat in our game.
"""
import pygame

from .ebullet import Ebullet
from ..helper import load_image


class Boat(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.image = load_image("boat.png")
        self.image = pygame.transform.scale(self.image, [60, 50])
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 300
        self.vx = 0
        self.vy = 0
        self.last_shot = pygame.time.get_ticks()
        self.shot_delay = 400
        self.vx = -0.5
        self.vy = 0
        self.game = game

    def update(self):
        self.rect.x += self.vx
        if self.rect.left <= 0:
            self.kill()
            self.game.mobgen()

        now = pygame.time.get_ticks()
        if now - self.last_shot > 600:
            self.last_shot = now

            ebullet = Ebullet(self.rect.centerx, self.rect.top, -10, -10)
            self.game.all_sprites.add(ebullet)
            self.game.ebullets.add(ebullet)
