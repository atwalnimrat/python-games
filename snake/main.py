import random
import pygame
from pygame.locals import *
pygame.init()

# Creating the window
screen = pygame.display.set_mode((500,500))

# Styling the window
pygame.display.set_caption('Snake')
icon = pygame.image.load('snake\\snake.png')
pygame.display.set_icon(icon)

# Game variables
cell_size = 10

# Snake
snake_pos = [[250,250]]
for i in range(1,4):
    snake_pos.append([250-(i*cell_size),250])

# Game loop
running = True
while running:

    # Setting background color
    screen.fill((255,200,150))

    # For closing the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Snake
    head = 1
    for j in snake_pos:
        pygame.draw.rect(screen,(0,0,0),(j[0],j[1],cell_size,cell_size))
        if head == 1:
            pygame.draw.rect(screen,(41,44,75),(j[0]+1,j[1]+1,cell_size-2,cell_size-2))
            head = 0
        else:
            pygame.draw.rect(screen,(50,175,25),(j[0]+1,j[1]+1,cell_size-2,cell_size-2))

    pygame.display.update()

pygame.quit()