# Simple Ping Pong Game

import pygame 

# Constants and variables - Dimensions, speed etc 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Size of screen
WIDTH =  600
HEIGHT = 600

pygame.init()
game_font = pygame.font.SysFont('monospace', 40)

delay = 30 # Game pace, when increased game becomes slower

# Paddle/Bat properties
paddle_speed = 15

paddle_width = 10
paddle_height = 75

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
ball_x_vel = -15 # Goes left 
ball_y_vel = 0 # Doesn't move vertically

# Draw game components
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Create screen, pass tuple for size

# Drawing objects 
def draw_objects():
    ''' Drawn on screen, color is white, int() used since division occurs, tuple passed with player position and bat dimensions'''
    pygame.draw.rect(screen, WHITE, (int(p1_x_pos), int(p1_y_pos), paddle_width, paddle_height))
    pygame.draw.rect(screen, WHITE, (int(p2_x_pos), int(p2_y_pos), paddle_width, paddle_height))
    pygame.draw.circle(screen, WHITE, (int(ball_x_pos), int(ball_y_pos)), ball_width) 

    # Scores 
    score = game_font.render(f"{str(p1_score)} - {str(p2_score)}", False, WHITE)
    screen.blit(score, (WIDTH / 2, 30)) # (X, Y)

def apply_player_movement():
    global p1_y_pos # Vertical movement only 
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
        ball_x_vel = 15
        ball_y_vel = 0 

    # Identical code for another player
    if (ball_x_pos + ball_x_vel > p2_x_pos - paddle_width) and (p2_y_pos < ball_y_pos + ball_y_vel < p2_y_pos + paddle_height):
        ball_x_vel = -ball_x_vel
        ball_y_vel = (p2_y_pos + paddle_height / 2 - ball_y_pos) / 15
        ball_y_vel = -ball_y_vel
    
    elif ball_x_pos + ball_x_vel > HEIGHT:
        p1_score += 1
        ball_x_pos = WIDTH / 2
        ball_y_pos = HEIGHT / 2
        ball_x_vel = -15
        ball_y_vel = 0

    # If ball hits top or bottom wall
    if ball_y_pos + ball_y_vel > HEIGHT or ball_y_pos + ball_y_vel < 0:
        ball_y_vel = -ball_y_vel

    ball_x_pos += ball_x_vel # Ball moves horizontally
    ball_y_pos += ball_y_vel # Ball moves vertically

# Main Game Loop 
pygame.display.set_caption("Ping Pong")
screen.fill(BLACK)
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            if event.key == pygame.K_e:
                p1_up = True

            if event.key == pygame.K_d:
                p1_down = True

            if event.key == pygame.K_i:
                p2_up = True

            if event.key == pygame.K_k:
                p2_down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_e:
                p1_up = False

            if event.key == pygame.K_d:
                p1_down = False

            if event.key == pygame.K_i:
                p2_up = False

            if event.key == pygame.K_k:
                p2_down = False

    screen.fill(BLACK)    
    apply_player_movement()
    apply_ball_movement()
    draw_objects()
    pygame.display.flip()
    pygame.time.delay(delay) 