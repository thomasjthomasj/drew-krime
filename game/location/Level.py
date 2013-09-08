import pygame
import random

from game.world.Platform import Platform
from game.Game import Game

class Level(object):
    
    player = False
    platforms = []
    
    def __init__(self, player):
        self.player = player
        self.buildPlatforms()
        
    
    def buildPlatforms(self):
        dimensions = Game.getDefaultDimensions()
        pos = (50, dimensions[1] - 100)
        platform = Platform(pos, (153,25,190), 400, 50)
        self.platforms.append(platform)