import pygame
from pygame import mixer
import random
pygame.init()

# Creating the window
screen = pygame.display.set_mode((800,620))

# Styling the window
pygame.display.set_caption('Space Invaders')
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
enemy_x,enemy_y = [],[]
enemy_x_change,enemy_y_change = [],[]
def enemy(x,y):
    screen.blit(enemy_img,(x,y))

# Bullet
bullet_img = pygame.image.load('space-invader\\bullet.png')
bullet_x,bullet_y = player_x,520
bullet_y_change = -0.5
bullet_state = 'ready'
def fire_bullet(x,y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bullet_img,(x+16,y+10))

#Collision
def iscollision(enemy_x,enemy_y,bullet_x,bullet_y):
    distance = ((enemy_x-bullet_x)**2 + (enemy_y-bullet_y)**2)**0.5
    if distance < 30:
        return True
    else:
        return False

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
        for event in pygame.event.get():    
            # For closing the window
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.display.update()
    return y
def game_banner(x,y):
    intro_img = pygame.image.load('space-invader\\intro.png')
    text_img = pygame.image.load('space-invader\\intro-text.png')
    bgd = mixer.Sound('space-invader\\background.wav')
    screen.blit(intro_img,(x,y))
    screen.blit(text_img,(x+65,y+170))
    bgd.play(-1)
    pygame.display.update()
    show = True
    while show:
        for event in pygame.event.get():
             # For closing the window
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    mode_img = pygame.image.load('space-invader\\mode.png')
                    screen.blit(mode_img,(x,y-50))
                    pygame.display.update()
                elif event.key == pygame.K_e:
                    mode = 'easy'
                    show = False
                elif event.key == pygame.K_h:
                    mode = 'hard'
                    show = False
                elif event.key == pygame.K_c:
                    controls_img = pygame.image.load('space-invader\\controls.png')
                    screen.blit(controls_img,(x-2,y-40))
                    pygame.display.update()
    return mode
def intro2(x,y):
    screen.fill((41,44,75))
    intro_run = True
    while intro_run:
        if y < 520:
            y += 0.1
            player(x,y)
        else:
            intro_run = False
        for event in pygame.event.get():    
            # For closing the window
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.display.update()
    return y

player_y = intro(player_x,player_y)
mode = game_banner(190,220)
player_y = intro2(player_x,player_y)
play = True

# Modes
if mode == 'easy':
    num_of_enemies = 5
    change = 0.4
elif mode == 'hard':
    num_of_enemies = 10
    change = 0.6

for i in range(num_of_enemies):
    enemy_x.append(random.randint(0,735))
    enemy_y.append(random.randint(10,200))
    enemy_x_change.append(change)
    enemy_y_change.append(45)

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)
text_x,text_y = 620,20
def show_score(x,y):
    score = font.render('Score: '+str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))

# Game Over
go_font = pygame.font.Font('freesansbold.ttf',64)
pa_font = pygame.font.Font('freesansbold.ttf',28)
def game_over_text():
    go = go_font.render('GAME OVER',True,(77,208,225))
    pa = pa_font.render('Press p to play again',True,(255,255,255))
    screen.blit(go,(200,250))
    screen.blit(pa,(255,320))

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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                for l in range(num_of_enemies):
                    enemy_y[l] = random.randint(10,200)
                score_value = 0
                play = True
                pygame.display.update()
            elif event.key == pygame.K_LEFT:
                player_x_change = -0.5
            elif event.key == pygame.K_RIGHT:
                player_x_change = 0.5
            elif event.key == pygame.K_SPACE:
                if bullet_state == 'ready':
                    bullet_sound = mixer.Sound('space-invader\\bullet.wav')
                    bullet_sound.play()
                    bullet_x = player_x
                    fire_bullet(bullet_x,bullet_y)
        elif event.type == pygame.KEYUP:
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
    for j in range(num_of_enemies):
        if enemy_y[j] > 460:
            for k in range(num_of_enemies):
                enemy_y[k] = 2000
            if play:
                go_sound = mixer.Sound('space-invader\\game-over.wav')
                go_sound.play()
                play = False
            game_over_text()

        if enemy_x[j] <= 0:
            enemy_x_change[j] = change
            enemy_y[j] += enemy_y_change[j]
        elif enemy_x[j] >= 736:
            enemy_x_change[j] = -change
            enemy_y[j] += enemy_y_change[j]
        enemy_x[j] += enemy_x_change[j]
        enemy(enemy_x[j],enemy_y[j])

        # Collision detection
        collision = iscollision(enemy_x[j],enemy_y[j],bullet_x,bullet_y)
        if collision:
            explosion_sound = mixer.Sound('space-invader\\explosion.wav')
            explosion_sound.play()
            bullet_y = 520
            bullet_state = 'ready'
            score_value += 1
            enemy_x[j],enemy_y[j] = random.randint(0,735),random.randint(10,200)

    player(player_x,player_y)    
    show_score(text_x,text_y)
    
    pygame.display.update()

pygame.quit()