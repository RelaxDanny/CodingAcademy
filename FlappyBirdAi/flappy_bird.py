# pip install neat-python
import pygame
# import neat
import time
import os
import random

#use uppercase for constants
WIN_WIDTH = 570
WIN_HEIGHT = 800

BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("FlappyBirdAi\imgs", "bird1.png")))],[pygame.transform.scale2x(pygame.image.load(os.path.join("FlappyBirdAi\imgs", "bird2.png")))],[pygame.transform.scale2x(pygame.image.load(os.path.join("FlappyBirdAi\imgs", "bird3.png")))]#change the size using this function
PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("FlappyBirdAi\imgs", "pipe.png")))
BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("FlappyBirdAi\imgs", "base.png")))
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("FlappyBirdAi\imgs", "bg.png")))


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
        self.img = self.IMGS[0][0]
    
    def jump(self): 
        self.vel = -10.5 # negative인 이유는 알다 싶히, 올라가는거임 
        self.tick_count = 0 #keep track of when we last jumped
        self.height = self.y #where it originated starting to move from

    def move(self):
        self.tick_count += 1 #count how many moved we did since the last jumb
        d = self.vel * self.tick_count + 1.5 * self.tick_count ** 2 # velocity * time  
        #-10.5 * 1^2 = -9
        #9 * 1^2 = -8 ... 이러다가 플로스로 바뀜 추후에 bird여러개를 try할때 쓰임
        if d >= 16:
            #이 이하로가면 화면 아래로 벗어나니 중지해주기
            d = 16 #최대 16이상은 못가게 설정
        if d < 0:
            #0점프를 -2 정도 더 높게 설정해서 경우의수를 높이기
            d -= 2
        self.y = self.y + d

        #tilt the bird! 올라갈땐 25씩 조금식 올리고 내릴때 90도씩 빠르게 나려가기
        if d < 0 or self.y < self.height + 50:
            #when we are moving upwards
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION
        else: #if not going upwards => downwards
            if self.tilt > -90:
                self.tilt -= self.ROT_VEL #Rotate the bird to 90 degree
    
    def draw(self, win):
        self.img_count += 1
        #새가 위로 오르고 내리는걸 표현
        if self.img_count < self.AIMATION_TIME:
            self.img = self.IMGS[0][0]
        elif self.img_count < self.AIMATION_TIME * 2:
            self.img = self.IMGS[1][0]
        elif self.img_count < self.AIMATION_TIME * 3:
            self.img = self.IMGS[2][0]
        elif self.img_count < self.AIMATION_TIME * 4:
            self.img = self.IMGS[1][0]
        elif self.img_count == self.AIMATION_TIME * 4 + 1:
            self.img = self.IMGS[0][0]
            self.img_count = 0

        #90도로 떨어질땐 날개를 흔들면 안되니
        if self.tilt <= -80:
            self.img = self.IMGS[1][0] #2번째 사진을 그냥 보여주기
            self.img_count = self.AIMATION_TIME*2
        
        #rotate img 하는 부분
        rotated_image = pygame.transform.rotate(self.img, self.tilt)#rotate the img for us
        new_rect = rotated_image.get_rect(center = self.img.get_rect(topleft = (self.x, self.y)).center)
        win.blit(rotated_image, new_rect.topleft)

    def get_mask(self):
        return pygame.mask.from_surface(self.img)


def draw_window(win, bird):
    #draw the back ground and draw bird on top
    win.blit(BG_IMG, (0,0)) #top_left position에다가 bg넣기
    bird.draw(win)
    pygame.display.update()


def main():
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    bird = Bird(200, 200) #starting position
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(30) #atmost 30 ticks every sec
        for event in pygame.event.get():
            #when user clicks something do loop
            if event.type == pygame.QUIT:
                run = False
        bird.move() #call movement in every frame
        #바로 떨어지는걸 잡기위해 clock를 써서 느리게 떨어뜨릴거
    
        draw_window(win, bird)
    
    pygame.quit()
    quit()

main()
            
