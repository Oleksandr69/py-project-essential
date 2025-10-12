import pygame
import os

PATH = os.path.abspath(__file__+ '/../..')
SCREEN_WIDTH = 1200
SCREEN_HIGHT = 600
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
    pass
class Panzar(pygame.Rect):
    pass
class Player1(Panzar):
    pass
class Player2(Panzar):
    pass

# class Panzar:
#     def __init__(self, x, y, width, hight):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.hight = hight
#         self.speed = 7
#     def move(self):
#         self.x -= self.speed