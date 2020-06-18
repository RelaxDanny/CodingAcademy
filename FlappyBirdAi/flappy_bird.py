# pip install neat-python
import pygame
# import neat
import time
import os
import random

pygame.font.init()
#use uppercase for constants
WIN_WIDTH = 570
WIN_HEIGHT = 800

BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("FlappyBirdAi\imgs", "bird1.png")))],[pygame.transform.scale2x(pygame.image.load(os.path.join("FlappyBirdAi\imgs", "bird2.png")))],[pygame.transform.scale2x(pygame.image.load(os.path.join("FlappyBirdAi\imgs", "bird3.png")))]#change the size using this function
PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("FlappyBirdAi\imgs", "pipe.png")))
BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("FlappyBirdAi\imgs", "base.png")))
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("FlappyBirdAi\imgs", "bg.png")))

STAT_FONT = pygame.font.SysFont("comicsans", 50)

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






class Pipe:
    GAP = 200
    VEL = 5

    def __init__(self, x):
        self.x = x
        self.height = 0
        self.gap = 100
        self.top = 0 #where are the top and bottom of pipe img?
        self.bottom = 0

        self.PIPE_TOP = pygame.transform.flip(PIPE_IMG, False, True) #flip the pipe (위에 있는거)
        self.PIPE_BOTTOM = PIPE_IMG
        self.passed = False #is bird passed from pipe?
        self.set_height() #define where top and bottom and how tall the pipe is

    def set_height(self):
        #give random number to the pipe height
        self.height = random.randrange(40,450)
        self.top = self.height - self.PIPE_TOP.get_height()
        self.bottom = self.height + self.GAP
    
    def move(self):
        self.x -= self.VEL 
    
    def draw(self, win): #draw pipe
        win.blit(self.PIPE_TOP, (self.x, self.top))
        win.blit(self.PIPE_BOTTOM, (self.x, self.bottom))
    
    def collide(self, bird): #이번엔 마스크라는 기능을 사용할것. 박스가 아니라
        # 박스를 사용하면 오차가 심함. 그래서 마스크라는 함수를 써서 실제 픽셀의 위치를 확인하고 부딛혔는지 확인 
        #위에서 get_mask를 만든이유
        bird_mask = bird.get_mask()
        top_mask = pygame.mask.from_surface(self.PIPE_TOP)
        bottom_mask = pygame.mask.from_surface(self.PIPE_BOTTOM)
        #offset = how far each objects are 
        # bird to top 
        top_offset = (self.x - bird.x, self.top - round(bird.y)) #좌표는 decimal이면 안되어서
        bottom_offset = (self.x - bird.x, self.bottom - round(bird.y))

        b_point = bird_mask.overlap(bottom_mask, bottom_offset)  #returns True when collide
        t_point = bird_mask.overlap(top_mask, top_offset)

        if t_point or b_point:
            return True
        else:
            return False  #안부딛힘 

#땅바닥 움직이는 모션 주기
class Base:
    VEL = 5 #same as pipe
    WIDTH = BASE_IMG.get_width()
    IMG = BASE_IMG

    def __init__(self, y):
        self.y = y
        self.x1 = 0
        self.x2 = self.WIDTH

    def move(self):
        #왼쪽으로 이동해야하니 빼주기
        self.x1 -= self.VEL
        self.x2 -= self.VEL 

        #2개의 이미지를 사용하면서 왼쪽으로 보내고 하나가 0에닿으면 다시 오른쪽으로 오게하는 코드
        if self.x1 + self.WIDTH < 0:
            self.x1 = self.x2 + self.WIDTH
        if self.x2 + self.WIDTH < 0:
            self.x2 = self.x1 + self.WIDTH

    def draw(self, win):
        win.blit(self.IMG, (self.x1, self.y))
        win.blit(self.IMG, (self.x2, self.y))






def draw_window(win, bird, pipes, base, score):
    #draw the back ground and draw bird on top
    win.blit(BG_IMG, (0,0)) #top_left position에다가 bg넣기
    for pipe in pipes:
        pipe.draw(win)

    score_label = STAT_FONT.render("Score: " + str(score),1,(255,255,255))
    win.blit(score_label, (WIN_WIDTH - score_label.get_width() - 15, 10))
    
    base.draw(win)

    bird.draw(win)
    pygame.display.update() 

def main():
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    bird = Bird(230, 350) #starting position
    base = Base(730) #very bottom of the screen
    pipes = [Pipe(700)]
    run = True
    score = 0 
    clock = pygame.time.Clock()

    while run:
        clock.tick(30) #atmost 30 ticks every sec
        for event in pygame.event.get():
            #when user clicks something do loop
            if event.type == pygame.QUIT:
                run = False
            
        # bird.move() #call movement in every frame
        add_pipe = False
        #바로 떨어지는걸 잡기위해 clock를 써서 느리게 떨어뜨릴거
        rem = []
        for pipe in pipes:
            #계속 새로운 파이프가 나오게 하기 x축의 끝을 보면 바로 생성
            if pipe.collide(bird):
                pass
            if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                rem.append(pipe)
            if not pipe.passed and pipe.x < bird.x:
                pipe.passed = True
                add_pipe = True

            pipe.move()
        if add_pipe:
            score += 1 #파이프 패스하면 스코어 1점
            pipes.append(Pipe(700)) #이거 숫자바꾸면 좀더 빠르게 나타남

        #지나가면 지우기
        for r in rem:
            pipes.remove(r)

        if bird.y + bird.img.get_height() > 730:
            #hit the floor
            pass

        base.move()
        draw_window(win, bird, pipes, base, score)
    
    pygame.quit()
    quit()

main()