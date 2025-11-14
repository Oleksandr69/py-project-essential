import pygame
# from modules.mapsettings import map_1
from modules.constants import STEP, window
from modules.bullet import Bullet

class Panzar(pygame.Rect):
    def __init__(self, x, y):
        super().__init__(x * STEP, y * STEP, STEP, STEP)
        self.image = None
        self.shot = None
        self.position = [x, y]
        self.bullet = Bullet(x, y)
        self.angle = 0
        self.hit = 0
        self.win = 0

    def move(self):
        pass

    def blit(self):
        self.move()
        window.blit(self.image, (self.x, self.y))

    def rotate_to(self, angle):
        rotate = (360 - self.angle + angle)
        self.angle = angle
        self.image = pygame.transform.rotate(self.image, rotate)

    def bullet_from_panzar(self):
        if self.bullet.count == 0:
            self.bullet.x = self.x + STEP / 2 - 10
            self.bullet.y = self.y + STEP / 2 - 10
            self.bullet.count = 10
            self.bullet.direction = self.angle
    #         self.shot.play()

    def player_bullet(self, player):
        sound_expl_tank = pygame.mixer.Sound('sounds/explosion-tank.wav')
        sound_hit_tank = pygame.mixer.Sound('sounds/explosion-blok.wav')
        if self.colliderect(player.bullet):
            self.hit += 1
            self.win +=1
            player.bullet.stop() 
            if self.hit <= 3:
                sound_hit_tank.play()
                return False
            else:
                sound_expl_tank.play()
                self.hit = 0
                return True