import pygame

from game.mechanics.combat.weapon.BaseWeapon import BaseWeapon

class Pistol(BaseWeapon):
    
    def __init__(self, pos):
        super(Pistol, self).__init__(pos)