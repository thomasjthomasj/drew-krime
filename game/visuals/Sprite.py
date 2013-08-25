import pygame

class Sprite(pygame.sprite.Sprite):
    
    def __init__(self, src, pos):
        super(Sprite, self).__init__()
        self.pos = pos
        self.src_image = pygame.image.load(src).convert_alpha()
        self.src_width, self.src_height = self.src_image.get_size()
        self.image = self.src_image
        self.rect = self.src_image.get_rect()
        