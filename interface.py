import node
import search
import sokoPuzzle
import pygame
import pygame_gui
from pygame import *
import random

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
pygame.init()


# Set up the drawing window
screen = pygame.display.set_mode([300, 300])
obstacle = pygame.image.load("C:/Users/21354/Desktop/TPs MIV/RP/SOKOPUZZLE/sokoban-working/images/wall.png")
terre = pygame.image.load("C:/Users/21354/Desktop/TPs MIV/RP/SOKOPUZZLE/sokoban-working/images/floor.png")
box = pygame.image.load("C:/Users/21354/Desktop/TPs MIV/RP/SOKOPUZZLE/sokoban-working/images/box.png")
box_docked = pygame.image.load("C:/Users/21354/Desktop/TPs MIV/RP/SOKOPUZZLE/sokoban-working/images/box_docked.png")
robot = pygame.image.load("C:/Users/21354/Desktop/TPs MIV/RP/SOKOPUZZLE/sokoban-working/images/worker.png")
worker_docked = pygame.image.load("C:/Users/21354/Desktop/TPs MIV/RP/SOKOPUZZLE/sokoban-working/images/X.png")
docker = pygame.image.load("C:/Users/21354/Desktop/TPs MIV/RP/SOKOPUZZLE/sokoban-working/images/dock.png")

# Run until the user asks to quit
running = True
while running:

    # button close to close the game window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # la couleur du background
    screen.fill((255,226,191))

    x = 0
    y = 0

    for row in search.board8:
        for char in row:
            if char == ' ': 
               screen.blit(terre,(x,y))
            elif char == 'O': 
                screen.blit(obstacle,(x,y))
            elif char == 'R': 
                screen.blit(robot,(x,y))
            elif char == 'S': 
                screen.blit(docker,(x,y))
            elif char == '*': 
                screen.blit(box_docked,(x,y))
            elif char == 'B': 
                screen.blit(box,(x,y))
            elif char == 'D': 
                screen.blit(worker_docked,(x,y))
            x = x + 32
        x = 0
        y = y + 32
    


    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()