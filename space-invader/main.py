import pygame
import random
pygame.init()

# Creating the window
screen = pygame.display.set_mode((800,620))

# Styling the window
pygame.display.set_caption('Space Invader')
icon = pygame.image.load('space-invader\\ship.png')
pygame.display.set_icon(icon)

# Player ship
player_ship = pygame.image.load('space-invader\\player.png')
player_x,player_y = 370,600
player_x_change = 0
def player(x,y):
    screen.blit(player_ship,(x,y))

# Enemy
enemy_img = pygame.image.load('space-invader\\enemy.png')
enemy_x,enemy_y = random.randint(0,800),random.randint(10,200)
enemy_x_change,enemy_y_change = 0.2,40
def enemy(x,y):
    screen.blit(enemy_img,(x,y))

# Bullet
bullet_img = pygame.image.load('space-invader\\bullet.png')
bullet_y = 520
bullet_y_change = -0.5
bullet_state = 'ready'
def fire_bullet(x,y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bullet_img,(x+16,y+10))

# Intro
def intro(x,y):
    screen.fill((41,44,75))
    intro_run = True
    while intro_run:
        if y > 100:
            y -= 0.2
            player(x,y)
        else:
            intro_run = False
        pygame.display.update()
    return y
def game_banner(x,y):
    intro_img = pygame.image.load('space-invader\\intro.png')
    text_img = pygame.image.load('space-invader\\intro-text.png')
    screen.blit(intro_img,(x,y))
    screen.blit(text_img,(x+65,y+170))
    pygame.display.update()
    show = True
    while show:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    mode_img = pygame.image.load('space-invader\\mode.png')
                    screen.blit(mode_img,(x,y-30))
                    pygame.display.update()
                elif event.key == pygame.K_e:
                    mode = 'easy'
                    show = False
                elif event.key == pygame.K_m:
                    mode = 'medium'
                    show = False
                elif event.key == pygame.K_h:
                    mode = 'hard'
                    show = False
                elif event.key == pygame.K_c:
                    controls_img = pygame.image.load('space-invader\\controls.png')
                    screen.blit(controls_img,(x-2,y-40))
                    pygame.display.update()
    return
def intro2(x,y):
    screen.fill((41,44,75))
    intro_run = True
    while intro_run:
        if y < 520:
            y += 0.1
            player(x,y)
        else:
            intro_run = False
        pygame.display.update()
    return y

mode = ''
player_y = intro(player_x,player_y)
game_banner(190,220)
player_y = intro2(player_x,player_y)

# Modes
if mode == 'easy':
    enemy_x_change = 0.2
elif mode == 'medium':
    #enemy_no % 2 != 0  ---> enemy_x_change = 0.2
    #enemy_no % 2 == 0  ---> enemy_x_change = -0.2
    enemy_x_change = 0.2
elif mode == 'hard':
    # random movement for each enemy
    enemy_x_change = 0.2

# Game loop
running = True
while running:

    # Setting background color
    screen.fill((41,44,75))
    
    for event in pygame.event.get():
                
        # For closing the window
        if event.type == pygame.QUIT:
            running = False

    # For moving the player ship & firing bullets
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -0.3
            if event.key == pygame.K_RIGHT:
                player_x_change = 0.3
            if event.key == pygame.K_SPACE:
                if bullet_state is 'ready':
                    bullet_x = player_x
                    fire_bullet(bullet_x,bullet_y)
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT,pygame.K_RIGHT):
                player_x_change = 0
    player_x += player_x_change

    # Creating boundaries
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736
    
    # For firing multiple bullets
    if bullet_y <= 0:
        bullet_y = 520
        bullet_state = 'ready'
    if bullet_state == 'fire':
        bullet_y += bullet_y_change
        fire_bullet(bullet_x,bullet_y)

    # For enemy movement
    if enemy_x <= 0:
        enemy_x_change = 0.2
        enemy_y += enemy_y_change
    elif enemy_x >= 736:
        enemy_x_change = -0.2
        enemy_y += enemy_y_change
    enemy_x += enemy_x_change

    player(player_x,player_y)
    enemy(enemy_x,enemy_y)
    
    pygame.display.update()