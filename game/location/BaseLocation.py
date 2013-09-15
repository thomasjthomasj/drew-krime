import pygame
from random import randint

from game.world.terrain.Platform import Platform
from game.world.terrain.Wall import Wall
from game.world.terrain.room.Room import Room
from game.world.terrain.door.SideDoor import SideDoor
from game.Game import Game
from game.character.TestEnemy import TestEnemy

class BaseLocation(object):
    
    player = False
    terrain = []
    enemies = []
    bullets = []
    
    @property
    def dimensions(self):
        return Game.getDimensions()
    
    @property
    def random_colour(self):
        return (randint(0, 255), randint(0, 255), randint(0, 255))
    
    def __init__(self, player):
        self.player = player
        self.buildLevel()
        self.setEnemies()
        
    def buildLevel(self):
        dimensions = Game.getDefaultDimensions()
        platform1_pos = (50, dimensions[1] - 100)
        platform1 = Platform(self, platform1_pos, self.random_colour, 400, 50)
        room = Room(self, (self.dimensions[0] / 4, self.dimensions[1] / 3 + 100), (400,200), (10,10,30,10), True, False)
        room.buildFloor((255,255,255))
        room.buildWalls((255,0,0), (0,255,0))
        room.buildCeiling((0,0,255))
    
    def setEnemies(self):
        enemy = TestEnemy(self, (100, self.dimensions[1] - 600))
        
    def againstTerrainLeft(self, sprite):
        for terrain in self.terrain:
            if terrain.againstLeft(sprite):
                return True
        return False
    
    def againstTerrainRight(self, sprite):
        for terrain in self.terrain:
            if terrain.againstRight(sprite):
                return True
        return False
        
    def toggleDoor(self, character):
        for terrain in self.terrain:
            if isinstance(terrain, SideDoor):
                terrain.toggleDoor(character)
        
    def getTerrain(self, sprite):
        for terrain in self.terrain:
            if terrain.onTerrain(sprite):
                return terrain
        return False
    
    def touchCeiling(self, sprite):
        for terrain in self.terrain:
            if terrain.touchCeiling(sprite):
                sprite.pos[1] = terrain.pos[1] + terrain.height
                return True
        return False
    
    def hitTerrain(self, sprite):
        for terrain in self.terrain:
            if terrain.touchCeiling(sprite):
                return True
            #if terrain.onTerrain(sprite):
            #    return True
            if terrain.againstRight(sprite):
                return True
            if terrain.againstLeft(sprite):
                return True
    