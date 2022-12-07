import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30
fpsClock = pygame.time.Clock()

#set up the window
DISPLAYSURF = pygame.display.set_mode((1000,800), 0, 32)
pygame.display.set_caption('Animation')

WHITE = (255, 255, 255)
mitsImg = pygame.image.load('D:/Code/PollutionModellingProject/Assets/1670392999326.jpg')
mitsx = 10
mitsy = 10
direction = 'right'

while True: # the main game loop
    DISPLAYSURF.fill(WHITE)

    if direction == 'right':
        mitsx += 5
        if mitsx == 500:
            direction = 'down'
    elif direction == 'down':
        mitsy += 5
        if mitsy == 500:
            direction = 'left'
    elif direction == 'left':
        mitsx -= 5
        if mitsx == 10:
            direction = 'up'
    elif direction == 'up':
        mitsy -= 5
        if mitsy == 10:
            direction = 'right'
    
    DISPLAYSURF.blit(mitsImg, (mitsx,mitsy))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    fpsClock.tick(FPS)
    pygame.display.update()