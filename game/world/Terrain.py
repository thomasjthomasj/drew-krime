import pygame
from game.Game import Game

class Terrain(pygame.sprite.Sprite):
    '''Generic class for all terrain including platforms and walls'''
    
    src_path = 'sprites/world/'
    top_clip = False
    right_clip = False
    bottom_clip = False
    left_clip = False
    
    def __init__(self, pos, src, width, height):
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
    
    def draw(self, screen):
        screen.blit(self.image, self.pos)