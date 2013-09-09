import pygame
from random import randint

from game.world.terrain.Platform import Platform
from game.world.terrain.Wall import Wall
from game.Game import Game

class BaseLocation(object):
    
    player = False
    platforms = []
    
    @property
    def dimensions(self):
        return Game.getDimensions()
    
    @property
    def random_colour(self):
        return (randint(0, 255), randint(0, 255), randint(0, 255))
    
    def __init__(self, player):
        self.player = player
        self.buildLevel()
        
    def buildLevel(self):
        dimensions = Game.getDefaultDimensions()
        platform1_pos = (50, dimensions[1] - 100)
        platform1 = Platform(self, platform1_pos, self.random_colour, 400, 50)
        platform2_pos = (randint(0, dimensions[0]), randint(0, dimensions[1]))
        platform2 = Platform(self, platform2_pos, self.random_colour, 300, 20)
        platform3_pos = (dimensions[0] - 80, dimensions[1] - 40)
        platform3 = Platform(self, platform3_pos, self.random_colour, 85, 20)
        self.platforms.append(platform1)
        self.platforms.append(platform2)
        self.platforms.append(platform3)
        
    def getPlatform(self, character):
        for platform in self.platforms:
            if platform.onPlatform(character):
                return platform
        
        return False
    