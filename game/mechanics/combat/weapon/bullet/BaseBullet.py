import pygame
from game.visuals.Sprite import Sprite
from game.helper.Vector import Vector

class BaseBullet(Sprite):
    
    render = False
    original_pos = (0, 0)
    move_x = 0
    move_y = 0
    
    def __init__(self, pos):
        super(BaseBullet, self).__init__('bullet.png', pos)
        self.original_pos = pos
        
    def draw(self, screen):
        if self.render:
            self.pos[0] += self.move_x
            self.pos[1] += self.move_y
            screen.blit(self.image, self.pos)
    
    def move(self, new_pos, speed):
        self.render = True
        move_x = speed
        move_y = speed
        diff_x = float(new_pos[0] - self.pos[1])
        diff_y = float(new_pos[1] - self.pos[1])
        
        if self.pos != new_pos:
            # Stolen from http://stackoverflow.com/questions/16288905/make-a-sprite-move-to-the-mouse-click-position-step-by-step/16294710#16294710
            target_vector = Vector.sub(new_pos, self.pos)
            if Vector.magnitude(target_vector) < 2:
                return
            move_vector = [c * speed for c in Vector.normalize(target_vector)]
            
            move_x, move_y = Vector.add(self.pos, move_vector)
        else:
            self.render = False
        