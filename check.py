"""
    Description of file; Purpose of file

-----------------------------------------------------------------------
"""
# Importing libraries & classes
import pygame, sys


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
    
    if math.sqrt((mouse_pos[0] - target_entity.getPosition()[0])**2 + (mouse_pos[1] - \
        target_entity.getPosition()[1])**2) <= target_entity.radius:
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
def check_for_quit(event) -> None:
    if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and \
        event.key == pygame.K_ESCAPE):
        pygame.quit()
        sys.exit()
 

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
def check_for_clicks(event) -> None:
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
                target_entity.updatePosition(generate_circle_pos())
                # print(circle_pos)
                score_ctr += 1