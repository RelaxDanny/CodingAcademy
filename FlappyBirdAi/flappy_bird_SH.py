
import pygame
# import neat
import time
import os
import random

#use uppercase for constants
WIN_WIDTH = 570
WIN_HEIGHT = 800

BIRDS_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("FlappyBirdAi\imgs", "bird1.png")))], [pygame.transform.scale2x(pygame.image.load(os.path.join("FlappyBirdAi\imgs", "bird2.png")))], [pygame.transform.scale2x(pygame.image.load(os.path.join("FlappyBirdAi\imgs", "bird3.png")))]
PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("FlappyBirdAi\imgs", "pipe.png")))
BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("FlappyBirdAi\imgs", "base.png")))
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("FlappyBirdAi\imgs", "bg.png")))

class Bird:
    IMGS = BIRDS_IMGS
    MAX_ROTATION = 25 # rot degree
    ROT_VEL = 20 
    ANIMATION_TIME = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt = 0
        self.tick_count = 0
        self.vel = 0
        self.height = self.y
        self.img_count = 0
        self.img = self.IMGS[0][0]
    
    def jump(self):
        self.vel = -10.5 
        self.tick_count = 0
        self.height = self.y 
    
    def move(self):
        self.tick_count += 1
        d = self.vel * self.tick_count + 1.5 * self.tick_count ** 2 
        # -10.5 * 1^2 = -9
        if d >= 16:
            d = 16

        if d < 0:
            d -= 2
        
        self.y = self.y+d

        if d < 0 or self.y < self.height + 50:
            #when jumping
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION
        else:
            if self.tilt > -90:
                self.tilt -= self.ROT_VEL

    def draw(self, win):
        self.img_count += 1
        #새가 위로 오르고 내리는걸 표현하는 곳
        if self.img_count < self.ANIMATION_TIME:
            self.img = self.IMGS[0][0]
        elif self.img_count < self.ANIMATION_TIME * 2:
            self.img = self.IMGS[1][0]
        elif self.img_count < self.ANIMATION_TIME * 3:
            self.img = self.IMGS[2][0]
        elif self.img_count < self.ANIMATION_TIME * 4:
            self.img = self.IMGS[1][0]
        elif self.img_count < self.ANIMATION_TIME * 4 +1:
            self.img = self.IMGS[0][0]
            self.img_count = 0
        
        #떨어지는 코드
        if self.tilt <= -80:
            self.img = self.IMGS[1][0]
            self.img_count = self.ANIMATION_TIME * 2
        
        rotated_image = pygame.transform.rotate(self.img, self.tilt) #rotating img
        new_rect = rotated_image.get_rect(center = self.img.get_rect(topleft = (self.x, self.y)).center)
        win.blit(rotated_image, new_rect.topleft)
    
    def get_mas(self):
        return pygame.mask.from_surface(self.img)
    

def draw_window(win, bird):
    win.blit(BG_IMG, (0,0))
    bird.draw(win)
    pygame.display.update()

def main():
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    bird = Bird(200, 200)
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        bird.move()
        draw_window(win, bird)
    pygame.quit()
    quit()

main()
