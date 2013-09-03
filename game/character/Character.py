import pygame
from game.visuals.Sprite import Sprite

class Character(Sprite):
    
    invinsible = False
    
    def __init__(self, src, pos):
        super(Character, self).__init__(src, pos)