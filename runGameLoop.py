"""
    Description of file; Purpose of file

-----------------------------------------------------------------------
"""
# Importing libraries & classes
import pygame, random, time
from check import check_for_clicks, check_for_quit
from circle import circle
from rectangle import rectangle

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

# --- Timer ---

# Sets the game round length in seconds; Controls how long the player 
# has to click targets
DURATION = 6 # seconds

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

# --- Score Tracking ---

# Tracks number of successful hits; Incremented on each accurate click
score_ctr = 0

# Tracks total number of clicks made; Used to calculate accuracy on 
# results screen
click_ctr = 0

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
def runGameLoop() -> None:
    global show_results, score_ctr, click_ctr, screen, first_loop_of_show_results
    # Game loop
    while True:
        timer_remaining = DURATION - (pygame.time.get_ticks() - \
            start_time) // 1000
        
        events = pygame.event.get()

        # Loop that checks if an event in events list is equal to quit;
        # quits application if True 
        for event in events:
            check_for_quit(event)
            score_ctr, click_ctr = check_for_clicks(event, show_results, \
                score_ctr, click_ctr, target_entity, screen)


        if timer_remaining <= 0:
            timer_remaining = 0
            show_results = True

        # Renders current user's score
        user_score_label = font.render(f"Score: {score_ctr}", True, "black")
        timer_label = font.render(f"Time: {timer_remaining} s", True, "black")
        click_counter_label = font.render(f"Clicks: {click_ctr}", True, "black")

        # Items drawn bottom -> on top -> on top
        screen.fill('purple')
        
        pygame.draw.rect(target_spawning_rectangle.getDisplay(), \
            target_spawning_rectangle.getColor(), (\
            target_spawning_rectangle.getPosition()[0], \
            target_spawning_rectangle.getPosition()[1],\
            target_spawning_rectangle.getLength(), target_spawning_rectangle.getWidth()))
        
        # print(f"show_results={show_results}, drawing frame...")
        if not show_results:
            pygame.draw.circle(target_entity.display, target_entity.color, target_entity.position, \
                target_entity.radius)
        
        screen.blit(user_score_label, (5, 5))
        screen.blit(click_counter_label, (5, 45))
        screen.blit(timer_label, (5, 85))


        if show_results:
            # Items drawn bottom -> on top -> on top
            if first_loop_of_show_results:
                pygame.draw.rect(target_spawning_rectangle.getDisplay(), \
                    target_spawning_rectangle.getColor(), (\
                    target_spawning_rectangle.getPosition()[0], \
                    target_spawning_rectangle.getPosition()[1],\
                    target_spawning_rectangle.getLength(), target_spawning_rectangle.getWidth()))
                # Updates pygame display
                pygame.display.update()
                time.sleep(1)
                first_loop_of_show_results = False
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

        # Updates pygame display
        pygame.display.update()