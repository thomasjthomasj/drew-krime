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
        self.src = src
        
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
    
    def inBoundry(self, sprite):
        return self.inLeftBoundry(sprite) and self.inRightBoundry(sprite)
    
    def inLeftBoundry(self, sprite):
        return sprite.pos[0] + sprite.src_width > self.pos[0]
    
    def inRightBoundry(self, sprite):
        return sprite.pos[0] < self.pos[0] + self.width
    
    def onTop(self, sprite):
        boundry = self.pos[1] - (sprite.move_y)
        return sprite.base_pos <= self.pos[1] + 5 and sprite.base_pos >= boundry
        
    def againstLeft(self, sprite):
        if self.left_clip == False:
            return False
        if sprite.left_pos >= self.pos[0] and sprite.left_pos <= self.pos[0] + self.width:
            return self.vertBoundry(sprite)
        return False
    
    def againstRight(self, sprite):
        if self.right_clip == False:
            return False
        if sprite.pos[0] <= self.pos[0] + self.width and sprite.pos[0] >= self.pos[0]:
            return self.vertBoundry(sprite)
        return False        
    
    def vertBoundry(self, sprite):
        return sprite.base_pos > self.pos[1] and sprite.pos[1] < self.pos[1] + self.height
    
    def touchCeiling(self, sprite):
        if self.bottom_clip == False:
            return False
        if self.inBoundry(sprite):
            return self.pos[1] <= sprite.pos[1] <= self.pos[1] + self.height
        return False
    