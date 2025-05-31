# Import the base Point class
from point import Point
import random


class ColorPoint(Point):
    """
    A subclass of Point that adds a color attribute to the point.
    Inherits coordinate-related behavior from the Point class.
    """

    def __init__(self, x, y, color):
        """
        Initialize a ColorPoint with coordinates (x, y) and a color.

        Parameters:
        x (int or float): The x-coordinate of the point.
        y (int or float): The y-coordinate of the point.
        color (str): The color of the point.
        """
        self.x = x
        self.y = y
        self.color = color

    def __str__(self):
        """
        Return a string representation of the ColorPoint.
        Format: (x, y) (color)
        """
        return f'<{self.x}, {self.y}> ({self.color})'


# This block only runs when the script is executed directly
if __name__ == '__main__':
    """
    Generate a list of 5 random ColorPoint objects, print them, then sort and print again.
    """

    colors = ['red', 'green', 'blue', 'pink', 'orange', 'black', 'white'] # List of allowed colors

    # Generate 5 random ColorPoint objects with random coordinates and colors
    color_point = [
        ColorPoint(random.randint(-100, 100), random.randint(-100, 100), random.choice(colors))
        for i in range(5)
    ]

    # Print the list before sorting
    print('random color points')
    print(color_point)

    # Sort the list of color points
    print('sorted color points')
    color_point.sort()
    print(color_point)