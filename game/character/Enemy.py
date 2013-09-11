import pygame
from game.Game import Game
from game.character.Character import Character

class Enemy(Character):
    
    def __init__(self, src, location, pos):
        super(Enemy, self).__init__(src, pos)
        self.location = location
        self.location.enemies.append(self)
        Game.addSprite('enemies', self)