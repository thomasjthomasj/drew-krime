import pygame
from game.mechanics.combat.weapon.bullet.BaseBullet import BaseBullet
from game.Game import Game

class BaseWeapon(object):
    
    speed = 1
    rate = 0
    pos = (0, 0)
    carrier = False

    def __init__(self, carrier):
        '''takes Sprite instance as parameter'''
        self.carrier = carrier
        self.setPos()
    
    def fire(self):
        self.setPos()
        mousePos = pygame.mouse.get_pos()
        bullet = BaseBullet(self.pos)
        bullet.move(mousePos, self.speed)
        Game.addSprite("bullets", bullet)
    
    def ceaseFire(self):
        return
    
    def setPos(self):
        pos_x = self.carrier.pos[0] + (self.carrier.src_width / 2)
        pos_y = self.carrier.pos[1] + (self.carrier.src_height / 2)
        
        if self.carrier.direction == 'left':
            pos_x = self.carrier.pos[0]
        elif self.carrier.direction == 'right':
            pos_x = self.carrier.pos[0] + self.carrier.src_width
        
        self.pos = (pos_x, pos_y)