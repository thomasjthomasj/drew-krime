import pygame

class Game:
    
    sprites = {}
    
    fps = 60
    frame = 1
    
    gravity = .2
    gravity_offset = 0.02
    
    def __init__(self):
        pass
    
    @staticmethod
    def addSpriteGroup(name):
        Game.sprites[name] = pygame.sprite.Group()
    
    @staticmethod
    def addSprite(group, sprite):
        Game.sprites[group].add(sprite)
    
    @staticmethod
    def render(screen, frame_ticks, ticks):
        
        Game.frame += 1
        if Game.frame > Game.fps:
            Game.frame = 1
            
        for group in Game.sprites:
            for sprite in Game.sprites[group].sprites():
                sprite.draw(screen)