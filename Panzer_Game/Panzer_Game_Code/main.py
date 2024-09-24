
import pygame
import os
import random
import sys
sys.path.append('/Users/macbookproandrii/Documents/GitHub/Panzer_Game')

from objects_class import *
from EnemyAI import Enemy
from maps import map
# from .objects_class import *
pygame.init()

pygame.font.init()


backgrnd = pygame.image.load(os.path.join(PATH, 'background.png'))
backgrnd = pygame.transform.scale(backgrnd, (SCREEN_WIDTH, SCREEN_HEIGHT))

text_font = pygame.font.Font(None, 120)
winner_1user_text = text_font.render('Blue Win', True, (0, 0, 255))
winner_2user_text = text_font.render('Red Win', True, (255, 0, 0))
winner_enemy_text = text_font.render('Ai Win', True, (255, 0, 0))

left = 0
top = 0

list_of_blocks = []



wall1_img = os.path.join(PATH, 'grass_block.png')
wall2_img = os.path.join(PATH, 'grass_block_no_collision.png')

for textures in map:
    for i in textures:
        if i == 1:
            list_of_blocks.append(Blocks(left, top, 1, wall1_img))
        elif i == 2:
            list_of_blocks.append(Blocks(left, top, 2, wall2_img))
        left += STEP
    top += STEP
    left = 0

user = User(2, 2)
user2 = User2(24, 2)
enemy = Enemy(4, 2, "/Users/macbookproandrii/Documents/GitHub/Panzer_Game/Panzer_Game_Code/Textures/silvertank_front.png")

timer = pygame.time.Clock()

game_start_processing = True

win = None

while game_start_processing:
    window.blit(backgrnd, (0, 0))
    for block in list_of_blocks:
        block.img_init() #img_init
        if block.colliderect(user.guns):
            user.guns.game_over()
            if block.block_type == 1:
                map[block.top // STEP][block.left // STEP] = 0

                block.left = 1000000

        if block.colliderect(user2.guns):
            user2.guns.game_over()
            if block.block_type == 1:
                map[block.top // STEP][block.left // STEP] = 0

                block.left = 1000000


    user.guns.moving()
    user2.guns.moving()
    user.img_init() #blit
    user2.img_init()
    enemy.img_init()
    
    if user.colliderect(user2.guns):
        win = 2
        game_start_processing = False
        processing_win = True

    elif user2.colliderect(user.guns):
        win = 1
        game_start_processing = False
        processing_win = True

    elif enemy.colliderect(enemy.guns):
        win = 3
        game_start_processing = False
        processing_win = True


    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            game_start_processing = False
    
    timer.tick(10)
    pygame.display.flip()

coordinate_text = (SCREEN_WIDTH // 2 - winner_1user_text.get_width() // 2,
                   SCREEN_HEIGHT //2 - winner_1user_text.get_width() // 2)

while processing_win:
    window.blit(backgrnd, (0, 0))

    if win == 1:
        window.blit(winner_1user_text, coordinate_text) 
    elif win == 2:
        window.blit(winner_2user_text, coordinate_text)
    elif win == 3:
        window.blit(winner_enemy_text, coordinate_text)

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            processing_win == False

            pygame.quit()
    
    pygame.display.flip()


    





