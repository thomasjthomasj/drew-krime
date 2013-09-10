import pygame
from game.world.terrain.Wall import Wall

class SideDoor(Wall):
    
    door_open = False
    top_clip = False
    
    @property
    def left_clip(self):
        return self.door_open
    
    @property
    def right_clip(self):
        return self.door_open
    
    def __init__(self, location, pos, width, height):
        src = (100,100,100)
        super(SideDoor, self).__init__(location, pos, src, width, height)