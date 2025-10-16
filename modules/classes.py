import pygame
import os
from modules.mapsettings import map_1

PATH = os.path.abspath(__file__+ '/../..')
SCREEN_WIDTH = 1200
SCREEN_HIGHT = 650
STEP = 50

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGHT))
pygame.display.set_caption('TANKS')

class Block(pygame.Rect):
    def __init__(self, x, y, type_wall, img):
        super().__init__(x, y, STEP, STEP)
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (STEP, STEP))
        self.type_wall = type_wall
        
    def blit(self):
        window.blit(self.image, (self.x, self.y))

class Bullet(pygame.Rect):
    def __init__(self, x, y):
        super().__init__(x, y, 20, 20)
        self.image = pygame.image.load(os.path.join(PATH, 'images/bullet_1.png'))
        self.image = pygame.transform.scale(self.image, (15, 15))
        self.direction = None
        self.speed = 50
        self.count = 0
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
                self.stop
    def stop(self):
        self.count = 0
        self.x = 0

class Panzar(pygame.Rect):
    def __init__(self, x, y):
        super().__init__(x * STEP, y * STEP, STEP, STEP)
        self.image = None
        self.position = [x, y]
        self.bullet = Bullet(x, y)
        self.angle = 0  
    def move(serlf):
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

class Player1(Panzar):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.image.load(os.path.join(PATH, 'images/tank_x.png'))
        self.image = pygame.transform.scale(self.image, (STEP, STEP))
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            if map_1[self.position[1] - 1][self.position[0]] == 0:              
                self.y -= STEP
                self.position[1] -= 1
            self.rotate_to(0)
        elif keys[pygame.K_s]:
            if map_1[self.position[1] + 1][self.position[0]] == 0:
                self.y += STEP
                self.position[1] += 1
            self.rotate_to(180)
        elif keys[pygame.K_a]:
            if map_1[self.position[1]][self.position[0] - 1] == 0:
                self.x -= STEP
                self.position[0] -= 1
            self.rotate_to(90)
        elif keys[pygame.K_d]:
            if map_1[self.position[1]][self.position[0] + 1] == 0:
                self.x += STEP
                self.position[0] += 1
            self.rotate_to(270)
        elif keys[pygame.K_c]:
            self.bullet_from_panzar()
class Player2(Panzar):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.image.load(os.path.join(PATH, 'images/tank_y.png'))
        self.image = pygame.transform.scale(self.image, (STEP, STEP))
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if map_1[self.position[1] - 1][self.position[0]] == 0:              
                self.y -= STEP
                self.position[1] -= 1
            self.rotate_to(0)
        elif keys[pygame.K_DOWN]:
            if map_1[self.position[1] + 1][self.position[0]] == 0:
                self.y += STEP
                self.position[1] += 1
            self.rotate_to(180)
        elif keys[pygame.K_LEFT]:
            if map_1[self.position[1]][self.position[0] - 1] == 0:
                self.x -= STEP
                self.position[0] -= 1
            self.rotate_to(90)
        elif keys[pygame.K_RIGHT]:
            if map_1[self.position[1]][self.position[0] + 1] == 0:
                self.x += STEP
                self.position[0] += 1
            self.rotate_to(270)
        elif keys[pygame.K_c]:
            self.bullet_from_panzar()

# class Panzar:
#     def __init__(self, x, y, width, hight):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.hight = hight
#         self.speed = 7
#     def move(self):
#         self.x -= self.speed