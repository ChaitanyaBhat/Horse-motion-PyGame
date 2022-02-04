import pygame
import time
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()
displayWidth=9*100
displayHeight=7*100
black = (0,0,0); green = (10,200,10); orange = (200,100,10); white = (255,250,200)

gameDisplay=pygame.display.set_mode((displayWidth,displayHeight))
pygame.display.set_caption("Move Horse")

class Horse(pygame.sprite.Sprite):
    def __init__(self,*kwargs):
        super(Horse,self).__init__(*kwargs)
        self.x =140; self.y =100
        
        self.horseImg = []
        self.horseImg.append(pygame.image.load('h1.png'))
        self.horseImg.append(pygame.image.load('h2.png'))
        self.horseImg.append(pygame.image.load('h3.png'))
        self.horseImg.append(pygame.image.load('h4.png'))
        self.horseImg.append(pygame.image.load('h5.png'))
        self.horseImg.append(pygame.image.load('h6.png'))
        self.horseImg.append(pygame.image.load('h7.png'))
        self.horseImg.append(pygame.image.load('h8.png'))

        for i in range(8):
            self.horseImg[i].set_colorkey((255,255,255),RLEACCEL)
            self.rect = self.horseImg[i].get_rect(bottomright = (self.x,self.y))

    def update(self,pressed_key,i):
        if self.rect.left < 0: 
            self.rect.left = 0
        elif self.rect.right > displayWidth: 
            self.rect.right = displayWidth
        if self.rect.top < 0: 
            self.rect.top = 0
        elif self.rect.bottom > displayHeight: 
            self.rect.bottom = displayHeight

        if pressed_key[K_RIGHT]:
            self.rect.move_ip(40,0)
            self.x += 40
        elif pressed_key[K_LEFT]:
            self.rect.move_ip(-40,0)
            self.x -= 40
        elif pressed_key[K_UP]:
            self.rect.move_ip(0,-40)
            self.y -= 40
        elif pressed_key[K_DOWN]:
            self.rect.move_ip(0,40)
            self.y += 40
        if pressed_key[K_KP6]:
            for j in range(8):
                self.horseImg[j] = pygame.transform.rotate(self.horseImg[j],-90)
            self.rect = self.horseImg[i].get_rect(bottomright = (self.x,self.y))
        elif pressed_key[K_KP8]:
            for j in range(8):
                self.horseImg[j] = pygame.transform.rotate(self.horseImg[j],90)
            self.rect = self.horseImg[i].get_rect(bottomright = (self.x,self.y))
        if pressed_key[K_KP4]:
            for j in range(8):
                self.horseImg[j] = pygame.transform.flip(self.horseImg[j],1,0)
            self.rect = self.horseImg[i].get_rect(bottomright = (self.x,self.y))
        elif pressed_key[K_KP2]:
            for j in range(8):
                self.horseImg[j] = pygame.transform.flip(self.horseImg[j],0,1)
            self.rect = self.horseImg[i].get_rect(bottomright = (self.x,self.y))
        
        for track in tracks:
            if self.rect.colliderect(track.rect):
                if pressed_key[K_RIGHT]:
                    self.rect.move_ip(-40,0)
                elif pressed_key[K_LEFT]:
                    self.rect.move_ip(40,0)
                elif pressed_key[K_UP]:
                    self.rect.move_ip(0,40)
                elif pressed_key[K_DOWN]:
                    self.rect.move_ip(0,-40)
                if pressed_key[K_KP6]:
                    for j in range(8):
                        self.horseImg[j] = pygame.transform.rotate(self.horseImg[j],90)
                    self.rect = self.horseImg[i].get_rect(bottomright = (self.x,self.y))
                elif pressed_key[K_KP8]:
                    for j in range(8):
                        self.horseImg[j] = pygame.transform.rotate(self.horseImg[j],-90)
                    self.rect = self.horseImg[i].get_rect(bottomright = (self.x,self.y))
                
class Track(object):
    def __init__(self,pos):
        tracks.append(self)
        self.rect = pygame.Rect(pos[0],pos[1],100,100)

def messege(msg,color):
    font_style = pygame.font.SysFont(None,50)
    msg = font_style.render(msg,True,color)
    gameDisplay.blit(msg, [displayWidth/2-100,displayHeight/2-10])

horse = Horse()
tracks = [] 

def gameLoop():
    board = [[0,0,0,0,0,0,0,0,0],
            [0,1,1,1,0,0,1,1,0],
            [0,1,1,1,0,0,1,1,0],
            [0,1,1,1,0,0,1,1,0],
            [0,1,1,1,0,0,1,1,0],
            [0,1,1,1,0,0,1,1,0],
            [0,0,0,0,0,0,0,0,0]]
            
    posX = posY = 0        
    for row in board:
        for column in row:
            if column == 1:
                Track((posX,posY))
            posX += 100
        posY += 100; posX = 0

    i = 0;j=0; k = 1
    game = True
    
    while game:
        
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    game = False
            elif event.type == QUIT:
                game = False

        pressed_key = pygame.key.get_pressed()           
        gameDisplay.fill(white)
           
        for track in tracks:
            pygame.draw.rect(gameDisplay,green,track.rect)
        
        horse.update(pressed_key,i)
        gameDisplay.blit(horse.horseImg[i],horse.rect)   
        i += 1
        if i == 7:
            i = 0
        
        pygame.display.update()
        clock.tick(8)         

messege('Loading...',green)
pygame.display.update()
time.sleep(0.5)
gameLoop()

pygame.quit()
quit()

