import pygame, math, random

# Import classes
from game.character.Character import Character
from game.Game import Game
from game.mechanics.Leveller import Leveller
from game.mechanics.combat.weapon.BaseWeapon import BaseWeapon
from game.mechanics.combat.weapon.Pistol import Pistol
from game.location.BaseLocation import BaseLocation

class Player(Character):
    
    # Controls
    control_left = pygame.K_a
    control_right = pygame.K_d
    control_up = pygame.K_w
    control_down = pygame.K_s
    control_jump = pygame.K_SPACE
    control_sneak = pygame.K_LSHIFT
    control_reload = pygame.K_r
    control_fire = 1
    control_melee = 3
    
    # Combat
    weapon = False
    
    # Level
    level_gun = 1
    level_melee = 1
    level_talk = 1
    level_ath = 1
    
    level_sneak = 1
    sneak_level_up = 0
    
    level_jump = 2
    level_jump_cap = 2
    jump_level_up = 0
    jump_level_up_cap = 5
    
    health = 5
    
    # Misc
    platform = False
    
    def __init__(self):
        super(Player, self).__init__("player.png", [300, 200])
        self.weapon = Pistol(self)
        self.location = BaseLocation(self)
        dimensions = Game.getDefaultDimensions()
        Game.addSprite("player", self)
    
    def setDirection(self):
        mouse_pos = pygame.mouse.get_pos()
        if mouse_pos[0] < self.centre_pos[0] and self.direction == 'right':
            self.flipVert()
            self.direction = 'left'
        elif mouse_pos[0] > self.centre_pos[0] and self.direction == 'left':
            self.flipVert()
            self.direction = 'right'
    
    def draw(self, screen):
        if self.render:
            self.applyPhysics()
            self.setDirection()
            self.checkHealth()
            
            if self.dead == True:
                self.dead = False
                self.pos = [300, 200]
            
            if self.sneak:
                self.moveSneak()
            else:
                self.moveX()
            
            self.pos[1] += self.move_y
            screen.blit(self.image, self.pos)
        
    def keyDown(self, key):
        if key == self.control_sneak:
            self.sneak = True
        if key == self.control_left:
            self.moveLeft(self.walk_speed)
        elif key == self.control_right:
            self.moveRight(self.walk_speed)
        elif key == self.control_jump and self.pos[1]>= 300:
            self.jump()
        elif key == self.control_reload:
            if isinstance(self.weapon, BaseWeapon):
                self.weapon.reload_ammo()
    
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
    
    def moveSneak(self):
        dimensions = Game.getDimensions()
        if self.move_x < 0 and self.pos[0] > 0:
            self.pos[0] -= self.sneak_speed
        elif self.move_x > 0 and self.pos[0] < (dimensions[0] - self.src_width):
            self.pos[0] += self.sneak_speed
    
    def moveX(self):
        dimensions = Game.getDimensions()
        if self.pos[0] >= 0 and self.move_x < 0:
            self.pos[0] += self.move_x
        elif self.pos[0] <= (dimensions[0] - self.src_width) and self.move_x > 0:
            self.pos[0] += self.move_x
