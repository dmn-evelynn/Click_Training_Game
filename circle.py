"""
    Circle Shape Class; Defines a Circle subclass of Shape with color, 
    position, and radius attributes.

-----------------------------------------------------------------------
"""
from shape import shape

class circle(shape):
    """
        __init__

        Initializes a Circle instance with a color, position, and radius.

        Parameters:
        display: The display surface or context the shape is rendered on.
        color (str): The color of the shape (e.g., "red", "blue").
        position (tuple): The (x, y) coordinates of the shape's 
        position.
        radius (float): The radius of the circle.

        Returns:
        None
    """
    def __init__(self, display, color, position, radius):
        super().__init__(display, color, position)
        self.radius = radius

    def getRadius(self):
        return self.radius