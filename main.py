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

# Importing libraries
import pygame, sys, math, random

# Single Lined Comments:

# Description of line; Purpose of line

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
circle_pos = (random.randint(screen.get_size()[0] // 3, screen.get_size()[0] // 2), \
    random.randint(screen.get_size()[1] // 3, screen.get_size()[1] // 2))

# Defines the radius of the clickable circle in pixels; Controls target
# hit area size
circle_width = 95

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

# --- Timer & Game State ---

# Sets the game round length in seconds; Controls how long the player 
# has to click targets
DURATION = 6 # seconds

# Flags whether the results screen is active; Toggled to True when the
# timer expires
show_results = False

# Records the time the game started in milliseconds; Used to calculate
# elapsed time each frame
start_time = pygame.time.get_ticks()


"""
    check_circle_collision

    Checks whether the mouse cursor is currently within the bounds of a circle
    by calculating the Euclidean distance between the mouse position and the
    circle's center, and comparing it against the circle's radius.

    Parameters:
    None

    Returns:
    bool: True if the mouse cursor is within or on the circle's boundary,
          False otherwise.
"""
def check_circle_collision() -> bool:
    mouse_pos = pygame.mouse.get_pos()

    if math.sqrt((mouse_pos[0] - circle_pos[0])**2 + (mouse_pos[1] - \
        circle_pos[1])**2) <= circle_width:
        return True
    return False


"""
    check_for_quit

    Checks if the given event is a quit or escape key event, and if so,
    shuts down pygame and exits the program.

    Parameters:
    event (pygame.event.Event): The pygame event to evaluate.

    Returns:
    bool: Does not return a value under normal execution; exits the program if a quit event is detected.
"""
def check_for_quit(event) -> bool:
    if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and \
        event.key == pygame.K_ESCAPE):
        pygame.quit()
        sys.exit()


"""
    generate_circle_pos

    Randomly generates a valid (x, y) position on the screen where the pixel
    color is cyan (R=0, G=255, B=255). Continues generating random positions
    until a matching pixel is found.

    Parameters:
    None

    Returns:
    tuple (int, int): A tuple containing the x and y coordinates of a cyan pixel.
"""
def generate_circle_pos() -> (int, int):
    while True:
        circle_x = random.randint(0, int(screen.get_size()[0]) - 1)
        circle_y = random.randint(0, int(screen.get_size()[1]) - 1)
        
        color = screen.get_at((circle_x, circle_y))
        RED, GREEN, BLUE = color.r, color.g, color.b

        if RED == 0 and GREEN == 255 and BLUE == 255:
            return (circle_x, circle_y)
        

"""
    check_for_clicks

    Handles mouse click events during gameplay, checking whether the user clicked
    on the circle and updating the score and circle position accordingly.

    Parameters:
    event (pygame.event.Event): The Pygame event object captured from the event loop.

    Returns:
    bool: Returns None implicitly if show_results is True (interaction blocked),
        otherwise processes the click event and updates game state.
"""
def check_for_clicks(event) -> bool:
    global score_ctr, circle_pos, click_ctr

    # If show_results is True then prevent user from being able to interact with game components.
    if show_results:
        return

    # If event mouse button down is found (clicking) then checks if circle was clicked/collided with
    if event.type == pygame.MOUSEBUTTONDOWN:
        # 1 = left click; 3 = right click
        if event.button == 1 or event.button == 3:
            click_ctr += 1
            # Changes circle position & adds points to score counter
            if check_circle_collision():
                circle_pos = generate_circle_pos()
                # print(circle_pos)
                score_ctr += 1


"""
    run_game_loop

    Runs the main game loop, handling events, updating the display, and
    switching between the active game view and the results screen when
    the timer expires.

    Parameters:
    None

    Returns:
    None: Runs indefinitely until the application is quit.
"""
def run_game_loop() -> None:
    global show_results
    # Game loop
    while True:
        timer_remaining = DURATION - (pygame.time.get_ticks() - \
            start_time) // 1000
        
        events = pygame.event.get()

        # Loop that checks if an event in events list is equal to quit;
        # quits application if True 
        for event in events:
            check_for_quit(event)
            check_for_clicks(event)


        if timer_remaining < 0:
            show_results = True

        # Renders current user's score
        user_score_label = font.render(f"Score: {score_ctr}", True, "black")
        timer_label = font.render(f"Time: {timer_remaining} s", True, "black")
        click_counter_label = font.render(f"Clicks: {click_ctr}", True, "black")

        if show_results:
            # Items drawn bottom -> on top -> on top
            screen.fill('orange')
            
            screen.blit(user_score_label, (screen.get_size()[0]/3, \
                screen.get_size()[1]/2))
            
            screen.blit(click_counter_label, (screen.get_size()[0]/3, \
                screen.get_size()[1]/2 + 40))

            if click_ctr != 0:
                
                accuracy_label = font.render(f"Accuracy: {(score_ctr \
                    / click_ctr) * 100:.2f}%", True, "black")
                screen.blit(accuracy_label, (screen.get_size()[0]/3, \
                    screen.get_size()[1]/2 + 80))
        else:
            # Items drawn bottom -> on top -> on top
            screen.fill('purple')
            
            pygame.draw.rect(screen, "aqua", (100, 150, \
                screen.get_size()[0] - 200, screen.get_size()[1] - 350))
            
            pygame.draw.circle(screen, "orange", circle_pos, \
                circle_width)
            
            screen.blit(user_score_label, (5, 5))
            screen.blit(click_counter_label, (5, 45))
            screen.blit(timer_label, (5, 85))

        # Updates pygame display
        pygame.display.update()


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