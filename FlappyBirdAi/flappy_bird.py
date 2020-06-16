# pip install neat-python
import pygame
import neat
import time
import os
import random

#use uppercase for constants
WIN_WIDTH = 600
WIN_HEIGHT = 800

BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("FlappyBirdAi\imgs", "bird1.png")))],[pygame.transform.scale2x(pygame.image.load(os.path.join("FlappyBirdAi\imgs", "bird2.png")))],[pygame.transform.scale2x(pygame.image.load(os.path.join("FlappyBirdAi\imgs", "bird3.png")))]#change the size using this function
PIPE_IMG = [pygame.transform.scale2x(pygame.image.load(os.path.join("FlappyBirdAi\imgs", "pipe.png")))]
BASE_IMG = [pygame.transform.scale2x(pygame.image.load(os.path.join("FlappyBirdAi\imgs", "base.png")))]
BG_IMG = [pygame.transform.scale2x(pygame.image.load(os.path.join("FlappyBirdAi\imgs", "bg.png")))]


class Bird:
    IMGS = BIRD_IMGS
    MAX_ROTATION = 25 # tilt degrees
    ROT_VEL = 20 #how much will we rotate the bird for each frame
    AIMATION_TIME = 5 #how long will we show the animation, how fast, slow while flying

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt = 0 # 새의 기울기
        self.tick_count = 0
        self.vel = 0
        self.height = self.y
        self.img_count = 0 #which image will be shown?
        self.img = self.IMGS[0]
    
    def jump(self): 
        self.vel = -10.5 # negative인 이유는 알다 싶히, 올라가는거임 
        self.tick_count = 0 #keep track of when we last jumped
        self.height = self.y #where it originated starting to move from

    def move(self):
        pass
while True: #30 times per sec
    bird.move() #how much does it need to move in a second?

