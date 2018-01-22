"""
Assignment 2
# Your names here

# Give a description of what your new program does


Original documentation: (Leave this intact)
Pygame base template for opening a window, done with functions
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

Source: http://programarcadegames.com/python_examples/show_file.php?file=pygame_base_template_proper.py
Modified slightly by OttoBorchert 1/18/2018
 
"""
 
import pygame
 
# Define some colors as global constants (can add colors, if you'd like)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255,255,0)

# Width and height of the screen (width,height)
size = (700, 500)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
# josh zickermann
def draw_house(screen, x, y):
    pygame.draw.rect(screen, BLACK, [40+x,40+y,100,100], 2)
    pygame.draw.polygon(screen, BLACK, [[40+x,40+y], [140+x,40+y],[92.5+x,0+y]])
    pygame.draw.rect(screen, BLUE, [60+x,65+y,20,20])
    pygame.draw.rect(screen, BLUE, [100+x,65+y,20,20])
    pygame.draw.rect(screen, RED, [80+x,100+y,20,40])

# Made by Bryce Suchy
def draw_sun(screen, x, y):
    pygame.draw.circle(screen,YELLOW,[200+x,200+y],80, 80)
    pygame.draw.polygon(screen, YELLOW, [[100+x, 100+y], [115+x, 200+y], [200+x, 115+y]], 10)
    pygame.draw.polygon(screen, YELLOW, [[200+x, 280+y], [115+x, 200+y], [90+x, 250+y]], 10)
    pygame.draw.polygon(screen, YELLOW, [[275+x, 200+y], [300+x, 50+y], [200+x, 115+y]], 10)
    pygame.draw.polygon(screen, YELLOW, [[275+x, 200+y], [275+x, 320+y], [200+x, 280+y]], 10)
    pygame.draw.line(screen, YELLOW, [215+x, 225+y], [370+x,215+y], 10)
    pygame.draw.line(screen, YELLOW, [215+x, 150+y], [370+x,215+y], 10)


def main():
    """ Main function for the game. """
    
    pygame.init()
    # Set the width and height of the screen [width,height]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("My Game")
 
    # Loop until the user clicks the close button.
    done = False
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
 
    # -------- Main Program Loop -----------
    while not done:
        # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT
 
        # GAME LOGIC BEGIN
 
        # GAME LOGIC END
 
        # DRAW CODE BEGIN
 
        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        screen.fill(WHITE)

        #josh zickermann
        draw_house(screen, 500, 300)
        draw_sun(screen, 350, -50)

        # DRAW CODE END
 
        # Update the screen with what we've drawn.
        pygame.display.flip()
 
        # Limit to 60 frames per second
        clock.tick(60)

    # Close the window and quit.
    # If you forget this line, the program will 'hang'
    # on exit if running from IDLE.
    pygame.quit()
 
if __name__ == "__main__":
    main()
