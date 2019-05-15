import pygame, sys, random
from pygame.locals import*
ENEMYTRI = pygame.image.load('enemytri.png')
class maincube(pygame.sprite.Sprite):
    #Initialize the attributes related to the trex's position (x and y coords), image, and rectangle hitbox
    def __init__(self):
        #Calls the Sprite class constructor.
        #It must be the first line in constructor.
        super().__init__()
        self.x = 80
        self.y = 20
