import pygame
import sys
import random

pygame.init()
#Player 1:
x_position1 = 25
y_position1 = 400
player1_rect_width = 25
player1_rect_height = 100

#Player 2:
x_position2 = 750
y_position2 = 400
player2_rect_width = 25
player2_rect_height = 100

#Other code
middleline_pos_x = 400
middleline_pos_y = 0
endmiddleline_pos_y = 800
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
yellow = (255,255,0)
green = (0,128,0)
color_list = [green, blue, yellow]
color_list1 = [blue, yellow, green]
random_color = random.choice(color_list)
random_color1 = random.choice(color_list1)
WIDTH = 800
HEIGHT = 800
font = pygame.font.SysFont("Arial", 36)
fontend = pygame.font.SysFont("Arial", 58)
text_color = (white)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")
basket_velocity = 10
clock = pygame.time.Clock()

#score system 
score = 0
score1 = 0

#Ball properties:
ball_x = 375
ball_y = random.randint(0,HEIGHT)
radius = 10
gravity = random.randint(1,10)

#Second Ball Properties:
ball_x_1  = 425
ball_y_1 = random.randint(0,HEIGHT)
radius_1 = 10
gravity_1 = random.randint(1,10)
        
running = True
#Function to check who have won the game 
def check_winner(score, score1, player1_score, player2_score):
    if score >= 10:
        screen.fill(black)
        screen.blit(player1_score,(300,400))
        

    elif score1 >= 10:
        screen.fill(black)
        screen.blit(player2_score,(300,400))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pressed_key = pygame.key.get_pressed()
    if pressed_key[pygame.K_w] and y_position1 >= 0:
        y_position1 -= basket_velocity

    if pressed_key[pygame.K_s] and y_position1 + player1_rect_height <= HEIGHT:
        y_position1 += basket_velocity

    if pressed_key[pygame.K_UP] and y_position2 >= 0:
        y_position2 -= basket_velocity

    if pressed_key[pygame.K_DOWN] and y_position2 + player2_rect_height <= HEIGHT:
        y_position2 += basket_velocity 

    #Player 1: basket 
    if (ball_x <= x_position1 + player1_rect_width) and (ball_y >= y_position1 and ball_y <= y_position1 + player1_rect_height):
        ball_x = 375
        random_color = random.choice(color_list)
        ball_y = random.randint(0,HEIGHT)
        score += 1
        gravity = random.randint(1,10)

    elif ball_x >= 0:
        ball_x -= gravity

    else:
        ball_x = 375
        random_color = random.choice(color_list)
        ball_y = random.randint(0,HEIGHT)
        gravity = random.randint(1,10)

    #Player 2: basket
    if(ball_x_1 >= x_position2) and (ball_y_1 >= y_position2 and ball_y_1 <= y_position2 + player2_rect_height):
        ball_x_1 = 425
        random_color1 = random.choice(color_list1)
        ball_y_1 = random.randint(0,HEIGHT)
        score1 += 1
        gravity_1 = random.randint(1,10)

    elif ball_x_1 <= WIDTH:
        ball_x_1 += gravity_1
    
    else:
        ball_x_1 = 425
        random_color1 = random.choice(color_list1)
        ball_y_1 = random.randint(0,HEIGHT)
        gravity_1 = random.randint(1,10)
        
    screen.fill(black)
    player1 = font.render("Player 1: " + str(score), True, text_color)
    player2 = font.render("Player 2: " + str(score1), True, text_color)
    player1_score = font.render("Player 1 won", True, text_color)
    player2_score = font.render("Player 2 won", True, text_color)    
    pygame.draw.line(screen, white, (middleline_pos_x, middleline_pos_y), (middleline_pos_x,endmiddleline_pos_y), width=1)
    screen.blit(player1,(25,25))
    screen.blit(player2,(600,25))
    pygame.draw.rect(screen, red, (x_position1, y_position1, player1_rect_width, player1_rect_height))
    pygame.draw.rect(screen, red, (x_position2, y_position2, player2_rect_width, player2_rect_height))
    pygame.draw.circle(screen, random_color, (ball_x,ball_y), radius)
    pygame.draw.circle(screen, random_color1, (ball_x_1,ball_y_1), radius_1)
    check_winner(score,score1,player1_score, player2_score)
    clock.tick(60)
    pygame.display.flip()

pygame.quit()
sys.exit()