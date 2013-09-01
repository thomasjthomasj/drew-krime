import pygame, math, random

# Import classes
from game.visuals.Sprite import Sprite
from game.Game import Game
from game.mechanics.Leveller import Leveller
from game.mechanics.combat.weapon.BaseWeapon import BaseWeapon


class Player(Sprite):
    
    # Controls
    control_left = pygame.K_a
    control_right = pygame.K_d
    control_up = pygame.K_w
    control_down = pygame.K_s
    control_jump = pygame.K_SPACE
    control_sneak = pygame.K_LSHIFT
    control_fire = 1
    control_melee = 3
    
    # Movement
    move_x = 0
    move_y = 0
    vel_y = 0
    walk_speed = 4
    sneak_speed = 2
    sneak = False
    
    # Combat
    weapon = False
    
    # Level
    level_gun = 1
    level_melee = 1
    level_talk = 1
    level_ath = 1
    
    level_sneak = 1
    sneak_level_up = 0
    
    level_jump = 1
    level_jump_cap = 2
    jump_level_up = 0
    jump_level_up_cap = 5
    
    # Misc
    draw = True
    
    def __init__(self):
        super(Player, self).__init__("test.png", [300, 200])
        self.weapon = BaseWeapon(self.pos)
        Game.addSprite("player", self)
    
    def draw(self, screen):
        # Temporary true if statement
        if self.draw:
            self.applyPhysics()
            
            if self.sneak:
                if self.move_x < 0:
                    self.pos[0] -= self.sneak_speed
                elif self.move_x > 0:
                    self.pos[0] += self.sneak_speed
            else:
                # If statements to allow for map movement in the future
                if self.move_x < 0:
                    self.pos[0] += self.move_x
                elif self.move_x > 0:
                    self.pos[0] += self.move_x
            
        self.pos[1] += self.move_y
        screen.fill((0,0,0))
        screen.blit(self.image, self.pos)
        
    def keyDown(self, key):
        if key == self.control_sneak:
            self.sneak = True
        
        if key == self.control_left:
            self.moveLeft(self.walk_speed)
        elif key == self.control_right:
            self.moveRight(self.walk_speed)
        elif key == self.control_jump and self.pos[1]>= 300:
            jump_height = self.level_jump / 5
            self.vel_y = 0 - self.level_jump
            Leveller.levelUpJump(self)
    
    def keyUp(self, key):
        if key == self.control_left:
            self.move_x = 0
        elif key == self.control_right:
            self.move_x = 0
        elif key == self.control_sneak:
            self.sneak = False
    
    def mouseDown(self, button):
        if button == self.control_fire:
            self.weapon.fire()

    def mouseUp(self, button):
        if button == self.control_fire:
            self.weapon.ceaseFire()
            
    def moveLeft(self, speed):
        self.move_x = self.move_x - speed
    
    def moveRight(self, speed):
        self.move_x = self.move_x + speed
            
    def applyPhysics(self):
        self.move_y = self.move_y + self.vel_y
        self.vel_y += Game.gravity
        if self.pos[1] > 300 and self.vel_y > 0:
            self.vel_y = 0
            self.move_y = 0
            self.pos[1] = 300
