import pygame
from game.world.terrain.Wall import Wall

class SideDoor(Wall):
    
    door_open = False
    
    @property
    def left_clip(self):
        return self.door_open
    
    @property
    def right_clip(self):
        return self.door_open
    
    def __init__(self, level, pos, width, height):
        src = (100,100,100)
        super(Wall, self).__init__(level, pos, src, width, height)
