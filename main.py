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
            
            pygame.draw.polygon(screen, GREY, [[60+x,100+y], [125+x,55+y], [60+x,35+y]], 0)#Left Ear
            pygame.draw.polygon(screen, PINK, [[65+x,100+y], [115+x,65+y], [65+x,50+y]], 0)
            pygame.draw.polygon(screen, GREY, [[200+x,55+y], [265+x,120+y], [275+x,40+y]], 0)#Right Ear
            pygame.draw.polygon(screen, PINK, [[225+x,60+y], [255+x,140+y], [265+x,50+y]], 0)
            pygame.draw.ellipse(screen, GREY, [50+x,50+y,225,175], 0) #head
            pygame.draw.polygon(screen, PINK, [[140+x,150+y], [185+x,150+y], [162+x,180+y]], 0)#nose
            pygame.draw.ellipse(screen, WHITE, [90+x,85+y,55,45], 0) #Left Eye
            pygame.draw.ellipse(screen, BLACK, [96+x,90+y,45,35], 0)
            pygame.draw.ellipse(screen, WHITE, [110+x,94+y,10,10], 0) #white light speckles
            pygame.draw.ellipse(screen, WHITE, [123+x,98+y,10,10], 0)
            pygame.draw.ellipse(screen, WHITE, [122+x,95+y,5,5], 0)
            z = 90
            pygame.draw.ellipse(screen, WHITE, [90+x+z,85+y,55,45], 0) #Right Eye
            pygame.draw.ellipse(screen, BLACK, [96+x+z,90+y,45,35], 0)
            pygame.draw.ellipse(screen, WHITE, [110+x+z,94+y,10,10], 0) #white light speckles
            pygame.draw.ellipse(screen, WHITE, [123+x+z,98+y,10,10], 0)
            pygame.draw.ellipse(screen, WHITE, [122+x+z,95+y,5,5], 0)

            
            

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
