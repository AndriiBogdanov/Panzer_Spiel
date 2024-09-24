import pygame
import os

import sys

sys.path.append('/Users/macbookproandrii/Documents/GitHub/Panzer_Game/Panzer_Game_Code')

from maps import map



PATH = os.path.abspath(__file__ + '/../Textures')
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720
STEP = 39

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Battle City')

class Blocks(pygame.Rect):
    def __init__(self, left, top, block_type, img):
        super().__init__(left, top, STEP, STEP)
        self.img = pygame.image.load(img)
        self.img = pygame.transform.scale(self.img, (STEP, STEP))
        self.block_type = block_type
        self.left = left
        self.top = top
        
    def img_init(self):
        global window
        window.blit(self.img, (self.left, self.top))

class Guns(pygame.Rect):
    def __init__(self, left, top):
        super(). __init__(left, top, 25, 25)
        self.img = pygame.image.load(os.path.join(PATH, 'bullet_small.png'))
        self.img = pygame.transform.scale(self.img, (25, 25))
        self.directions = None
        self.counts = 0
        self.speed = 40
    def moving(self):
        if self.counts != 0:
            window.blit(self.img, (self.left, self.top))
            if self.directions == 0:
                self.top -= self.speed
            elif self.directions == 90:
                self.left -= self.speed
            elif self.directions == 270:
                self.left += self.speed
            elif self.directions == 180:
                self.top += self.speed
            self.counts -= 1

            if self.counts == 0:
                self.game_over()



    def game_over(self):
        self.counts = 0
        self.left = 100000

class Panzern(pygame.Rect):
    def __init__(self, left, top):
        super().__init__(left * STEP, top * STEP, STEP, STEP)
        self.health = 3
        self.img = None
        self.position = [left, top]
        self.guns = Guns(left, top)
        self.angle = 0
    def moving(self):
        pass
    def img_init(self):
        self.moving()
        window.blit(self.img, (self.left, self.top))
    def rotation_to_obj(self, angle):
        rotation = (360 - self.angle + angle)
        self.angle = angle
        self.img = pygame.transform.rotate(self.img, rotation)
    def strikes(self):
        if self.guns.counts == 0:
            self.guns.left = self.left + STEP / 2 - 10
            self.guns.top = self.top + STEP / 2 - 10
            self.guns.counts = 10
            self.guns.directions = self.angle

class User(Panzern):
    def __init__(self, left, top):
        super().__init__(left, top)
        self.img = pygame.image.load(os.path.join(PATH, 'yellowtank_front.png'))
        self.img = pygame.transform.scale(self.img, (STEP, STEP))
    def moving(self):
        play_keys = pygame.key.get_pressed()
        if play_keys[pygame.K_w]:
            if map[self.position[1] - 1][self.position[0]] == 0:
                self.top -= STEP
                self.position[1] -= 1
            self.rotation_to_obj(0)
        elif play_keys[pygame.K_s]:
            if map[self.position[1] + 1][self.position[0]] == 0:
                self.top += STEP
                self.position[1] += 1
            self.rotation_to_obj(180)
        elif play_keys[pygame.K_a]:
            if map[self.position[1]][self.position[0] - 1] == 0:
                self.left -= STEP
                self.position[0] -= 1
            self.rotation_to_obj(90)
        elif play_keys[pygame.K_d]:
            if map[self.position[1]][self.position[0] + 1] == 0:
                self.left += STEP
                self.position[0] += 1
            self.rotation_to_obj(270)
        elif play_keys[pygame.K_SPACE]:
            self.strikes()

class User2(Panzern):
    def __init__(self, left, top):
        super().__init__(left, top)
        self.img = pygame.image.load(os.path.join(PATH, 'redfiretank_front.png'))
        self.img = pygame.transform.scale(self.img, (STEP, STEP))
    def moving(self):
        play_keys = pygame.key.get_pressed()
        if play_keys[pygame.K_UP]:
            if map[self.position[1] - 1][self.position[0]] == 0:
                self.top -= STEP
                self.position[1] -= 1
            self.rotation_to_obj(0)
        elif play_keys[pygame.K_DOWN]:
            if map[self.position[1] + 1][self.position[0]] == 0:
                self.top += STEP
                self.position[1] += 1
            self.rotation_to_obj(180)
        elif play_keys[pygame.K_LEFT]:
            if map[self.position[1]][self.position[0] - 1] == 0:
                self.left -= STEP
                self.position[0] -= 1
            self.rotation_to_obj(90)
        elif play_keys[pygame.K_RIGHT]:
            if map[self.position[1]][self.position[0] + 1] == 0:
                self.left += STEP
                self.position[0] += 1
            self.rotation_to_obj(270)
        elif play_keys[pygame.K_f]:
            self.strikes()

#class Enemy(Panzern):
    

            

    

        

    
