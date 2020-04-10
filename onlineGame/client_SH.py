import pygame
from network_SH import network

width = 500
height = 500

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Manhattan")

clientNumber = 0

class Player(object):
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.vel = 5
        self.rect = (x, y, width, height)

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.vel
        if keys[pygame.K_RIGHT]:
            self.x += self.vel
        if keys[pygame.K_UP]:
            self.y -= self.vel
        if keys[pygame.K_DOWN]:
            self.y += self.vel

        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)

def read_pos(str):
    str = str.split(",") # ,형태로스트링을 나눠라 24, 30
    return int(str[0]), int(str[1])

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1]) # -. 24, 30 ->  "24, 30"

def redrawWindow(win, player, player2):
    win.fill((255, 255, 255))
    player.draw(win)
    player2.draw(win)
    pygame.display.update() #업데이트 
    
def main():
    n = network()
    startPos = read_pos(n.getPos()) #getPos의 리턴값은 connect()의 리턴값과 같다 -> 받은 데이터 -> 내가 받은 포지션 -> (50, 50) =(x,y) 
    p1 = Player(startPos[0], startPos[1], 100, 100, (10, 100, 100))
    p2 = Player(0, 0, 100, 100, (200, 0, 0))
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        p2Pos = read_pos(n.send(make_pos((p1.x, p1.y))))
        p2.x = p2Pos[0]
        p2.y = p2Pos[1]
        p2.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p1.move()
        redrawWindow(win, p1, p2)

main()