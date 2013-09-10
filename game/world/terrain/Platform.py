import pygame

from game.world.terrain.Terrain import Terrain
from game.Game import Game

class Platform(Terrain):
    
    top_clip = True
    
    def __init__(self, location, pos, src, width, height):
        super(Platform, self).__init__(location, pos, src, width, height)