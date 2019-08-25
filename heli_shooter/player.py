"""
A player that plays our game. (That could be you!)
"""
import pygame

from .bullet import Bullet
from .helper import load_image


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, game):
        super().__init__()
        self.image = load_image("copter.png")
        self.image = pygame.transform.scale(self.image, [60, 50])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vx = 0
        self.vy = 0
        self.last_shot = pygame.time.get_ticks()
        self.shot_delay = 1000
        self.game = game

    def shoot(self):
        now = pygame.time.get_ticks()
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            if now - self.last_shot > self.shot_delay:
                self.last_shot = now
                bullet = Bullet(self.rect.centerx, self.rect.top, 10, 0)
                self.game.all_sprites.add(bullet)
                self.game.bullets.add(bullet)

        if keys[pygame.K_LSHIFT]:
            if now - self.last_shot > self.shot_delay:
                self.last_shot = now
                bullet = Bullet(self.rect.centerx, self.rect.bottom, 0, 10)
                self.game.all_sprites.add(bullet)
                self.game.bullets.add(bullet)

    def update(self):
        self.vx, self.vy = 0, 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.vx = -5
        elif keys[pygame.K_RIGHT]:
            self.vx = 5
        elif keys[pygame.K_UP]:
            self.vy = -5
        elif keys[pygame.K_DOWN]:
            self.vy = 5

        self.rect.x += self.vx
        self.rect.y += self.vy
        if self.rect.right >= 400:
            self.rect.right = 400
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.bottom >= 400:
            self.rect.bottom = 400
        if self.rect.top <= 0:
            self.rect.top = 0
