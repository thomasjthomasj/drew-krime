import pygame
from game.visuals.Sprite import Sprite
from game.Game import Game

class Background(Sprite):
    
    player = False
    
    def __init__(self):
        dimensions = Game.getDefaultDimensions()
        pos = (dimensions[0] / 2, dimensions[1] / 2)
        super(Background, self).__init__("background.png", pos)
        Game.addSprite("world", self)
    
    def draw(self, screen):
        screen.fill((0,0,0))
        screen.blit(self.image, self.pos)
    
    def addPlayer(self, player):
        self.player = player