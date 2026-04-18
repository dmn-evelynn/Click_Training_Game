"""
    Description of file; Purpose of file

-----------------------------------------------------------------------
"""


# Importing libraries & classes
import pygame


# --- Timer ---

# Sets the game round length in seconds; Controls how long the player 
# has to click targets
DURATION = 6 # seconds


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