"""
    Shape Base Class; Defines a base class for geometric shapes with 
    common attributes such as color and position.

-----------------------------------------------------------------------
"""
class shape:

    """
        __init__

        Initializes a new Shape instance with a color and position.

        Parameters:
        display: The display surface or context the shape is rendered on.
        color (str): The color of the shape (e.g., "red", "blue").
        position (tuple): The (x, y) coordinates of the shape's 
        position.

        Returns:
        None
    """
    def __init__(self, display, color, position):
        self.display = display
        self.color = color
        self.position = position

    def updatePosition(self, position):
        self.position = position

    def getPosition(self):
        return self.position