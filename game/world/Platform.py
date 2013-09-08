import pygame

from game.world.Terrain import Terrain

class Platform(Terrain):
    
    top_clip = True
    
    def __init__(self, pos, src, width, height):
        super(Platform, self).__init__(pos, src, width, height)
    
    def onPlatform(self, player):
        if self.top_clip == False:
            return False
        if player.foot_pos <= self.pos[1] and player.foot_pos > self.pos[1] - player.vel_y:
            return True
        
        return False
    