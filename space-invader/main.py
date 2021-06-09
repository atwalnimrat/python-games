import pygame
pygame.init()

# Creating the window
screen = pygame.display.set_mode((800,600))

# Styling the window
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('space-invader\\ship.png')
pygame.display.set_icon(icon)

# Game loop
running = True
while running:
    for event in pygame.event.get():
    
        # For closing the window
        if event.type == pygame.QUIT:
            running = False
    
    # Setting background color
    screen.fill((0,0,50))

    pygame.display.update()