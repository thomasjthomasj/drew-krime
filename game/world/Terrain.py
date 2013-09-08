import pygame
from game.Game import Game

class Terrain(pygame.sprite.Sprite):
    '''Generic class for all terrain including platforms and walls'''
    
    src_path = 'sprites/world/'
    
    def __init__(self, pos, src, width, height):
        '''first parameter can be colour or image'''
        super(Terrain, self).__init__()
        self.pos = pos
        
        self.image = pygame.Surface([width, height])
        
        if not isinstance(src, basestring):
            self.image.fill(src)
        
        self.rect = self.image.get_rect()
        
        Game.addSprite('terrain', self)
    
    def draw(self, screen):
        screen.blit(self.image, self.pos)