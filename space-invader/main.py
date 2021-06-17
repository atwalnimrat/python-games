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
player_x,player_y = 365,520
player_x_change = 0
def player(x,y):
    screen.blit(player_ship,(x,y))

# Game loop
running = True
while running:

    # Setting background color
    screen.fill((0,0,0))
    
    for event in pygame.event.get():
        
        # For closing the window
        if event.type == pygame.QUIT:
            running = False

    # For moving the player ship
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -0.3
            if event.key == pygame.K_RIGHT:
                player_x_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT,pygame.K_RIGHT):
                player_x_change = 0
    player_x += player_x_change
    player(player_x,player_y)

    pygame.display.update()