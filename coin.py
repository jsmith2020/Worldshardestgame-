import pygame, sys, random
from pygame.locals import*
COIN = pygame.image.load('coin.png')
class coin(pygame.sprite.Sprite):
    #Initialize the attributes related to the trex's position (x and y coords), image, and rectangle hitbox
    def __init__(self, ground):
        #Calls the Sprite class constructor.
        #It must be the first line in constructor.
        super().__init__()
        self.x = 60
        self.y = ground
        self.ground = ground
