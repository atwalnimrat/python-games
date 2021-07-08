import random
import pygame
from pygame.locals import *
pygame.init()

# Creating the window
screen = pygame.display.set_mode((450,450))

# Styling the window
pygame.display.set_caption('Snake')
icon = pygame.image.load('snake\\snake.png')
pygame.display.set_icon(icon)

# Game variables
cell_size = 10
direction = 2        # 1 is up, 2 is right, 3 is down and 4 is left
update_snake = 0

# Snake
snake_pos = [[0,225]] #235
for i in range(1,4):
    snake_pos.append([snake_pos[0][0]-(i*cell_size),snake_pos[0][1]])

# Game loop
running = True
while running:

    # Setting background color
    screen.fill((255,200,150))

    for event in pygame.event.get():
        
        # For closing the window
        if event.type == pygame.QUIT:
            running = False

        # For snake movement 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 3:
                direction = 1
            if event.key == pygame.K_DOWN and direction != 1:
                direction = 3
            if event.key == pygame.K_LEFT and direction != 2:
                direction = 4
            if event.key == pygame.K_RIGHT and direction != 4:
                direction = 2
    if update_snake > 129: #499
        update_snake = 0
        snake_pos = snake_pos[-1:] + snake_pos[:-1]
        if direction == 1:
            snake_pos[0][0] = snake_pos[1][0]
            snake_pos[0][1] = snake_pos[1][1] - cell_size
        if direction == 3:
            snake_pos[0][0] = snake_pos[1][0]
            snake_pos[0][1] = snake_pos[1][1] + cell_size
        if direction == 4:
            snake_pos[0][0] = snake_pos[1][0] - cell_size
            snake_pos[0][1] = snake_pos[1][1]
        if direction == 2:
            snake_pos[0][0] = snake_pos[1][0] + cell_size
            snake_pos[0][1] = snake_pos[1][1]

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

    update_snake += 1

pygame.quit()