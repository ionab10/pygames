import pygame, sys
from random import *



size = width, height = 640, 480
screen = pygame.display.set_mode(size)
screen.fill([255, 255, 255])
#img_file = "blue_ball.png"


location = [50, 50]
speed = (2, 2)

x = 50
y = 50
x_speed = 10
y_speed = 20

ball = pygame.image.load("blue_ball.png")
#brick = SpriteClass("brick.png")



while True:


    pygame.time.delay(20)
    screen.fill([255, 255, 255])
   # screen.blit(brick.image, brick.rect)

    x += x_speed
    y += y_speed

    

    screen.blit(ball, [x,y])
    pygame.display.flip()
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


    
