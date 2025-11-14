import pygame
import os
# from modules.mapsettings import map_1
from modules.constants import PATH, window

class Bullet(pygame.Rect):
    def __init__(self, x, y):
        super().__init__(x, y, 20, 20)
        self.image = pygame.image.load(os.path.join(PATH, 'images/expl_1.png'))
        self.image = pygame.transform.scale(self.image, (15, 15))
        self.direction = None
        self.speed = 60
        self.count = None
        # self.sound = pygame.mixer.Sound('sounds/shot-1.wav')
    def move(self):
        if self.count != 0:
            window.blit(self.image, (self.x, self.y))
            if self.direction == 0:
                self.y -= self.speed
            elif self.direction == 180:
                self.y += self.speed
            elif self.direction == 90:
                self.x -= self.speed
            elif self.direction == 270:
                self.x += self.speed
            self.count -= 1
            if self.count == 0:  
                self.stop()
    def stop(self):
        self.count = 0
        self.x = 1000000
        self.y = 1000000