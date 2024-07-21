# Simple Ping Pong Game

import pygame 

# Constants and variables - Dimensions, speed etc 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Size of screen
WIDTH =  600
HEIGHT = 600

pygame.innit()
game_font = pygame.font.SysFont('monospace', 40)

delay = 30 # Game pace, when increased game becomes slower

# Paddle/Bat properties
paddle_speed = 20 

paddle_width = 10
paddle_height = 100

# Player positions
p1_x_pos = 10 
p1_y_pos = HEIGHT / 2 - paddle_height / 2

p2_x_pos = WIDTH - paddle_width - 10
p2_y_pos = HEIGHT / 2 - paddle_height / 2

# Player scores
p1_score = 0
p2_score = 0

# Direction changes
p1_up = False
p1_down =  False 
p2_up = False
p2_down = False

# Ball properties
ball_x_pos = WIDTH / 2
ball_y_pos = HEIGHT / 2

ball_width =  8
ball_x_vel = -10 # Goes left 
ball_y_vel = 0 # Doesn't move vertically
