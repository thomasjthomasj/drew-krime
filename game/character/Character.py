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
    def left_pos(self):
        return self.pos[0] + self.width
    
    def __init__(self, src, pos):
        super(Character, self).__init__(src, pos)
        
    def checkHealth(self):
        if self.health <= 0 or self.pos[1] > self.location.dimensions[1]:
            self.dead = True
            
    def jump(self):
        if self.location.getTerrain(self):
            self.vel_y = 0 - (1 + self.level_jump / 2)
                
    def moveLeft(self, speed):
        if self.location.againstTerrainLeft(self) == False:
            self.move_x = self.move_x - speed
    
    def moveRight(self, speed):
        if self.location.againstTerrainRight(self) == False:
            self.move_x = self.move_x + speed
    
    def moveX(self):
        dimensions = Game.getDimensions()
        if self.pos[0] >= 0 and self.move_x < 0:
            self.pos[0] += self.move_x
        elif self.pos[0] <= (dimensions[0] - self.src_width) and self.move_x > 0:
            self.pos[0] += self.move_x
    
    def applyPhysics(self):
        self.move_y = self.move_y + self.vel_y
        terrain = self.location.getTerrain(self)
        if terrain and self.vel_y >= 0:
            self.vel_y = 0
            self.move_y = 0
            self.pos[1] = terrain.pos[1] - self.src_height + 5
        else:
            self.vel_y += Game.gravity
    