# print("Hello world")
import pygame
import os
import random
from modules.classes import *
from modules.mapsettings import map_1


pygame.init()

x = 0
y = 0
blocks_list = []

background_1 = pygame.image.load(os.path.join(PATH, 'images/background_1.png'))
background_1 = pygame.transform.scale(background_1, (SCREEN_WIDTH, SCREEN_HIGHT))
block_img1 = os.path.join(PATH, 'images/wall_6.png')
block_img2 = os.path.join(PATH, 'images/wall_1.png')
block_img3 = os.path.join(PATH, 'images/city_1.png')

for row in map_1:
    for i in row:
        if i == 1:
            blocks_list.append(Block(x, y, 1, block_img1))
        elif i == 2:
            blocks_list.append(Block(x, y, 2, block_img2))
        elif i == 3:
            blocks_list.append(Block(x, y, 3, block_img3))
        x += STEP
    y += STEP
    x = 0
# image_1 = pygame.image.load(os.path.join(PATH, 'images/tank_x.png'))
player_1 = Player1(1, 1)
# image_2 = pygame.image.load(os.path.join(PATH, 'images/tank_y.png'))
player_2 = Player2(22, 11)


clock = pygame.time.Clock()
is_running = True

while is_running:
    window.fill((100, 150, 200))
    # window.blit(background_1, (0, 0))
    for item in blocks_list:
        item.blit()
    player_1.bullet.move()
    player_2.bullet.move()
    player_1.blit()
    player_2.blit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
    clock.tick(10)
    pygame.display.flip()


