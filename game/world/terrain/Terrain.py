import pygame
from game.Game import Game

class Terrain(pygame.sprite.Sprite):
    '''Generic class for all terrain including platforms and walls'''
    
    src_path = 'sprites/world/'
    top_clip = False
    right_clip = False
    bottom_clip = False
    left_clip = False
    
    def __init__(self, location, pos, src, width, height):
        '''first parameter can be colour or image'''
        super(Terrain, self).__init__()
        self.pos = pos
        self.width = width
        self.height = height
        
        self.image = pygame.Surface([self.width, self.height])
        
        if not isinstance(src, basestring):
            self.image.fill(src)
        
        self.rect = self.image.get_rect()
        
        Game.addSprite('terrain', self)
        location.terrain.append(self)
    
    def draw(self, screen):
        screen.blit(self.image, self.pos)
    
    def onTerrain(self, character):
        if self.top_clip == False:
            return False
        if self.onTop(character) and self.inBoundry(character):
            return True
        return False
    
    def inBoundry(self, character):
        return self.inLeftBoundry(character) and self.inRightBoundry(character)
    
    def inLeftBoundry(self, character):
        return character.pos[0] + character.src_width > self.pos[0]
    
    def inRightBoundry(self, character):
        return character.pos[0] < self.pos[0] + self.width
    
    def onTop(self, character):
        boundry = self.pos[1] - (character.move_y + character.vel_y)
        return character.foot_pos <= self.pos[1] + 5 and character.foot_pos >= boundry
        
    def againstLeft(self, character):
        if self.left_clip == False:
            return False
        if character.left_pos >= self.pos[0] and character.left_pos <= self.pos[0] + self.width:
            return self.vertBoundry(character)
        return False
    
    def againstRight(self, character):
        if self.right_clip == False:
            return False
        if character.pos[0] <= self.pos[0] + self.width and character.pos[0] >= self.pos[0]:
            return self.vertBoundry(character)
        return False        
    
    def vertBoundry(self, character):
        return character.foot_pos > self.pos[1] and character.pos[1] < self.pos[1] + self.height