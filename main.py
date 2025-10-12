# print("Hello world")
import pygame
import os
import random
from modules.classes import *

pygame.init()

is_running = True

while is_running:
    window.fill((200, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
    pygame.display.flip()


