import pygame
from modules.constants import STEP, window

class Block(pygame.Rect):
    def __init__(self, x, y, type_wall, img):
        super().__init__(x, y, STEP, STEP)
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (STEP, STEP))
        self.type_wall = type_wall
        
    def blit(self):
        window.blit(self.image, (self.x, self.y))