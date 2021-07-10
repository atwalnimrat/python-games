import random
import pygame
from pygame import mixer
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
play = True

# Food
food = [0,0]
new_food = True

# Snake
snake_pos = [[0,225]]
new_piece = [0,0]
for i in range(1,4):
    snake_pos.append([snake_pos[0][0]-(i*cell_size),snake_pos[0][1]])
def snake():
    head = 1
    for j in snake_pos:
        pygame.draw.rect(screen,(0,0,0),(j[0],j[1],cell_size,cell_size))
        if head == 1:
            pygame.draw.rect(screen,(41,44,75),(j[0]+1,j[1]+1,cell_size-2,cell_size-2))
            head = 0
        else:
            pygame.draw.rect(screen,(50,175,25),(j[0]+1,j[1]+1,cell_size-2,cell_size-2))
# For snake movement
def move_snake():
    global snake_pos
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

# Button class
class Button():
    def _init_(self,x,y,image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
    def draw(self):
        screen.blit(self.image,(self.rect.x,self.rect.y))

# Intro
def intro():
    screen.fill((255,200,150))
    intro_run = True
    update_snake = 0
    while intro_run:
        screen.fill((255,200,150))
        snake()
        if snake_pos[0][0] < 235:
            if update_snake > 299:
                update_snake = 0
                move_snake()
            update_snake += 1
        else:
            intro_run = False
        for event in pygame.event.get():    
            # For closing the window
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.display.update()
def game_banner():
    # Button class
    class button():
        def __init__(self,x,y,image):
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.topleft = (x,y)
        def draw(self):
            screen.blit(self.image,(self.rect.x,self.rect.y))
    intro_img = pygame.image.load('snake\\intro.png')
    button_img = pygame.image.load('snake\\intro-btn.png')
    play_button = button(170,290,button_img)
    screen.blit(intro_img,(155,50))
    play_button.draw()
    pygame.display.update()
    intro_sound = mixer.Sound('snake\\intro-bgd.wav')
    intro_sound.play()
    show = True
    clicked = False
    while show:
        for event in pygame.event.get():
             # For closing the window
            if event.type == pygame.QUIT:
                pygame.quit()
            # Button related
            if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                clicked = True
            elif event.type == pygame.MOUSEBUTTONUP and clicked == True:
                clicked = False
                pos = pygame.mouse.get_pos()
                if play_button.rect.collidepoint(pos):
                    show = False

intro()
game_banner()
snake_pos[0] = [130,225]

# Score
score = 0
font = pygame.font.Font('freesansbold.ttf',24)
text_x,text_y = 310,30
def show_score(x,y):
    score_txt = font.render(f'Score: {score}',True,(0,0,0))
    screen.blit(score_txt,(x,y))

# Game Over
game_over = False
go_font = pygame.font.Font('freesansbold.ttf',32)
pa_font = pygame.font.Font('freesansbold.ttf',20)
def game_over_text():
    go = go_font.render('GAME OVER',True,(41,44,75))
    pa = pa_font.render('Press p to play again',True,(0,0,0))
    screen.blit(go,(125,190))
    screen.blit(pa,(125,240))
def check_game_over(game_over):
    global snake_pos
    for segment in snake_pos[1:]:
        if snake_pos[0] == segment:
            game_over = True
    if snake_pos[0][0] < 5 or snake_pos[0][0] > 435 or snake_pos[0][1] < 5 or snake_pos[0][1] > 435:
        game_over = True
    return game_over

# Game loop
running = True
while running:

    # Setting background color
    screen.fill((255,200,150))

    for event in pygame.event.get():
        
        # For closing the window
        if event.type == pygame.QUIT:
            running = False

        # For moving the snake
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                snake_pos[0] = [130,225]
                snake_pos = snake_pos[:4]
                score = 0
                play = True
                game_over = False
            if event.key == pygame.K_UP and direction != 3:
                direction = 1
            if event.key == pygame.K_DOWN and direction != 1:
                direction = 3
            if event.key == pygame.K_LEFT and direction != 2:
                direction = 4
            if event.key == pygame.K_RIGHT and direction != 4:
                direction = 2
    
    # For creating food
    if new_food == True:
        new_food = False
        no = True
        while no:
            food[0] = (cell_size * random.randint(1,43)) + cell_size/2
            food[1] = (cell_size * random.randint(1,43)) + cell_size
            if food not in snake_pos:
                no = False
        food_sound = mixer.Sound('snake\\food.wav')
        food_sound.play()
    pygame.draw.circle(screen,(255,0,0),(food[0],food[1]),cell_size/2)

    # Checking if food eaten & increasing snake length
    if snake_pos[0] == [int(food[0]-5),food[1]-5]:
        new_food = True
        new_piece = list(snake_pos[-1])
        if direction == 1:
            new_piece[1] += cell_size
        if direction == 3:
            new_piece[1] -= cell_size
        if direction == 4:
            new_piece[0] += cell_size
        if direction == 2:
            new_piece[0] -= cell_size
        snake_pos.append(new_piece)
        score += 1
    
    # For snake movement & game over
    if game_over == False:
        snake()
        if update_snake > 149:
            update_snake = 0
            move_snake()
            game_over = check_game_over(game_over)
    else:
        snake()
        if play:
            go_sound = mixer.Sound('snake\\game-over.wav')
            go_sound.play()
            play = False
        game_over_text()
            
    #snake()
    show_score(text_x,text_y)
    pygame.display.update()

    update_snake += 1

pygame.quit()