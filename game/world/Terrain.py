import pygame

class Terrain(pygame.sprite.Sprite):
    '''Generic class for all terrain including platforms and walls'''
    
    src_path = 'sprites/world/'
    
    def __init__(self, src, width, height):
        '''first parameter can be colour or image'''
        super(Terrain, self).__init__()
        
        self.image = pygame.Surface([width, height])
        
        if isinstance(src, basestring):
            self.image.fill(src)
        
        self.rect = self.image.get_rect()