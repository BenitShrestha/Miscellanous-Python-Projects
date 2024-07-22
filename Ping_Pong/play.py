import pygame
from constants import *
from functions import draw_objects, apply_player_movement, apply_ball_movement

def main():
    global p1_up, p1_down, p2_up, p2_down

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

if __name__ == "__main__":
    main()
