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
BC = (226, 226, 215)

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

def draw_stick_figure(screen, x, y):
    # Head
    pygame.draw.ellipse(screen, BLACK, [1 + x, y, 10, 10], 0)
 
    # Legs
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [10 + x, 27 + y], 2)
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [x, 27 + y], 2)
 
    # Body
    pygame.draw.line(screen, RED, [5 + x, 17 + y], [5 + x, 7 + y], 2)
 
    # Arms
    pygame.draw.line(screen, RED, [5 + x, 7 + y], [9 + x, 17 + y], 2)
    pygame.draw.line(screen, RED, [5 + x, 7 + y], [1 + x, 17 + y], 2)

def draw_snowman(screen, x, y):
    # Draw a circle for the head
    pygame.draw.ellipse(screen, WHITE, [35 + x, y, 25, 25])
    # Draw the middle snowman circle
    pygame.draw.ellipse(screen, WHITE, [23 + x, 20 + y, 50, 50])
    # Draw the bottom snowman circle
    pygame.draw.ellipse(screen, WHITE, [x, 65 + y, 100, 100])

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
    # Starting position of the sun
    sun_x = 1000
    sun_y = -50
 
    # Speed and direction of sun
    sun_change_x = -2
    sun_change_y = 0

    ##speed and position of cat
    cat_x = 5
    cat_y = 5
    cat_x_speed = 5
    cat_y_speed = 5

    # Speed in pixels per frame
    x_speed = 0
    y_speed = 0
 
    # Current position
    x_coord = 10
    y_coord = 500

    pygame.mouse.set_visible(0)

    font = pygame.font.Font(None , 25)
 
    # -------- Main Program Loop -----------
    while not done:
        # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
        pos = pygame.mouse.get_pos()
        x_mouse = pos[0]
        y_mouse = pos[1]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            elif event.type == pygame.KEYDOWN:
                # Figure out if it was an arrow key. If so
                # adjust speed.
                if event.key == pygame.K_LEFT:
                    x_speed = -3
                elif event.key == pygame.K_RIGHT:
                    x_speed = 3
                elif event.key == pygame.K_UP:
                    y_speed = -3
                elif event.key == pygame.K_DOWN:
                    y_speed = 3
                elif event.key == pygame.K_SPACE:
                    y_coord = y_coord - 50
 
            # User let up on a key
            elif event.type == pygame.KEYUP:
                # If it is an arrow key, reset vector back to zero
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_speed = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_speed = 0
        # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT
 
        # GAME LOGIC BEGIN
        if x_coord > 1100:
            x_coord = x_coord - 1
        elif y_coord > 680:
            y_coord = y_coord - 1
        elif x_coord < 0:
            x_coord = x_coord + 1
        elif y_coord < 510:
            y_coord = y_coord + 1
        else:
            x_coord = x_coord + x_speed
            y_coord = y_coord + y_speed
    
        # GAME LOGIC END
 
        # DRAW CODE BEGIN
 
        # First, clear the screen to custom color. Don't put other drawing commands
        # above this, or they will be erased with this command.
        screen.fill(BC)

        pygame.draw.rect(screen, GREEN, [0,540,1200,200], 0)

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
        
        # sun animation
        if sun_x != -500:
            draw_sun(screen, sun_x, sun_y)
        else:
            sun_x = 1000
 
        # Move the sun's starting point
        sun_x += sun_change_x
        sun_y += sun_change_y

        draw_stick_figure(screen, x_coord, y_coord)
        
        if x_mouse > 1000:
            x_mouse = 1000
        elif y_mouse > 680:
            y_mouse = 500
        draw_snowman(screen, x_mouse, y_mouse)

        output_string = "Controls: Up-key = Stickman goes up"
        text = font.render(output_string, True, BLACK)
        screen.blit(text, [800, 50])
        output_string = "Down-key = Stickman goes down"
        text = font.render(output_string, True, BLACK)
        screen.blit(text, [800, 65])
        output_string = "Left-key = Stickman goes left"
        text = font.render(output_string, True, BLACK)
        screen.blit(text, [800, 80])
        output_string = "Right-key = Stickman goes right"
        text = font.render(output_string, True, BLACK)
        screen.blit(text, [800, 95])
        output_string = "Space bar = Stickman jumps"
        text = font.render(output_string, True, BLACK)
        screen.blit(text, [800, 110])

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
