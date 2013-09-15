import pygame

class Sprite(pygame.sprite.Sprite):
    
    src_path = 'sprites/'
    
    direction = False
    damage = 0
    z_index = 0
    render = True
    width = 0
    height = 0
        
    @property
    def base_pos(self):
        return self.pos[1] + self.src_height
    
    @property
    def left_pos(self):
        return self.pos[0] + self.width
    
    @property
    def centre_pos(self):
        return (self.pos[0] + self.width / 2, self.pos[1] + self.height / 2)

    def __init__(self, src, pos):
        super(Sprite, self).__init__()
        self.src_image = pygame.image.load(self.src_path + src).convert_alpha()
        self.src_width, self.src_height = self.src_image.get_size()
        x_pos = pos[0] - self.src_width / 2
        y_pos = pos[1] - self.src_height / 2
        self.width = self.src_width
        self.height = self.src_height
        self.pos = [x_pos, y_pos]
        self.image = self.src_image
        self.image.set_colorkey((0,0,0))
        self.rect = self.src_image.get_rect()
        
    def flipVert(self):
        self.image = pygame.transform.flip(self.image, 1, 0)
    
    def flipHor(self):
        self.image = pygame.transform.flip(self.image, 0, 1)
    
    