import pygame, sys
from pygame.locals import *
import time

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400,300))

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0 , 128)

DISPLAYSURF.fill(WHITE)

fontObj = pygame.font.Font('freesansbold.ttf', 32)
textSurfaceObj = fontObj.render("testing out some music", True, GREEN, BLUE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (200, 150)

while True:
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)

    musicObj = pygame.mixer.music
    musicObj.load("D:/Code/PollutionModellingProject/Assets/bleep-41488.mp3")
    musicObj.play()
    time.sleep(1)
    musicObj.stop()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.update()