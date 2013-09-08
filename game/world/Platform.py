import pygame

from game.world.Terrain import Terrain

class Platform(Terrain):
    
    def __init__(self, pos, src, width, height):
        super(Platform, self).__init__(pos, src, width, height)