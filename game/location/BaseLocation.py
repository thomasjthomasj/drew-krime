import pygame
from random import randint

from game.world.terrain.Platform import Platform
from game.world.terrain.Wall import Wall
from game.world.terrain.room.Room import Room
from game.Game import Game

class BaseLocation(object):
    
    player = False
    terrain = []
    
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
        room = Room(self, (self.dimensions[0] / 4, self.dimensions[1] / 3), (400,300), (10,10,30,10), True, False)
        room.buildFloor((255,255,255))
        room.buildWalls((255,0,0), (0,255,0))
        room.buildCeiling((0,0,255))
        
    def againstTerrainLeft(self, character):
        for terrain in self.terrain:
            if terrain.againstLeft(character):
                return True
        return False
    
    def againstTerrainRight(self, character):
        for terrain in self.terrain:
            if terrain.againstRight(character):
                return True
        return False
        
    def getTerrain(self, character):
        for terrain in self.terrain:
            if terrain.onTerrain(character):
                return terrain
        return False
    