import pygame, sys, random
from pygame.locals import*
MAINCUBE = pygame.image.load('mainchar.png')
class maincube(pygame.sprite.Sprite):
    #Initialize the attributes related to the trex's position (x and y coords), image, and rectangle hitbox
    def __init__(self):
        #Calls the Sprite class constructor.
        #It must be the first line in constructor.
        super().__init__()
        self.image = MAINCUBE
        self.rect = pygame.Rect(50,250,25,25)
        self.rect.x = 50
        self.rect.y = 250

    def up(self):
        self.rect.y = self.rect.y-10
        self.rect.x = self.rect.x
    def down(self):
        self.rect.y = self.rect.y+10
        self.rect.x = self.rect.x
    def right(self):
        self.rect.y = self.rect.y
        self.rect.x = self.rect.x-10
    def left(self):
        self.rect.y = self.rect.y
        self.rect.x = self.rect.x+10
