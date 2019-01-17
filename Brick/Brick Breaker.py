"""
Brick Breaker

Iona Buchanan
2015
"""


import pygame, sys, math
from random import *
from pygame.locals import *

class BallClass(pygame.sprite.Sprite):                          #Ball class
    def __init__(self, image_file, location, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed

    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > screen.get_width():
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0:
            self.speed[1] = -self.speed[1]


class PadClass(pygame.sprite.Sprite):                           #paddle
    def __init__(self, location = [0,0]):
        pygame.sprite.Sprite.__init__(self)
        image_surface = pygame.surface.Surface([100,20])
        image_surface.fill([0,0,0])
        self.image = image_surface.convert()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

class BrickClass(pygame.sprite.Sprite):                         #bricks
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

class RedBrickClass(pygame.sprite.Sprite):                         #bricks
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

pygame.init()
size = width, height = 1080, 640
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

font = pygame.font.Font(None,70)


ball = BallClass("blue_ball.png", [540, 300], [1, 10])          #ball
ballGroup = pygame.sprite.Group(ball)

paddle = PadClass([500,600])            #paddle

bricks = pygame.sprite.Group()          #bricks
for row in range(0,3):
    for column in range(0,6):
        location = [column*180 + 10, row*90 + 10]
        brick = BrickClass("brick.png", location)
        bricks.add(brick)

"""
redbricks = pygame.sprite.Group()
for row in range(0,2):
    for column in range(0,3):
        location = [column*360 + 10, row*180 + 10]
        redbrick = BrickClass("red_brick.png", location)
        redbricks.add(redbrick)
"""


lives = 3


while 1:
    clock.tick(30)
    screen.fill([255, 255, 255])

    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEMOTION:  #mouse control
            paddle.rect.centerx = event.pos[0]

    if pygame.sprite.spritecollide(paddle,ballGroup, False):        #ball hits paddle
        ball.speed[1] = -ball.speed[1]
        diffx = paddle.rect.centerx - ball.rect.centerx
        if diffx > 0:
            ball.speed[0] = -math.fabs(ball.speed[0]*diffx/15)
        elif diffx < 0:
            ball.speed[0] = math.fabs(ball.speed[0]*diffx/15)
        #ball.speed[1] = -math.sqrt(121 - math.pow(ball.speed[0],2))

    for brick in bricks:
        if pygame.sprite.spritecollide(brick,ballGroup, False):     #ball hits bricks
            ball.speed[0] = -ball.speed[0]
            ball.speed[1] = -ball.speed[1]
            bricks.remove(brick)                    #brick dissapears
        """if pygame.sprite.spritecollide(redbrick,ballGroup, False):     #ball hits redbricks
            ball.speed[0] = -ball.speed[0]
            ball.speed[1] = -ball.speed[1]
            redbricks.remove(redbrick)   """             #brick dissapears
    if  bricks.has() == Falses:                   #no bricks left 
        win_txt = font.render("YOU WIN!", 1, (0,0,0))
        screen.blit(win_txt, [screen.get_width()/2 - win_txt.get_width()/2,300])
        

    if ball.rect.top >= screen.get_height():
        lives = lives - 1
        if lives == 0:              #game over
            gameover_txt = font.render("Game Over", 1, (0,0,0))
            screen.blit(gameover_txt, [screen.get_width()/2 - gameover_txt.get_width()/2,300])
            pygame.display.flip()
            pygame.time.delay(4000)
            sys.exit()
        else:
            pygame.time.delay(2000)         #new ball
            ball.rect.topleft = [540,300]
            ball.speed = [1,10]
    lives_txt = font.render(str(lives), 1, (0,0,0))
    screen.blit(lives_txt, [1020,10])

    ball.move()
    
    screen.blit(ball.image, ball.rect)          #display
    screen.blit(paddle.image, paddle.rect)
    for brick in bricks:
        screen.blit(brick.image, brick.rect)
    """for redbrick in redbricks:
        screen.blit(redbrick.image, redbrick.rect)"""

    pygame.display.flip()
    




    
