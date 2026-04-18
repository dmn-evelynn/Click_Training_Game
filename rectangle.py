"""
    Defines a Rectangle shape that inherits from the base Shape class,
    representing a rectangle with a specific length and width.

-----------------------------------------------------------------------
"""
from shape import shape

class rectangle(shape):
    """
        __init__

        Initializes a new Shape instance with a color and position.

        Parameters:
        display: The display surface or context the shape is rendered on.
        color (str): The color of the shape (e.g., "red", "blue").
        position (tuple): The (x, y) coordinates of the shape's 
        position.
        length (int/float): The length of the rectangle.
        width (int/float): The width of the rectangle.

        Returns:
        None
    """
    def __init__(self, display, color, position, length, width):
        super().__init__(display, color, position)
        self.length = length
        self.width = width