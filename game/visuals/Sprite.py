import pygame

class Sprite(pygame.sprite.Sprite):
    
    def __init__(self, src):
        pygame.sprite.Sprite.__init__(self)
        self.src_image = pygame.image.load(src).convert_alpha()
        self.src_width, self.src_height = self.src_image.get_size()
        