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
from runGameLoop import runGameLoop









"""
    main

    Entry point of the program. Initiates the game by calling the main game loop.

    Parameters:
    None

    Returns:
    None: This function does not return a value.
"""
def main() -> None:
    runGameLoop()

# --- Main Entry Point ---

# Standard Python idiom; ensures main() only runs when script is executed directly
if __name__ == "__main__":
    main()