import pygame

from game.mechanics.combat.weapon.BaseWeapon import BaseWeapon
from game.mechanics.combat.weapon.bullet.PistolBullet import PistolBullet

class Pistol(BaseWeapon):
    
    speed = 30
    ammo = 6
    max_ammo = 6
    reload_time = 500
    
    @property
    def bullet(self):
        return PistolBullet(self.pos)
    
    def __init__(self, carrier):
        super(Pistol, self).__init__(carrier)
    
        