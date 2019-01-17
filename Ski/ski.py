"""
Ski

Iona Buchanan
2015
"""


import pygame, sys, math
from random import *
from pygame.locals import *

class TreeClass(pygame.sprite.Sprite):                          #Ball class
    def __init__(self, image_file, location, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed

    def move(self):
        self.rect = self.rect.move(self.speed)


class SkierClass(pygame.sprite.Sprite):                         #skier
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


skier = SkierClass("blue_ball.png", [540, 300])          #skier
#skier = pygame.sprite.Group(ball)


trees = pygame.sprite.Group()          #bricks
for row in range(0,3):
    for column in range(0,6):
        location = [column*180 + 10, row*90 + 10]
        tree = TreeClass("brick.png", location, [0,5])
        trees.add(tree)


lives = 3


while 1:
    clock.tick(30)
    screen.fill([255, 255, 255])

    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEMOTION:  #mouse control
            skier.rect.centerx = event.pos[0]

    for tree in trees:
        if pygame.sprite.spritecollide(tree,skier, False):     #skier hits tree
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

        """
        win_txt = font.render("YOU WIN!", 1, (0,0,0))
        screen.blit(win_txt, [screen.get_width()/2 - win_txt.get_width()/2,300])"""
        



    tree.move()
    
    screen.blit(skier.image, skier.rect)          #display
    for tree in trees:
        screen.blit(tree.image, tree.rect)

    pygame.display.flip()
    




    
