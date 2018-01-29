"""
Assignment 3
# Bryce Suchy, Josh Zickermann, and Callahan Stewart

# This program opens a window and draws a cat, house, and sun
This program animates both the sun and cat. Also, randomly draws 4 houses.


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
import random
 
# Define some colors as global constants (can add colors, if you'd like)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255,255,0)
GREY = (211,211,211)
PINK = (255,192,203)

# Width and height of the screen (width,height)
size = (1200, 700)

# Callahan Stewart
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

house_list = []

for i in range(4):
    x = random.randrange(0, 1000)
    house_list.append(x)


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
    # Starting position of the rectangle
    rect_x = 1000
    rect_y = -50
 
    # Speed and direction of rectangle
    rect_change_x = -2
    rect_change_y = 0

    ##speed and position of cat
    cat_x = 5
    cat_y = 5
    cat_x_speed = 5
    cat_y_speed = 5
 
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

        #makes new houses
        for i in range(len(house_list)):
            draw_house(screen, house_list[i], 400)

        # cat animation
        draw_cat(screen, cat_x, cat_y)

        cat_x += cat_x_speed
        cat_y += cat_y_speed
        if cat_y > 450 or cat_y < 0:
            cat_y_speed = cat_y_speed * -1
        if cat_x > 650 or cat_x < 0:
            cat_x_speed = cat_x_speed * -1
        
        ## sun animation
        if rect_x != -500:
            draw_sun(screen, rect_x, rect_y)
        else:
            rect_x = 1000
 
        # Move the rectangle starting point
        rect_x += rect_change_x
        rect_y += rect_change_y

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
