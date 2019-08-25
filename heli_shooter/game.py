"""
A heli-shooter game, developed using pygame.
"""
import pygame
import random

from .helper import load_image, BLUE, RED, WHITE
from .objects import (
    Boat,
    Bullet,
    Cloud,
    Ebullet,
    Ecopter,
    Mob,
    Player,
    Ship,
)


class Game():

    def __init__(self):
        self.bg = None
        self.screen = None
        self.score = 0
        self.hi_score = 0
        self.boats = None
        self.ecopters = None
        self.mobs = None
        self.ships = None
        self.all_sprites = None


    def msg(self, txt, size, color, x, y):
        font = pygame.font.SysFont("comicsansms", size)
        txtsurf = font.render(txt, True, color)
        txtrect = txtsurf.get_rect()
        txtrect.center = x, y
        self.screen.blit(txtsurf, txtrect)


    def newmob(self):
        mob = Mob()
        self.mobs.add(mob)
        self.all_sprites.add(mob)


    def newboat(self):
        boat = Boat(self)
        self.boats.add(boat)
        self.all_sprites.add(boat)


    def newecopter(self):
        ecopter = Ecopter(self)
        self.ecopters.add(ecopter)
        self.all_sprites.add(ecopter)


    def newship(self):
        self.msg("!", 100, RED, 380, 200)
        pygame.display.update()
        ship = Ship(self)
        self.ships.add(ship)
        self.all_sprites.add(ship)


    def mobgen(self):
        i = random.choice([1, 2, 3, 4])
        if i == 1:
            self.newmob()
        if i == 2:
            self.newboat()
        if i == 3:
            self.newship()
        if i == 4:
            self.newecopter()


    def start(self):
        self.screen.fill(WHITE)
        self.msg("Heli Shooter", 50, RED, 200, 100)

        if self.score > self.hi_score:
            hscore = open("highscore.txt", "w")
            hscore.write(str(score))
            hscore.close()

        self.msg("High Score:-%s" % self.hi_score, 20, RED, 200, 50)

        wait = True
        while wait:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            c = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            if 150 + 70 > c[0] > 150 and 160 + 40 > c[1] > 160:
                self.msg("Start", 30, BLUE, 180, 180)
                if click[0] == 1:
                    wait = 0
            else:
                self.msg("Start", 30, RED, 180, 180)

            if 160 + 60 > c[0] > 160 and 230 + 40 > c[1] > 230:
                self.msg("Exit", 30, BLUE, 180, 240)
                if click[0] == 1:
                    pygame.quit()
                    quit()
            else:
                self.msg("Exit", 30, RED, 180, 240)

            pygame.display.update()


    def pause(self):
        self.screen.blit(self.bg, [0, 0])
        self.msg("Paused", 50, RED, 200, 100)
        pygame.display.update()

        wait = True
        while wait:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        wait = False
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()


    def Score(self):
        gover = True

        if self.score > self.hi_score:
            hscore = open("highscore.txt", "w")
            hscore.write(str(score))
            hscore.close()

        while gover:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:

                        gover = False
                    elif event.key == pygame.K_r:
                        gover = False
                        self.intro = True
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()
            self.msg("High Score :%s" % self.hi_score, 25, BLUE, 200, 50)
            self.msg("Game Over", 30, RED, 200, 100)
            self.msg("Your Score :%s" % self.score, 25, BLUE, 200, 200)
            pygame.display.flip()


    def main(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode([400, 400])
        pygame.display.set_caption(" Shooter")
        clock = pygame.time.Clock()
        self.bg = load_image("bg.png")

        score = 0
        try:
            hscore = open("highscore.txt", "r")
            self.hi_score = int(hscore.read())
        except:
            self.hi_score = 0

        run = True
        intro = True
        over = False

        while run:
            clock.tick(50)

            if intro:
                self.all_sprites = pygame.sprite.Group()
                cloud = Cloud()
                self.start()
                player = Player(200, 100, self)
                self.mobs = pygame.sprite.Group()
                self.bullets = pygame.sprite.Group()
                self.boats = pygame.sprite.Group()
                self.ebullets = pygame.sprite.Group()
                self.ships = pygame.sprite.Group()
                self.ecopters = pygame.sprite.Group()
                self.all_sprites.add(cloud)
                self.all_sprites.add(player)
                mob = Mob()
                self.mobs.add(mob)
                self.all_sprites.add(mob)
                boat = Boat(self)
                self.boats.add(boat)
                self.all_sprites.add(boat)
                score = 0
                intro = False

            if over:
                self.all_sprites = pygame.sprite.Group()
                cloud = Cloud()
                player = Player(200, 100, self)
                self.mobs = pygame.sprite.Group()
                self.bullets = pygame.sprite.Group()
                self.boats = pygame.sprite.Group()
                self.ebullets = pygame.sprite.Group()
                self.ships = pygame.sprite.Group()
                self.ecopters = pygame.sprite.Group()
                self.all_sprites.add(cloud)
                self.all_sprites.add(player)
                mob = Mob()
                self.mobs.add(mob)
                self.all_sprites.add(mob)
                boat = Boat(self)
                self.boats.add(boat)
                self.all_sprites.add(boat)
                over = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    player.shoot()
                    if event.key == pygame.K_RETURN:
                        self.pause()

            self.all_sprites.update()
            last_shot = pygame.time.get_ticks()

            hits = pygame.sprite.groupcollide(self.mobs, self.bullets, True, True)
            if hits:
                score += 1
                self.mobgen()

            hits1 = pygame.sprite.spritecollide(player, self.mobs, True)
            if hits1:
                self.Score()
                self.mobgen()

            hits2 = pygame.sprite.groupcollide(self.boats, self.bullets, True, True)
            if hits2:
                score += 3
                self.mobgen()

            hits4 = pygame.sprite.spritecollide(player, self.ebullets, True)
            if hits4:
                self.Score()
                over = True

            hits5 = pygame.sprite.groupcollide(self.bullets, self.ships, True, True)
            if hits5:
                score += 10
                self.mobgen()

            hits6 = pygame.sprite.spritecollide(player, self.ships, False)
            if hits6:
                self.Score()
                over = True

            hits7 = pygame.sprite.groupcollide(self.bullets, self.ecopters, True, True)
            if hits7:
                score += 5
                self.mobgen()

            hits8 = pygame.sprite.spritecollide(player, self.ecopters, False)
            if hits8:
                self.Score()
                over = True

            self.screen.fill(WHITE)
            self.screen.blit(self.bg, [0, 0])
            self.all_sprites.draw(self.screen)
            self.msg("Score:" + str(score), 30, RED, 60, 30)
            pygame.display.flip()

        pygame.quit()
        quit()


if __name__ == "__main__":
    game = Game()
    game.main()
