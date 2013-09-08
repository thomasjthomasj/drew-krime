import pygame
from game.visuals.Sprite import Sprite
from game.Game import Game

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
    location = False
    
    # Toggles
    sneak = False
    
    @property
    def foot_pos(self):
        return self.pos[1] + self.src_height
    
    def __init__(self, src, pos):
        super(Character, self).__init__(src, pos)
        
    def checkHealth(self):
        if self.health <= 0 or self.pos[1] > self.location.dimensions[1]:
            self.dead = True
            
    def jump(self):
        if self.location.getPlatform(self):
            self.vel_y = 0 - (1 + self.level_jump / 2)
    
    def applyPhysics(self):
        self.move_y = self.move_y + self.vel_y
        platform = self.location.getPlatform(self)
        if platform and self.vel_y >= 0:
            self.vel_y = 0
            self.move_y = 0
            self.pos[1] = platform.pos[1] - self.src_height + 5
        else:
            self.vel_y += Game.gravity
    