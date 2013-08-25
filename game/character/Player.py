import pygame, math, random

# Import classes
from game.visuals.Sprite import Sprite
from game.Game import Game

class Player(Sprite):
    
    # Controls
    control_left = pygame.K_a
    control_right = pygame.K_d
    control_up = pygame.K_w
    control_down = pygame.K_s
    control_jump = pygame.K_SPACE
    control_sneak = pygame.K_LSHIFT
    
    # Movement
    move_x = 0
    move_y = 0
    
    # Level
    level_gun = 1
    level_melee = 1
    level_talk = 1
    level_ath = 1
    level_sneak = 1
    
    def __init__(self):
        super(Player, self).__init__("sprites/test.png", [300, 200])
        Game.addSprite("player", self)
    
    def draw(self, screen):
        # Temporary true if statement
        if True:
            self.applyPhysics()
            
            # If statements to allow for map movement in the future
            if self.move_x < 0:
                self.pos[0] += self.move_x
            elif self.move_x > 0:
                self.pos[0] += self.move_x
            
        self.pos[1] += self.move_y
        
        screen.blit(self.image, self.pos)
        
    def keyDown(self, key):
        if key == self.control_left:
            self.move_x = self.move_x - 2
        elif key == self.control_right:
            self.move_x = self.move_x + 2
        elif key == self.control_up:
            self.move_y = self.move_y - 2
        elif key == self.control_down:
            self.move_y = self.move_y + 2
    
    def keyUp(self, key):
        if key == self.control_left:
            self.move_x = 0
        elif key == self.control_right:
            self.move_x = 0
        elif key == self.control_up:
            self.move_y = 0
        elif key == self.control_down:
            self.move_y = 0
            
    def applyPhysics(self):
        if self.move_y < Game.gravity:
            self.move_y = self.move_y + Game.gravity_offset
        elif self.move_y > Game.gravity:
            self.move_y = Game.gravity
    
    
    
    
    