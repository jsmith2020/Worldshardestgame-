import pygame, sys, random
from pygame.locals import*
MAINCUBE = pygame.image.load('mainchar.png')
class maincube(pygame.sprite.Sprite):
    #Initialize the attributes related to the trex's position (x and y coords), image, and rectangle hitbox
    def __init__(self):
        #Calls the Sprite class constructor.
        #It must be the first line in constructor.
        super().__init__()
        self.x = 20
        self.y = 20


        def up(self):
            self.rect.y = self.rect.y-25
            self.rect.x = self.x_coord
        def down(self):
            self.rect.y = self.rect.y+25
            self.rect.x = slef.x_coord
