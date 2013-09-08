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
    
    @property
    def grounded(self):
        if self.foot_pos >= self.location.ground_level:
            return True
        return self.on_platform
    
    @property
    def floor_level(self):
        if self.on_platform:
            return self.platform.pos[1]
        return self.location.ground_level
    
    @property
    def on_platform(self):
        for platform in self.location.platforms:
            if platform.onPlatform(self):
                self.platform = platform
                return True
        
        return False
    
    def __init__(self, src, pos):
        super(Character, self).__init__(src, pos)
        
    def checkHealth(self):
        if self.health <= 0:
            self.dead = True
            
    def jump(self):
        if self.grounded == True:
            self.vel_y = 0 - (1 + self.level_jump / 2)
    
    def applyPhysics(self):
        self.move_y = self.move_y + self.vel_y
        if self.grounded and self.vel_y >= 0:
            self.vel_y = 0
            self.move_y = 0
            self.pos[1] = self.floor_level - self.src_height
        else:
            self.vel_y += Game.gravity
    