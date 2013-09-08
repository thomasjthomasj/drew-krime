import pygame
from game.visuals.Sprite import Sprite

class Character(Sprite):
    
    invinsible = False
    dead = False
    health = 1
    z_index = 5
    
    move_x = 0
    move_y = 0
    vel_y = 0
    walk_speed = 4
    sneak_speed = 2
    direction = 'right'
    
    @property
    def foot_pos(self):
        return self.pos[1] + self.src_height
    
    def __init__(self, src, pos):
        super(Character, self).__init__(src, pos)
        
    def checkHealth(self):
        if self.health <= 0:
            self.dead = True
    
    