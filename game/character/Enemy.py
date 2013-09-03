import pygame
from game.character.Character import Character

class Enemy(Character):
    
    def __init__(self, src, pos):
        super(Enemy, self).__init__(src, pos)