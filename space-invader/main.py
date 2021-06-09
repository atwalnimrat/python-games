import pygame
pygame.init()

# Creating the screen
screen = pygame.display.set_mode((800,600))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        # For closing the window
        if event.type == pygame.QUIT:
            running = False