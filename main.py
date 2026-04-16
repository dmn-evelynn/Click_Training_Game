# This file creates a pygame display that shows a screen the size of the 
# user's display. The screen shows a score in the top left corner with
# circles that show up at random spots on the screen. The user can click
# these circles to increase their score.  

import pygame, sys, math, random

# Initialize pygame
pygame.init()

# Gets monitor resolution size
info = pygame.display.Info()
screen_size = [info.current_w, info.current_h]

# Screen variable that takes in a tuple (x, y)
screen = pygame.display.set_mode((screen_size[0], screen_size[1]))

# Position for circle
circle_pos = (random.randint(0, int(screen_size[0])), random.randint(0, int(screen_size[1])))

# Radius width for circle
circle_width = 65

# Font variable used for rendering score and timer
font = pygame.font.Font("cour.ttf", 30)

# Starting score
score_ctr = 0

# Timer duration
DURATION = 9 # seconds


show_results = False

# Start time for timer
start_time = pygame.time.get_ticks()

def check_circle_collision() -> bool:
    mouse_pos = pygame.mouse.get_pos()

    if math.sqrt((mouse_pos[0] - circle_pos[0])**2 + (mouse_pos[1] - circle_pos[1])**2) <= circle_width:
        return True
    return False

def check_for_quit(event) -> bool:
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

def check_for_clicks(event) -> bool:
    global score_ctr, circle_pos
    # If event mouse button down is found (clicking) then checks if circle was clicked/collided with
    if event.type == pygame.MOUSEBUTTONDOWN:
        # 1 = left click; 3 = right click
        if event.button == 1 or event.button == 3:
            # Changes circle position & adds points to score counter
            if check_circle_collision():
                circle_pos = (random.randint(0, int(screen_size[0])), random.randint(0, int(screen_size[1])))
                score_ctr += 1

# Game loop
while True:
    timer_remaining = DURATION - (pygame.time.get_ticks() - start_time) // 1000
    
    events = pygame.event.get()

    # Loop that checks if an event in events list is equal to quit;
    # quits application if True 
    for event in events:
        check_for_quit(event)

        if timer_remaining < 0:
            show_results = True
        
        check_for_clicks(event)

        # Renders current user's score
        user_score_label = font.render(f"Score: {score_ctr}", True, "black")
        timer_label = font.render(f"Time: {timer_remaining} s", True, "black")

    if show_results:
        # Items drawn bottom -> on top -> on top
        screen.fill('orange')
        screen.blit(user_score_label, (screen_size[0]/2, screen_size[1]/3))
    else:
        # Items drawn bottom -> on top -> on top
        screen.fill('purple')
        pygame.draw.circle(screen, "orange", circle_pos, circle_width)
        screen.blit(user_score_label, (5, 5))
        screen.blit(timer_label, (5, 30))

    # Updates pygame display
    pygame.display.update()