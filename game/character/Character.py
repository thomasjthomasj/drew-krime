import pygame
from game.visuals.Sprite import Sprite

class Character(Sprite):
    
    invinsible = False
    dead = False
    health = 1
    z_index = 5
    
    def __init__(self, src, pos):
        super(Character, self).__init__(src, pos)
        
    def checkHealth(self):
        if self.health <= 0:
            self.dead = True
    
    