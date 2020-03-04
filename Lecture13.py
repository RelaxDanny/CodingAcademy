import pygame
pygame.init()

win = pygame.display.set_mode((500,480))

pygame.display.set_caption("First Game")

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

clock = pygame.time.Clock()


#####1. hit box 그리기!!
#####2.
#####3.

class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True
        #0304 1번
        self.hitbox = (self.x + 17, self.y + 11, 29, 52) # #일단은 self.x + 20 ,self.y, 28, 60 으로 해보
        

    def draw(self, win):
        if self.walkCount + 1 >= 27: #maximum walkcount
            self.walkCount = 0

        if not(self.standing): #If he is moving, run through the animation
            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount +=1
        else: #If he is standing still
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))#walkRight[0]는 오른쪽모습의 첫번째 사진임
                #총을쏘기위해서 모션 유지
            else:
                win.blit(walkLeft[0], (self.x, self.y))
        ###추가
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing #음수면 왼쪽, 양수면 오른쪽으로 총 발사

    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)
        #pygame에서 동그라미 그리는 방법!! x,y는 생성 위치

class enemy():
    walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png')]
    walkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png')]

    def __init__()self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.walkCount = 0
        self.vel = 3 #enemy's speed
        self.path = [self.x, self.end]
        self.hitbox = (self.x + 28, self.y + 2, 31, 57) #일단은 self.x + 20 ,self.y, 28, 60 으로 해보

    def draw(self, win):
        self.move()
        if self.walkCount + 1 >= 33: #33을 넘어가면 0으로 changez
            self.walkCount = 0

        if self.vel > 0: #move right
            win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        else:#moving left
            win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
            
        self.hitbox = (self.x + 28, self.y + 2, 31, 57)
        pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

    def move(self): #y축으로 움직이고 싶으면 x를 y로만 바꿔주면 
        if self.vel > 0:
            if self.x + self.vel < self.path[1] # 2번째 값인 path의 self.end를 의미함
            self.x += self.vel
            else:
                self.vel = self.vel * -1 #원점에서보다 왼쪽으로 가면 vel또한 음수가 되어서 else문이 실행 
                self.walkCount = 0
        else:#if vel is negative 
            if self.x - self.vel > self.path[0]: #should not move over the path
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

        
    

def redrawGameWindow():
    win.blit(bg, (0,0))
    man.draw(win)
    goblin.draw(win)
    for bullet in bullets: 
        bullet.draw(win) #이걸 추가해야 총알을 볼 수있음.
    
    pygame.display.update()


#mainloop
man = player(200, 410, 64,64)
goblin = enemy(100, 410, 64, 64, 450)
bullets = [] #this will contain our bullets
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    for bullet in bullets: #이거 새로 만들어야함 
        if bullet.x < 500 and bullet.x > 0: # < 500의 의미는 not off the screen
            bullet.x += bullet.vel #for loop이 끝날때까지 vel값대로 날아감
        else:
            bullets.pop(bullets.index(bullet))#501픽셀로 가버리면 불릿을 없애버리는 코드
            #현재의 bullet 인덱스(위치)를 찾아서 지움
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if man.left:
            facing = -1
        else:
            facing = 1
            
        if len(bullets) < 5:
            bullets.append(projectile(round(man.x + man.width //2), round(man.y + man.height//2), 6, (0,0,0), facing))
            #bullets.append는 bullets라는 리스트에 projectile클래스를 계속 추가 하는것 -> 총알 쏘는것
    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False #since he is moving right now 
    elif keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False
    else:
        #기존에 있던 fales값들을 지워줘야 함 그래야만 그대로 서있게 되니
        man.standing = True
        man.walkCount = 0
        
    if not(man.isJump):
        if keys[pygame.K_UP]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10
            
    redrawGameWindow()

pygame.quit()
