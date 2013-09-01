import pygame
from game.visuals.Sprite import Sprite

class BaseBullet(Sprite):
    
    draw = False
    
    
    def __init__(self, pos):
        super(BaseBullet, self).__init__('bullet.png', pos)
        
    def draw(self):
        if self.draw:
            self.pos[0] += self.move_x
            self.pos[1] += self.move_y
            screen.fill((0,0,0))
            screen.blit(self.image, self.pos)
            return True
        
        return False
    
    def move(self, newPos, speed):
        self.draw = True
        move_x = speed
        move_y = speed
        while self.pos != newPos:
            if newPos[0] > newPos[1]:
                move_y = (newPos[0] / newPos[1]) * speed
            elif newPos[0] < newPos[1]:
                move_x = (newPos[1] / newPos[0]) * speed
            
            self.move_x[0] += move_x
            self.move_y[1] += move_y
            
        self.draw = False
        