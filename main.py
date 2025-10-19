# print("Hello world")
import pygame
import os
import random
import time
from modules.classes import *
from modules.mapsettings import map_1


pygame.init()

x = 0
y = 0
blocks_list = []
map = map_1
sound_expl = pygame.mixer.Sound('sounds/explosion-tank.wav')

background_1 = pygame.image.load(os.path.join(PATH, 'images/background_1.png'))
background_1 = pygame.transform.scale(background_1, (SCREEN_WIDTH, SCREEN_HIGHT))

font = pygame.font.Font(None, 120)
winner_0_msg = font.render('all die', True, (0,0,0))
winner_1_msg = font.render('he win', True, (0,0,255))
winner_2_msg = font.render('she win', True, (255,0,0))
cors = (SCREEN_WIDTH // 2 - winner_1_msg.get_width() // 2,SCREEN_HIGHT // 2 - winner_1_msg.get_height() // 2)

block_img1 = os.path.join(PATH, 'images/wall_6.png')
block_img2 = os.path.join(PATH, 'images/wall_1.png')
block_img3 = os.path.join(PATH, 'images/city_1.png')

for row in map:
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

player_1 = Player1(1, 1)
player_2 = Player2(22, 11)

clock = pygame.time.Clock()

is_running = True
is_stop = False
winner = None
count_player_1 = 0
count_player_2 = 0

while is_running:
    window.fill((100, 150, 200))
    # window.blit(background_1, (0, 0))
    for item in blocks_list:
        item.blit()
        if item.colliderect(player_1.bullet):
            player_1.bullet.stop()
            if item.type_wall == 1:
                map[item.y // STEP][item.x // STEP] = 0
                item.x = 1000000
        if item.colliderect(player_2.bullet):
            player_2.bullet.stop()
            if item.type_wall == 1:
                map[item.y // STEP][item.x // STEP] = 0
                item.x = 1000000
    player_1.bullet.move()
    player_2.bullet.move()
    player_1.blit()
    player_2.blit()

    if player_1.colliderect(player_2.bullet):
        count_player_1 += 1
        if count_player_1 <= 3:
            player_2.bullet.stop()
        else:
            sound_expl.play()
            winner = 2
            is_running = False
            is_stop = True
    elif player_2.colliderect(player_1.bullet):
        count_player_2 += 1
        if count_player_2 <= 3:
            player_1.bullet.stop()
        else:
            sound_expl.play()
            winner = 1
            is_running = False
            is_stop = True
    elif player_1.colliderect(player_2) or player_2.colliderect(player_1):
        winner = 0
        sound_expl.play()
        is_running = False
        is_stop = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
    clock.tick(10)
    pygame.display.flip()

while is_stop:
    window.fill((100, 150, 100))
    # window.blit(background_1, (0, 0))
    if winner == 1:
        window.blit(winner_1_msg, cors)
    elif winner == 2:
        window.blit(winner_2_msg, cors)
    elif winner == 0:
        window.blit(winner_0_msg, cors)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
            is_stop = False
    pygame.display.flip()
