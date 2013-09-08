import pygame
import random

from game.world.Platform import Platform
from game.Game import Game

class BaseLocation(object):
    
    player = False
    platforms = []
    
    @property
    def dimensions(self):
        return Game.getDimensions()
    
    def __init__(self, player):
        self.player = player
        self.buildPlatforms()
        
    def buildPlatforms(self):
        dimensions = Game.getDefaultDimensions()
        platform1_pos = (50, dimensions[1] - 100)
        platform1 = Platform(platform1_pos, (153,25,190), 400, 50)
        platform2_pos = (500, dimensions[1] - 30)
        platform2 = Platform(platform2_pos, (200,155,19), 300, 20)
        platform3_pos = (dimensions[0] - 80, dimensions[1] - 40)
        platform3 = Platform(platform3_pos, (20,155,19), 85, 20)
        self.platforms.append(platform1)
        self.platforms.append(platform2)
        
    def getPlatform(self, character):
        for platform in self.platforms:
            if platform.onPlatform(character):
                return platform
        
        return False
    