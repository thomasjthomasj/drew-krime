# Drew Krime: Streets of Ellay

project_title = "Drew Krime: Streets of Ellay"

# Import dependencies
import os, sys
import pygame

# Check if Windows and import pygame._view if so
from sys import platform as _platform
#if _platform == "win32" or _platform == "cygwin":
#    import pygame._view

# Initialise pygame library
pygame.init()

# Import game files
from game.Game import Game
from game.character.Player import Player
from game.mechanics.Crosshair import Crosshair
from game.world.Background import Background

# Setup screen
size = Game.getDefaultDimensions()
screen = pygame.display.set_mode(size)
pygame.display.set_caption(project_title)

screen.convert()

# Run game
Game.addSpriteGroup("world")
Game.addSpriteGroup("player")
Game.addSpriteGroup("bullets")
Game.addSpriteGroup("enemies")

background = Background()
player = Player()
crosshair = Crosshair()

pygame.mouse.set_visible(False)

clock = pygame.time.Clock()

# Program loop
inLoop = True
while inLoop:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            inLoop = False
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                inLoop = False
            else:
                player.keyDown(event.key)
            
        elif event.type == pygame.KEYUP:
            player.keyUp(event.key)
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            player.mouseDown(event.button)
        
        elif event.type == pygame.MOUSEBUTTONUP:
            player.mouseUp(event.button)
        
        elif event.type == pygame.MOUSEMOTION:
            pass
    
    Game.render(screen, int(clock.get_time()), int(pygame.time.get_ticks()))
    
    clock.tick(Game.fps)
    
    pygame.display.flip()

pygame.quit()
sys.exit()