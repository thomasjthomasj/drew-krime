import pygame
from game.character.Enemy import Enemy
from game.mechanics.combat.weapon.Pistol import Pistol

class TestEnemy(Enemy):
    
    health = 5
    shot_fired = 0
    rate_of_fire = 1000
    level_jump = 2
    level_jump_cap = 2
    
    def __init__(self, location, pos):
        super(TestEnemy, self).__init__('monster.png', location, pos)
        self.weapon = Pistol(self)
        
    def draw(self, screen):
        self.applyPhysics()
        self.attack()
        screen.blit(self.image, self.pos)
        
    def attack(self):
        if self.shot_fired < pygame.time.get_ticks() - self.rate_of_fire:
            self.fire()
    
    def fire(self):
        self.shot_fired = pygame.time.get_ticks()
        self.weapon.fire(self.location.player.centre_pos)