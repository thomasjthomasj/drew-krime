import pygame, math, random
from game.visuals.Sprite import Sprite

class Player(Sprite):
    control_left = pygame.K_a
    control_right = pygame.K_d
    control_up = pygame.K_w
    control_down = pygame.K_s
    
    def __init__(self):
        return 'test'