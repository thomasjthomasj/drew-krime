import pygame
import game.world.terrain
from game.world.terrain.door.SideDoor import SideDoor

class Room(object):
    
    location = False
    dimensions = [0,0]
    pos = [0,0]
    
    '''(top, right, bottom, left)'''
    borders = [0,0,0,0]
    
    left_door = False
    right_door = False
    ceiling = False
    floor = False
    left_wall = False
    right_wall = False
    
    @property
    def floor_level(self):
        return self.pos[1] + self.dimensions[1] - self.borders[2]
    
    @property
    def ceiling_level(self):
        return self.pos[1] + self.borders[0]
    
    @property
    def wall_height(self):
        return self.floor_level - self.ceiling_level
    
    @property
    def door_height(self):
        return self.location.player.src_height + 30
    
    def __init__(self, location, pos, dimensions, borders, left_door = False, right_door = False):
        '''Class for generating rooms'''
        self.location = location
        self.pos = pos
        self.dimensions = dimensions
        self.borders = borders
        self.left_door = left_door
        self.right_door = right_door
        
    def buildFloor(self, src, ceiling = False):
        pos = (self.pos[0], self.floor_level)
        if ceiling:
            self.floor = terrain.Ceiling(self.location, pos, src, dimensions[0], borders[2])
        self.floor = terrain.Platform(self.location, pos, src, borders[2], dimensions[0])
    
    def buildCeiling(self, src):
        self.ceiling = terrain.Ceiling(self.location, self.pos, src, dimensions[0], borders[0])
    
    def buildWalls(self, leftSrc, rightSrc):
        self.buildLeftWall(leftSrc)
        self.buildRightWall(rightSrc)
        
    def buildLeftWall(self, src):
        wall_pos = (self.pos[0], ceiling_level)
        if self.left_door:
            door_pos = (self.pos[0], self.floor_level - self.door_height)
            wall_height = self.wall_height - self.door_height
            self.left_door = SideDoor(self.location, door_pos, borders[3], self.door_height)
            self.left_wall = terrain.Wall(self.location, wall_pos, src, borders[3], wall_height)
            return
        self.left_wall = terrain.Wall(self.location, wall_pos, src, borders[3], self.wall_height)
        
    def buildRightWall(self, src):
        wall_pos = (self.dimensions[0] - borders[1], ceiling_level)
        if self.right_door:
            door_pos = (self.dimensions[0] - borders[1], self.floor_level - self.door_height)
            wall_height = self.wall_height - self.door_height
            self.right_door = SideDoor(self.location, door_pos, borders[1], self.door_height)
            self.right_wall = terrain.Wall(self.location, wall_pos, src, borders[1], wall_height)
            return
        self.right_wall = terrain.Wall(self.location, wall_pos, src, borders[1], self.wall_height)
        
        
        
        
        
        
        
        