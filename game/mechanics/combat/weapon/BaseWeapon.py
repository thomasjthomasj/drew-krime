import pygame
from game.mechanics.combat.weapon.bullet.BaseBullet import BaseBullet
from game.Game import Game

class BaseWeapon(object):
    
    speed = 1
    rate = 0
    pos = (0, 0)

    def __init__(self, pos):
        self.pos = pos
    
    def fire(self):
        mousePos = pygame.mouse.get_pos()
        bullet = BaseBullet(self.pos)
        bullet.move(mousePos, self.speed)
        Game.addSprite("bullets", bullet)
    
    def ceaseFire(self):
        return