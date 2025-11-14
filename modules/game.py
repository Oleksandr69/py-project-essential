import os
from modules.constants import *
from modules.block import Block

class IsGame:
    def __init__(self, map):
        self.map = map
        self.x = 0
        self.y = 0
        self.blocks_list = []
        self.winner = None

    def game_map(self):
        block_img1 = os.path.join(PATH, 'images/wall_6.png')
        block_img3 = os.path.join(PATH, 'images/wall_1.png')
        block_img2 = os.path.join(PATH, 'images/city_1.png')
        for row in self.map:
            for i in row:
                if i == 1:
                    self.blocks_list.append(Block(self.x, self.y, 1, block_img1))
                elif i == 2:
                    self.blocks_list.append(Block(self.x, self.y, 2, block_img2))
                elif i == 3:
                    self.blocks_list.append(Block(self.x, self.y, 3, block_img3))
                self.x += STEP
            self.y += STEP
            self.x = 0

    def block_bullet(self, item, bullet):
        sound_hit_tank = pygame.mixer.Sound('sounds/explosion-blok.wav')
        sound_expl_block = pygame.mixer.Sound('sounds/shot-1.wav')
        if item.colliderect(bullet):
            bullet.stop()        
            if item.type_wall == 1:
                sound_expl_block.play()
                self.map[item.y // STEP][item.x // STEP] = 0
                item.x = 1000000
            elif item.type_wall == 3: 
                sound_hit_tank.play()