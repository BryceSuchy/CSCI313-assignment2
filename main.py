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

# Width and height of the screen (width,height)
size = (700, 500)
GREY = (211,211,211)
PINK = (255,192,203)
def draw_cat(screen,x,y):
            pygame.draw.ellipse(screen, GREY, [50+x,50+y,225,175], 0)
            pygame.draw.polygon(screen, GREY, [[60+x,100+y], [135+x,55+y], [75+x,20+y]], 0)
            pygame.draw.polygon(screen, GREY, [[200+x,55+y], [265+x,120+y], [275+x,20+y]], 0)


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
        draw_cat(screen,100,100)
        

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
