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
        
    def fire(self):
        # Check ammo count,reload if out
        if self.ammo <= 0 and self.reloading == False:
            self.reload_ammo()
        elif self.reloading == True:
            if pygame.time.get_ticks() > (self.reloaded_at + self.reload_time):
                self.ammo = self.max_ammo
                self.reloading = False
        if self.reloading == False:
            super(Pistol, self).fire()
            self.ammo = self.ammo - 1
    
        