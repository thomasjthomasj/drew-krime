import pygame
from game.visuals.Sprite import Sprite

class BaseBullet(Sprite):
    
    visible = False
    
    def __init__(self, pos):
        super(BaseBullet, self).__init__('bullet.png', pos)
    
    def move(self, newPos, speed):
        self.visible = True
        x_move = speed
        y_move = speed
        while self.pos != newPos:
            if newPos[0] > newPos[1]:
                y_move = (newPos[0] / newPos[1]) * speed
            elif newPos[0] < newPos[1]:
                x_move = (newPos[1] / newPos[0]) * speed
            
            self.pos[0] += x_move
            self.pos[1] += y_move
            
        self.visible = False
        