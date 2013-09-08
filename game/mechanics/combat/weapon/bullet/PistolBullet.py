import pygame
from game.mechanics.combat.weapon.bullet.BaseBullet import BaseBullet

class PistolBullet(BaseBullet):
    
    bullet_life = 150
    src_img = 'pistolbullet.png'
    
    def __init__(self, pos):
        super(PistolBullet, self).__init__(pos)