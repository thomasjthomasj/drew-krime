import pygame
from game.visuals.Sprite import Sprite
from game.Game import Game

class Crosshair(Sprite):
    
    def __init__(self):
        super(Crosshair, self).__init__("crosshair.png", pygame.mouse.get_pos())
        Game.addSprite("player", self)
        
    def draw(self, screen):
        screen.fill((0,0,0))
        screen.blit(self.image, self.pos)