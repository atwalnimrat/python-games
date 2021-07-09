import random
import pygame
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

# Food
food = [0,0]
new_food = True

# Snake
snake_pos = [[0,225]] #235
new_piece = [0,0]
for i in range(1,4):
    snake_pos.append([snake_pos[0][0]-(i*cell_size),snake_pos[0][1]])
def snake():
    global snake_pos
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


# Score
score = 0
font = pygame.font.Font('freesansbold.ttf',24)
text_x,text_y = 310,30
def show_score(x,y):
    score_txt = font.render(f'Score: {score}',True,(0,0,0))
    screen.blit(score_txt,(x,y))

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
        food[0] = (cell_size * random.randint(0,44)) + cell_size/2
        food[1] = (cell_size * random.randint(0,43)) + cell_size
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
    
    # For snake movement
    if update_snake > 149: #499
        update_snake = 0
        move_snake()
        
    snake()
    show_score(text_x,text_y)
    pygame.display.update()

    update_snake += 1

pygame.quit()