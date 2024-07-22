import pygame
from constants import *

def draw_objects():
    ''' Drawn on screen, color is white, int() used since division occurs, tuple passed with player position and bat dimensions'''
    pygame.draw.rect(screen, WHITE, (int(p1_x_pos), int(p1_y_pos), paddle_width, paddle_height))
    pygame.draw.rect(screen, WHITE, (int(p2_x_pos), int(p2_y_pos), paddle_width, paddle_height))
    pygame.draw.circle(screen, WHITE, (int(ball_x_pos), int(ball_y_pos)), ball_width) 

    # Scores 
    score = game_font.render(f"{str(p1_score)} - {str(p2_score)}", False, WHITE)
    screen.blit(score, (WIDTH / 2, 30)) # (X, Y)

def apply_player_movement():
    global p1_y_pos
    global p2_y_pos

    if p1_up:
        p1_y_pos = max(p1_y_pos - paddle_speed, 0) # Can't go below 0
    elif p1_down:
        p1_y_pos = min(p1_y_pos + paddle_speed, HEIGHT) # Can't go above HEIGHT

    if p2_up:
        p2_y_pos = max(p2_y_pos - paddle_speed, 0)
    elif p2_down:
        p2_y_pos = min(p2_y_pos + paddle_speed, HEIGHT)

def apply_ball_movement():
    global ball_x_pos, ball_y_pos, ball_x_vel, ball_y_vel, p1_score, p2_score

    # First Scenario - Ball hits paddle on left, reverse X velocity so ball goes to right
    if (ball_x_pos + ball_x_vel < p1_x_pos + paddle_width) and (p1_y_pos < ball_y_pos + ball_y_vel + ball_width < p1_y_pos + paddle_height):
        ball_x_vel = -ball_x_vel
        ''' If balls hits paddle in center (paddle_height / 2 == 0), no change in velocity, else goes up or down '''
        ball_y_vel = (p1_y_pos + paddle_height / 2 - ball_y_pos) / 15 # Subject to change depending on physics
        ball_y_vel = -ball_y_vel

    # Second Scenario - Ball hits the wall 
    elif ball_x_pos + ball_x_vel < 0: # Ball hits left wall
        p2_score += 1
        ball_x_pos = WIDTH / 2
        ball_y_pos = HEIGHT / 2
        ball_x_vel = 20
        ball_y_vel = 0 

    # Identical code for another player
    if (ball_x_pos + ball_x_vel > p2_x_pos - paddle_width) and (p2_y_pos < ball_y_pos + ball_y_vel < p2_y_pos + paddle_height):
        ball_x_vel = -ball_x_vel
        ball_y_vel = (p2_y_pos + paddle_height / 2 - ball_y_pos) / 15
        ball_y_vel = -ball_y_vel
    
    elif ball_x_pos + ball_x_vel > WIDTH:
        p1_score += 1
        ball_x_pos = WIDTH / 2
        ball_y_pos = HEIGHT / 2
        ball_x_vel = -20
        ball_y_vel = 0

    # If ball hits top or bottom wall
    if ball_y_pos + ball_y_vel > HEIGHT or ball_y_pos + ball_y_vel < 0:
        ball_y_vel = -ball_y_vel

    ball_x_pos += ball_x_vel # Ball moves horizontally
    ball_y_pos += ball_y_vel # Ball moves vertically
