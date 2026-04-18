# This file creates a pygame display that shows a screen the size of the 
# user's display. The screen shows a score in the top left corner with
# circles that show up at random spots on the screen. The user can click
# these circles to increase their score. 
# 
# The following tutorial was used to assist in the making of this program
# as well as referring to the pygame docs:
# https://youtu.be/dz9_-2G6o3o?si=d3t_dHBIr09ZDiqm
# 
# ----------------------------------------------------------------------- 

import pygame, sys, math, random

# Initialize pygame
pygame.init()

# Gets monitor resolution size
info = pygame.display.Info()
screen_size = [info.current_w, info.current_h]

# Screen variable that takes in a tuple (x, y)
screen = pygame.display.set_mode((screen_size[0]/2, screen_size[1]/2))

# Position for circle
circle_pos = (random.randint(screen.get_size()[0] // 3, screen.get_size()[0] // 2), \
    random.randint(screen.get_size()[1] // 3, screen.get_size()[1] // 2))

# Radius width for circle
circle_width = 95

# Font variable used for rendering score and timer
font = pygame.font.Font("cour.ttf", 30)

# Starting scores
score_ctr = 0
click_ctr = 0

# Timer duration
DURATION = 6 # seconds
# Boolean that determines if results screen should be shown
show_results = False

# Start time for timer
start_time = pygame.time.get_ticks()

def check_circle_collision() -> bool:
    mouse_pos = pygame.mouse.get_pos()

    if math.sqrt((mouse_pos[0] - circle_pos[0])**2 + (mouse_pos[1] - circle_pos[1])**2) <= circle_width:
        return True
    return False

def check_for_quit(event) -> bool:
    if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
        pygame.quit()
        sys.exit()

def generate_circle_pos() -> (int, int):
    while True:
        circle_x = random.randint(0, int(screen.get_size()[0]) - 1)
        circle_y = random.randint(0, int(screen.get_size()[1]) - 1)
        
        color = screen.get_at((circle_x, circle_y))
        RED, GREEN, BLUE = color.r, color.g, color.b

        if RED == 0 and GREEN == 255 and BLUE == 255:
            return (circle_x, circle_y)
        

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

# Game loop
while True:
    timer_remaining = DURATION - (pygame.time.get_ticks() - start_time) // 1000
    
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
        screen.blit(user_score_label, (screen.get_size()[0]/3, screen.get_size()[1]/2))
        screen.blit(click_counter_label, (screen.get_size()[0]/3, screen.get_size()[1]/2 + 40))

        if click_ctr != 0:
            accuracy_label = font.render(f"Accuracy: {(score_ctr / click_ctr) * 100:.2f}%", True, "black")
            screen.blit(accuracy_label, (screen.get_size()[0]/3, screen.get_size()[1]/2 + 80))
    else:
        # Items drawn bottom -> on top -> on top
        screen.fill('purple')
        pygame.draw.rect(screen, "aqua", (100, 150, screen.get_size()[0] - 200, screen.get_size()[1] - 350))
        pygame.draw.circle(screen, "orange", circle_pos, circle_width)
        screen.blit(user_score_label, (5, 5))
        screen.blit(click_counter_label, (5, 45))
        screen.blit(timer_label, (5, 85))

    # Updates pygame display
    pygame.display.update()