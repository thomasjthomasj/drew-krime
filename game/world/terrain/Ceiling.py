import pygame
from game.world.terrain.Terrain import Terrain

class Ceiling(Terrain):
    
    bottom_clip = True
    top_clip = True
    #left_clip = True
    #right_clip = True
    
    def __init__(self, location, pos, src, width, height):
        super(Ceiling, self).__init__(location, pos, src, width, height)
    