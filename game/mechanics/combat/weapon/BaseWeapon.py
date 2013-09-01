import pygame
from game.mechanics.combat.weapon.bullet import BaseBullet

class BaseWeapon():
    
    bullets = []
    speed = 1
    rate = 0
    pos = (0, 0)

    def __init__(self, pos):
        '''takes parameter of where weapon is located ie player location'''
        self.pos = pos
        
        for (key, bullet) in enumerate(self.bullets):
            bulletExists = bullet.draw()
            if bulletExists == False:
                self.bullets.remove(key)
    
    def fire(self):
        mousePos = pygame.mouse.get_pos()
        bullet = BaseBullet(self.pos)
        bullet.move(mousePos, speed)
        self.bullets.append(bullet)
    
    def ceaseFire(self):
        return