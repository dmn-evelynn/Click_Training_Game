"""
    Description of file; Purpose of file

-----------------------------------------------------------------------
"""


# Importing libraries & classes
import random


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
def generate_circle_pos(screen) -> (int, int):
    while True:
        circle_x = random.randint(0, int(screen.get_size()[0]) - 1)
        circle_y = random.randint(0, int(screen.get_size()[1]) - 1)
        
        color = screen.get_at((circle_x, circle_y))
        RED, GREEN, BLUE = color.r, color.g, color.b

        if RED == 0 and GREEN == 255 and BLUE == 255:
            return (circle_x, circle_y)