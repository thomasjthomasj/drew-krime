import pygame
from game.world.terrain.Platform import Platform

class Wall(Platform):
    
    left_clip = True
    right_clip = True
    
    def __init__(self):
        super(Wall, self).__init__(level, pos, src, width, height)