import pygame

class Sprite(pygame.sprite.Sprite):
    
    def __init__(self, src, pos):
        super(Sprite, self).__init__()
        self.src_image = pygame.image.load(src).convert_alpha()
        self.src_width, self.src_height = self.src_image.get_size()
        x_pos = pos[0] - self.src_width / 2
        y_pos = pos[1] - self.src_height / 2
        self.pos = [x_pos, y_pos]
        self.image = self.src_image
        self.rect = self.src_image.get_rect()