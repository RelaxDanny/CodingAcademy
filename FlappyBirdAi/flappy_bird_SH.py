import pygame
import neat
import time
import os
import random

#neuro evolution augmented topology
pygame.font.init()

#use uppercase for constants
WIN_WIDTH = 570
WIN_HEIGHT = 800

BIRDS_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("FlappyBirdAi\imgs", "bird1.png")))], [pygame.transform.scale2x(pygame.image.load(os.path.join("FlappyBirdAi\imgs", "bird2.png")))], [pygame.transform.scale2x(pygame.image.load(os.path.join("FlappyBirdAi\imgs", "bird3.png")))]
PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("FlappyBirdAi\imgs", "pipe.png")))
BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("FlappyBirdAi\imgs", "base.png")))
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("FlappyBirdAi\imgs", "bg.png")))

STAT_FONT = pygame.font.SysFont("comicsans", 50)

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


#땅 움직이는 모션
class Base:
    VEL = 5
    WIDTH = BASE_IMG.get_width()
    IMG = BASE_IMG

    def __init__(self, y):
        self.y = y
        self.x1 = 0
        self.x2 = self.WIDTH
    
    def move(self):
        self.x1 -= self.VEL
        self.x2 -= self.VEL

        if self.x1 + self.WIDTH < 0:
            self.x1 = self.x2 + self.WIDTH
        if self.x2 + self.WIDTH < 0:
            self.x2 = self.x1 + self.WIDTH
    
    def draw(self, win):
        win.blit(self.IMG, (self.x1, self.y))
        win.blit(self.IMG, (self.x2, self.y))



def draw_window(win, bird, pipes, base, score):
    win.blit(BG_IMG, (0,0))
    
    for pipe in pipes:
        pipe.draw(win)

    score_label = STAT_FONT.render("Score: " + str(score), 1, (255,255,255))
    win.blit(score_label, (WIN_WIDTH - score_label.get_width() - 15, 10))

    base.draw(win)
    bird.draw(win)
    pygame.display.update()

def main():
    base = Base(730)
    pipes = [Pipe(700)]
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    score = 0
    bird = Bird(200, 200)
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        add_pipe = False
        rem = []
        for pipe in pipes:
            if pipe.collide(bird):
                pass #꺼버려라
            if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                rem.append(pipe)
            if not pipe.passed and pipe.x < bird.x:
                pipe.passed = True
                add_pipe = True
            pipe.move()
        if add_pipe:
            score += 1
            pipes.append(Pipe(700))
        for r in rem:
            pipes.remove(r)
        if bird.y + bird.img.get_height() > 730:
            pass
            
            
            
        # bird.move()
        base.move()
        draw_window(win, bird, pipes, base, score)
    pygame.quit()
    quit()

main()

def run():
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, 
                        neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)

    p = neat.Population(config)
    #statistic info
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    winner = p.run(main, 50) #main을 50번 돌려라 genomes을 다 보내라

if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config_feedforward.txt")
    run(config_path)