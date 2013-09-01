import pygame, math, random

#from combat.weapon.BaseWeapon import BaseWeapon

class Leveller:
    '''Class to handle calculations for levelling up player'''
    
    @staticmethod
    def levelUpJump(player):
        if player.level_jump < player.level_jump_cap:
            if player.jump_level_up >= player.jump_level_up_cap:
                player.level_jump += 1
                player.jump_level_up = 0
            else:
                player.jump_level_up += 1