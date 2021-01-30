import pygame
pygame.init()

win = pygame.display.set_mode((500,480))

pygame.display.set_caption("First Game")

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

clock = pygame.time.Clock()

score = 0

#####1. Score 작성
#####2. hit box remove
#####3. Health bar drawing

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
        #need two more attributes for enemy
        self.health = 10
        self.visible = True #one the enemy is dead, erase health bar
        

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
                
       
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        #pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

class projectile(object): #Shoot
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
        if self.visible:#if enemy is alive
            if self.walkCount + 1 >= 33: #33을 넘어가면 0으로 changez
                self.walkCount = 0

            if self.vel > 0: #move right
                win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            else:#moving left
                win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
                
            self.hitbox = (self.x + 28, self.y + 2, 31, 57)
            #pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
             ###추가
            pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10)) #background
            pygame.draw.rect(win, (0,255,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - ((50/10)* (10 - self.health)), 10)) #declining health bar

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

    def hit(self):
        if self.health > 0:
            self.health = self.health - 1
        else:
            self.visible = False
        print("hit")

        
    

def redrawGameWindow():
    win.blit(bg, (0,0))
    text = font.render('Score: ' + str(score), 1, (0,0,0))# this will render the text
    win.blit(text, (390, 10)) # position of font
    man.draw(win)
    goblin.draw(win)
    for bullet in bullets: 
        bullet.draw(win) #이걸 추가해야 총알을 볼 수있음.
    
    pygame.display.update()


#mainloop
#to draw text in pygame
font = pygame.font.SysFont('comicsans', 30, True, True) # creating a font variable (fontname, Size, bold?, Italic?)
man = player(200, 410, 64,64)
goblin = enemy(100, 410, 64, 64, 450)
bullets = [] #this will contain our bullets
shootloops = 0
run = True
while run:
    clock.tick(27)
    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0
        
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #아래에서 총알이 닿는지 확인해야함 -> if the bullet is inside the rect, than it is hit
    for bullet in bullets: #이거 새로 만들어야함
        if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]: #if bullet is above of our rectangle
            if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:#we are on the right and left side of rectangle
                goblin.hit()
                score = score + 1 #when it is hit
                bullets.pop(bullet.index(bullet))
            
        if bullet.x < 500 and bullet.x > 0: # < 500의 의미는 not off the screen
            bullet.x += bullet.vel #for loop이 끝날때까지 vel값대로 날아감
        else:
            bullets.pop(bullets.index(bullet))
            
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootLoop == 0:
        if man.left:
            facing = -1
        else:
            facing = 1
            
        if len(bullets) < 5:
            bullets.append(projectile(round(man.x + man.width //2), round(man.y + man.height//2), 6, (0,0,0), facing))

        shootLoop = 1
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
