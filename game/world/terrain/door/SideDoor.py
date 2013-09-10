import pygame
from game.world.terrain.Wall import Wall

class SideDoor(Wall):
    
    door_closed = True
    locked = False
    top_clip = False
    open_range = 5
    
    @property
    def left_clip(self):
        return self.door_closed
    
    @property
    def right_clip(self):
        return self.door_closed
    
    def __init__(self, location, pos, width, height):
        src = (100,100,100)
        super(SideDoor, self).__init__(location, pos, src, width, height)
        
    def toggleDoor(self, character):
        if self.door_closed:
            self.openDoor(character)
        else:
            self.closeDoor(character)
        
    def openDoor(self, character):
        if self.canOpenFromRight(character) or self.canOpenFromLeft(character):
            self.door_closed = False
            self.width = self.width * 2
            self.image = pygame.Surface([self.width, self.height])
            self.image.fill(self.src)
    
    def closeDoor(self, character):
        if self.canCloseFromRight(character) or self.canCloseFromLeft(character):
            self.door_closed = True
            self.width = self.width / 2
            self.image = pygame.Surface([self.width, self.height])
            self.image.fill(self.src)
    
    def canOpenFromLeft(self, character):
        if character.direction == 'left':
            return False
        character_right = character.pos[0] + character.width
        if self.pos[0] - self.open_range <= character_right <= self.pos[0] + self.open_range:
            return self.doorOpenVertRange(character)
        return False
    
    def canOpenFromRight(self, character):
        if character.direction == 'right':
            return False
        right = self.pos[0] + self.width
        if right - self.open_range <= character.pos[0] <= right + self.open_range:
            return self.doorOpenVertRange(character)
        return False
    
    def canCloseFromRight(self, character):
        if character.direction == 'right':
            return False
        if self.pos[0] - self.open_range <= character.pos[0] <= self.pos[0] + self.width + self.open_range:
            return self.doorOpenVertRange(character)
        return False
    
    def canCloseFromLeft(self, character):
        if character.direction == 'left':
            return False
        character_right = character.pos[0] + character.width
        if self.pos[0] - self.open_range <= character_right <= self.pos[0] + self.width + self.open_range:
            return self.doorOpenVertRange(character)
        return False

    def doorOpenVertRange(self, character):
        character_pos = character.centre_pos[1]
        bottom_pos = self.pos[1] + self.height
        return character_pos >= self.pos[1] and character_pos <= bottom_pos