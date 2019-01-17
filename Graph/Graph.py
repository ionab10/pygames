import pygame, sys
import easygui
from pygame.locals import *
#import numpy



pygame.init()
size = width, height = 640, 480
screen = pygame.display.set_mode(size)
screen.fill([255, 255, 255])


func = easygui.enterbox(msg="y =", title="Graph", default="")



if 'x' in func:
    pos = func.index('x')
    terms = func.split('x')
    if pos == 0:
        m = 1
    else:
        m = float(terms[0])
    #if terms[1].startswith('^')


points = []
for i in range(0, 640):
    points.append(m*(i-320) + float(terms[1]))

print(points)

"""
# Loop over rows.
for row in elements:
    # Loop over columns.
    for column in row:
        print(column)
    print("\n")
"""
font = pygame.font.Font(None,20)

while 1:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


    #pygame.time.delay(20)
    screen.fill([255, 255, 255])

    pygame.draw.aaline(screen, [0,0,0], (0,height/2),(width,height/2))
    pygame.draw.aaline(screen, [0,0,0], (width/2,0),(width/2,height))
    screen.blit(font.render(("x"), 1, (0,0,0)), [width - 10, height/2 - 20])
    screen.blit(font.render(("y"), 1, (0,0,0)), [width/2 + 5, 5])
    
    for x in range(0,639):
        pygame.draw.aaline(screen, [255,0,0], (x,height/2-points[x]),(x+1,height/2-points[x+1]))

    pygame.display.flip()
    
