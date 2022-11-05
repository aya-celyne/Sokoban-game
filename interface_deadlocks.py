import node
import search
import sokoPuzzle
import pygame
import pygame_gui
from pygame import *
import random
import deadlock_matrix
# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
pygame.init()

board = deadlock_matrix.board9
# Set up the drawing window
screen = pygame.display.set_mode([300, 300])
obstacle = pygame.image.load("images/wall.png")
terre = pygame.image.load("images/floor.png")
box = pygame.image.load("images/box.png")
box_docked = pygame.image.load("images/box_docked.png")
robot = pygame.image.load("images/worker.png")
worker_docked = pygame.image.load("images/X.png")
docker = pygame.image.load("images/dock.png")

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255,226,191))

    x = 0
    y = 0

    for row in board:
        for char in row:
            if char == ' ': #floor
               screen.blit(terre,(x,y))
            elif char == 'O': #wall
                screen.blit(obstacle,(x,y))
            elif char == 'R': #worker on floor
                screen.blit(robot,(x,y))
            elif char == 'S': #dock
                screen.blit(docker,(x,y))
            elif char == '*': #box on dock
                screen.blit(box_docked,(x,y))
            elif char == 'B': #box
                screen.blit(box,(x,y))
            elif char == 'D': #deadlock
                screen.blit(worker_docked,(x,y))
            x = x + 32
        x = 0
        y = y + 32
    


    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
