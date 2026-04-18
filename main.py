"""
    This file creates a pygame display that shows a screen with a 
    score counter, a click counter, and a timer in the top left corner 
    with circles that show up at random spots within the aqua box. The 
    user can click these circles to increase their score. An accuracy 
    score will be calculated at the end of the time.

    The following tutorial was used to assist in the making of this 
    program as well as referring to the pygame docs:
    https://youtu.be/dz9_-2G6o3o?si=d3t_dHBIr09ZDiqm

-----------------------------------------------------------------------
"""

# Importing libraries & classes
import sys, math, random, time
from circle import circle
from rectangle import rectangle
from runGL import run_game_loop

# --- Pygame Initialization ---

# Initializes all pygame modules; Required before using any pygame 
# functionality
pygame.init()

# --- Display & Screen Setup ---

# Retrieves current monitor information; Used to get native screen 
# resolution
info = pygame.display.Info()

# Stores monitor width and height as a list; Used to calculate 
# half-resolution window size
screen_size = [info.current_w, info.current_h]

# Creates the game window at half the monitor resolution; Main surface
# for all rendering
screen = pygame.display.set_mode((screen_size[0]/2, screen_size[1]/2))

# --- Circle Properties ---

# Generates a random (x, y) position within the middle third of the 
# screen; Sets initial target location
circle_pos = (random.randint(screen.get_size()[0] // 3, \
    screen.get_size()[0] // 2), random.randint(screen. \
        get_size()[1] // 3, screen.get_size()[1] // 2))

circle_radius = 65

# Creates a circle class with specified display, color, position, & radius 
target_entity = circle(screen, "orange", circle_pos, circle_radius)

# --- Rectangle Properties ---

# Creates a rectangle class with specified display, color, position, 
# length, & width
target_spawning_rectangle = rectangle(screen, "aqua", (100, 150), \
    screen.get_size()[0] - 200, screen.get_size()[1] - 350)

# --- UI & Font ---

# Loads Courier font at size 30; Used to render score and timer text on
# screen
font = pygame.font.Font("cour.ttf", 30)

# --- Score Tracking ---

# Tracks number of successful hits; Incremented on each accurate click
score_ctr = 0

# Tracks total number of clicks made; Used to calculate accuracy on 
# results screen
click_ctr = 0

# --- Game State ---

# Flags whether the results screen is active; Toggled to True when the
# timer expires
show_results = False

# Flags whether it is the first loop of show_results being set to True;
# Toggled to False after first visit
first_loop_of_show_results = True

# Records the time the game started in milliseconds; Used to calculate
# elapsed time each frame
start_time = pygame.time.get_ticks()








"""
    main

    Entry point of the program. Initiates the game by calling the main game loop.

    Parameters:
    None

    Returns:
    None: This function does not return a value.
"""
def main() -> None:
    run_game_loop()

# --- Main Entry Point ---

# Standard Python idiom; ensures main() only runs when script is executed directly
if __name__ == "__main__":
    main()