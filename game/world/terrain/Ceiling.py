import pygame
from game.world.terrain.Wall import Wall

class Ceiling(Wall):
    
    bottom_clip = True
    
    def __init__(self, level, pos, src, width, height):
        super(Ceiling, self).__init__(level, pos, src, width, height)
    