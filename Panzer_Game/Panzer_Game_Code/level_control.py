import os
import pickle
import pygame
from pygame.locals import *
import sys 

sys.path.append('d:/Projects/Python/Panzer_Game_Git/Panzer_Game/Panzer_Game_Code')

if not os.path.exists('levels/'):
    os.mkdir('levels/')


#screen proportions

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720
tile_size = 50 #for 'table' 50x50

pygame.init()
clock = pygame.time.Clock()
FPS = 30

cols = SCREEN_WIDTH // tile_size
rows = SCREEN_HEIGHT // tile_size
margin = 300

win_width = SCREEN_WIDTH + margin
win_height = SCREEN_HEIGHT
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_mode('Level Control')

#backgrounds loading...

