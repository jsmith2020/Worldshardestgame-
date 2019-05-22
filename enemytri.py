import pygame, sys, random
from pygame.locals import*
ENEMYTRI = pygame.image.load('enemytri.png')
class enemyt(pygame.sprite.Sprite):
    #Initialize the attributes related to the trex's position (x and y coords), image, and rectangle hitbox
    def __init__(self):
        #Calls the Sprite class constructor.
        #It must be the first line in constructor.
        super().__init__()
        #add something to this function to what you have in trex.py
        self.image = ENEMYTRI
        self.rect = pygame.Rect(180,180,25,25)
        self.rect.x = 180
        self.rect.y = 180
        #Don't forget to add rect and image attributes!

    #Changes the cactus's horizontal location
    '''def move(self):
        if self.rect.x > -100:
            self.rect.x = self.rect.x-5
            self.rect.x = self.rect.x
            self.rect.y = 200
        elif self.rect.x <= -100:
            self.rect.x = 500'''
