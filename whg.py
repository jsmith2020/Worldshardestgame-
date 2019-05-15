#Sets FPS and starts game clock/
import pygame, sys, random
from pygame.locals import*
#Always call before utilizing pygame functions
pygame.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 30
BASICFONT = pygame.font.Font('freesansbold.ttf', 16)
fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((400,300), 0, 32)
#Sets title of GUI frame
t=0
pygame.display.set_caption("Wolrds Hardest Game In The World")

maincube = pygame.image.load('mainchar.png')
maincube_x = 160
maincube_y = 160 #Display png/jpg image at the coordinate specified.
from maincube import maincube
square = maincube()
coin = pygame.image.load('coin.png')
enemytri = pygame.image.load('enemytri.png')
#sets images for sprits
#sets caption
def update(p):
    DISPLAYSURF.blit(p.image,p.rect)

while True: #main game loop
	#An event can be a keyboard key or mouse moving, etc.
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(maincube, (maincube_x, maincube_y))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_UP:
                square.up()
                DISPLAYSURF.blit(cube.image, cube.rect)




    #Draws the surface object returned by pygame.display.set_mode(). It essentially repaints our canvas based on the updated game state.
    pygame.display.update()
