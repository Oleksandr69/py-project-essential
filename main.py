import pygame
import os
import random
import time
from modules.constants import window, SCREEN_HIGHT, SCREEN_WIDTH
from modules.mapsettings import *
from modules.player1 import Player1
from modules.player2 import Player2
from modules.game import IsGame

pygame.init()

map_list = {
    1: map_1,
    2: map_2,
    3: map_3
}
sound_back = {
    1: pygame.mixer.Sound('sounds/fon-3.wav'),
    2: pygame.mixer.Sound('sounds/fon-2.wav'),
    3: pygame.mixer.Sound('sounds/fon-1.wav')
}
sound_expl_tank = pygame.mixer.Sound('sounds/explosion-tank.wav')
# background_1 = pygame.image.load(os.path.join(PATH, 'images/background_1.png'))
# background_1 = pygame.transform.scale(background_1, (SCREEN_WIDTH, SCREEN_HIGHT))
is_stop = False
clock = pygame.time.Clock()
win_1 = 0
win_2 = 0

for i in range(1,4):
    map = map_list[i]
    back_sound = sound_back[i]
    is_game = IsGame(map)
    is_game.game_map()
    is_running = True

    player_1 = Player1(1, random.randint(1, 10), is_game.map)
    player_2 = Player2(22, random.randint(1, 10), is_game.map)

    back_sound.play()

    while is_running:
        window.fill((100 + 15 * i, 150, 200 - 15 * i))
        # window.blit(background_1, (0, 0))
        for item in is_game.blocks_list:
            item.blit()
            is_game.block_bullet(item, player_1.bullet)
            is_game.block_bullet(item, player_2.bullet)

        player_1.blit()
        player_2.blit()
        player_1.bullet.move()
        player_2.bullet.move()

        if player_1.player_bullet(player_2):
            win_1 += player_1.win
            win_2 += player_2.win
            is_running = False
            is_stop = True 
        elif player_2.player_bullet(player_1):
            win_2 += player_2.win
            win_1 += player_1.win
            is_running = False
            is_stop = True
        elif player_1.colliderect(player_2) or player_2.colliderect(player_1):
            # win_1 = win_2
            sound_expl_tank.play()
            is_running = False
            is_stop = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

        clock.tick(5)
        pygame.display.flip()
    back_sound.stop()

font = pygame.font.Font(None, 100)
winner_0_msg = font.render('All died!', True, (0,0,0))
winner_1_msg = font.render(f'He won! Hits: {win_1}. Holes: {win_2}.', True, (0,100,155))
winner_2_msg = font.render(f'She won! Hits: {win_2}. Holes: {win_1}.', True, (155,100,0))
cors_0 = (SCREEN_WIDTH // 2 - winner_0_msg.get_width() // 2, SCREEN_HIGHT // 2 - winner_0_msg.get_height() // 2)
cors_1 = (SCREEN_WIDTH // 2 - winner_1_msg.get_width() // 2, SCREEN_HIGHT // 2 - winner_1_msg.get_height() // 2)
cors_2 = (SCREEN_WIDTH // 2 - winner_2_msg.get_width() // 2, SCREEN_HIGHT // 2 - winner_2_msg.get_height() // 2)
# print(win_1, win_2)
while is_stop:
    window.fill((100, 150, 100))
    # window.blit(background_1, (0, 0))
    if win_1 > win_2:
        window.blit(winner_1_msg, cors_1)
    elif win_1 < win_2:
        window.blit(winner_2_msg, cors_2)
    elif win_1 == win_2:
        window.blit(winner_0_msg, cors_0)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = True
            is_stop = False
    pygame.display.flip()
