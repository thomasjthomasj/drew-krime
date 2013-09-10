import pygame
from game.world.terrain.Terrain import Terrain

class Wall(Terrain):
    
    left_clip = True
    right_clip = True
    top_clip = True
    
    def __init__(self, location, pos, src, width, height):
        super(Wall, self).__init__(location, pos, src, width, height)
