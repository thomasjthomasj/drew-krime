import pygame
from game.mechanics.combat.weapon.bullet import BaseBullet

class BaseWeapon():
    
    bullet = False

    def __init__(self, pos):
        '''takes parameter of where weapon is located ie player location'''
        bullet = BaseBullet(pos)