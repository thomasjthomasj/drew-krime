import pygame

from game.world.Terrain import Terrain
from game.Game import Game

class Platform(Terrain):
    
    top_clip = True
    
    def __init__(self, pos, src, width, height):
        super(Platform, self).__init__(pos, src, width, height)
    
    def onPlatform(self, character):
        if self.top_clip == False:
            return False
        if self.onTop(character) and self.inBoundry(character):
            return True
        return False
    
    def inBoundry(self, character):
        return self.inLeftBoundry(character) and self.inRightBoundry(character)
    
    def inLeftBoundry(self, character):
        return character.pos[0] - character.src_width > self.pos[0]
    
    def inRightBoundry(self, character):
        return character.pos[0] < self.pos[0] + self.width
    
    def onTop(self, character):
        boundry = self.pos[1] - (character.move_y - character.vel_y)
        return character.foot_pos <= self.pos[1] and character.foot_pos >= boundry