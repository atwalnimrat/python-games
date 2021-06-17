import pygame
pygame.init()

# Creating the window
screen = pygame.display.set_mode((800,600))

# Styling the window
pygame.display.set_caption('Space Invader')
icon = pygame.image.load('space-invader\\ship.png')
pygame.display.set_icon(icon)

# Player ship
player_ship = pygame.image.load('space-invader\\player.png')
player_x,player_y = 365,500
def player():
    screen.blit(player_ship,(player_x,player_y))

# Game loop
running = True
while running:

    # Setting background color
    screen.fill((0,0,0))
    
    # For closing the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player()

    pygame.display.update()