import pygame
from game.visuals.Sprite import Sprite
from game.helper.Vector import Vector

class BaseBullet(Sprite):
    
    render = False
    move_x = 0
    move_y = 0
    target = False
    speed = 0
    damage = 1
    bullet_life = 60000
    time_fired = 0
    src_img = 'bullet.png'
    location = False
    
    @property
    def int_pos(self):
        return map(int, self.pos)
    
    @property
    def int_target(self):
        if self.target == False:
            return
        return map(int, self.target)
    
    def __init__(self, pos):
        super(BaseBullet, self).__init__(self.src_img, pos)
        
    def draw(self, screen):
        if self.render:
            self.update()

            self.pos[0] = self.move_x
            self.pos[1] = self.move_y
            screen.blit(self.image, self.pos)
    
    def move(self, target, speed):
        self.time_fired = pygame.time.get_ticks()
        self.target = target
        self.speed = speed
        self.render = True
    
    def update(self):
        
        if self.int_pos == self.int_target:
            self.render = False
            return
        
        if self.location.hitTerrain(self):
            self.render = False
            return
        
        # Stolen from http://stackoverflow.com/questions/16288905/make-a-sprite-move-to-the-mouse-click-position-step-by-step/16294710#16294710
        target_vector = Vector.sub(self.target, self.pos)
            
        if pygame.time.get_ticks() > (self.time_fired + self.bullet_life):
            self.render = False
            return
        
        move_vector = [c * self.speed for c in Vector.normalize(target_vector)]
            
        movement = Vector.add(self.pos, move_vector)

        self.move_x = movement[0]
        self.move_y = movement[1]
        