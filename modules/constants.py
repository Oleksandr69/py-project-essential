import pygame
import os

PATH = os.path.abspath(__file__+ '/../..')
SCREEN_WIDTH = 1200
SCREEN_HIGHT = 650
STEP = 50

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGHT))
pygame.display.set_caption('TANKS')
