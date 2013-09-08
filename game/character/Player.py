import pygame, math, random

# Import classes
from game.character.Character import Character
from game.Game import Game
from game.mechanics.Leveller import Leveller
from game.mechanics.combat.weapon.Pistol import Pistol
from game.location.Level import Level

class Player(Character):
    
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
    direction = 'right'
    z_index = 5
    
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
    location = False
    
    # Misc
    ground_level = 700
    
    def __init__(self):
        super(Player, self).__init__("player.png", [300, 200])
        self.weapon = Pistol(self)
        self.location = Level(self)
        dimensions = Game.getDefaultDimensions()
        self.ground_level = dimensions[1] - 100
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
            
            if self.sneak:
                self.moveSneak()
            else:
                self.moveHor()
            
            
        self.pos[1] += self.move_y
        screen.blit(self.image, self.pos)
        
    def keyDown(self, key):
        if key == self.control_sneak:
            self.sneak = True
        
        if key == self.control_left:
            
            self.moveLeft(self.walk_speed)
        elif key == self.control_right:
            if self.direction == 'left':
                self.image = pygame.transform.flip(self.image, 1, 0)
            self.direction = 'right'
            self.moveRight(self.walk_speed)
        elif key == self.control_jump and self.pos[1]>= 300:
            self.jump()
    
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
        dimensions = Game.getDefaultDimensions()
        if self.move_x < 0 and self.pos[0] > 0:
            self.pos[0] -= self.sneak_speed
        elif self.move_x > 0 and self.pos[0] < (dimensions[0] - self.src_width):
            self.pos[0] += self.sneak_speed
    
    def moveHor(self):
        dimensions = Game.getDefaultDimensions()
        if self.pos[0] >= 0 and self.move_x < 0:
            self.pos[0] += self.move_x
        elif self.pos[0] <= (dimensions[0] - self.src_width) and self.move_x > 0:
            self.pos[0] += self.move_x
        
    def jump(self):
        self.vel_y = 0 - self.level_jump
        Leveller.levelUpJump(self)
            
    def applyPhysics(self):
        self.move_y = self.move_y + self.vel_y
        self.vel_y += Game.gravity
        if self.pos[1] > self.ground_level and self.vel_y > 0:
            self.vel_y = 0
            self.move_y = 0
            self.pos[1] = self.ground_level
