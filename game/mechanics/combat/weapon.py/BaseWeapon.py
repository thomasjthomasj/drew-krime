import pygame
from game.visuals.Sprite import Sprite

class BaseWeapon(Sprite):

    def __init__(self):
        super(BaseWeapon, self).__init__("test.png", [300, 200])