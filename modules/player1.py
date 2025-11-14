import pygame
import os
# from modules.mapsettings import map_1
from modules.constants import PATH, STEP
from modules.panzar import Panzar

class Player1(Panzar):
    def __init__(self, x, y, map):
        super().__init__(x, y)
        self.map = map
        self.number = 1
        self.image = pygame.image.load(os.path.join(PATH, 'images/tank_x.png'))
        self.image = pygame.transform.scale(self.image, (STEP, STEP))
        self.shot = pygame.mixer.Sound('sounds/shot-3.wav')

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            if self.map[self.position[1] - 1][self.position[0]] == 0:              
                self.y -= STEP
                self.position[1] -= 1
            self.rotate_to(0)
        elif keys[pygame.K_s]:
            if self.map[self.position[1] + 1][self.position[0]] == 0:
                self.y += STEP
                self.position[1] += 1
            self.rotate_to(180)
        elif keys[pygame.K_a]:
            if self.map[self.position[1]][self.position[0] - 1] == 0:
                self.x -= STEP
                self.position[0] -= 1
            self.rotate_to(90)
        elif keys[pygame.K_d]:
            if self.map[self.position[1]][self.position[0] + 1] == 0:
                self.x += STEP
                self.position[0] += 1
            self.rotate_to(270)
        elif keys[pygame.K_e]:
            self.bullet_from_panzar()
            # self.shot.play()