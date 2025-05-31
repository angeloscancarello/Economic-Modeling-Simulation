from color_point import ColorPoint # Import the base class ColorPoint (assumed to define a colored 2D point)


# Define a new class AdvancedPoint that inherits from ColorPoint
class AdvancedPoint(ColorPoint):  # Inherits from ColorPoint
    COLORS = ['red', 'green', 'blue', 'pink', 'orange', 'black', 'white'] # Class variable: allowed colors for points

    def __init__(self, x, y, color):
        if not isinstance(x, (int, float)): # Validate that x is a number (int or float)
            raise ValueError('x must be an int or float')
        if not isinstance(y, (int, float)): # Validate that y is a number
            raise ValueError('y must be an int or float')
        if not color in self.COLORS: # Validate that color is in the allowed COLORS list
            raise ValueError(f'color must be one of the following: {self.COLORS}')

        # Optional: Call parent constructor if needed
        # super().__init__(x, y, color)

        # Store attributes as "protected" instance variables
        self._x = x
        self._y = y
        self._color = color

    # Property getter for x
    @property
    def x(self):
        return self._x

    # Property getter for y
    @property
    def y(self):
        return self._y

    # Property getter for color
    @property
    def color(self):
        return self._color

    # Property setter for color with validation
    @color.setter
    def color(self, new_color):
        if new_color not in AdvancedPoint.COLORS:
            raise ValueError(f'color must be one of the following: {AdvancedPoint.COLORS}')
        self._color = new_color

    # Class method to add a new color to the shared COLORS list
    @classmethod
    def add_color(cls, new_color):
        cls.COLORS.append(new_color)

    # Static method to compute Euclidean distance between two points
    @staticmethod
    def distance_2_points(p1, p2):
        return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5

    # Static method to create an AdvancedPoint from a dictionary
    @staticmethod
    def from_dictionary(dict):
        x = dict.get('x', 10)  # Default x is 10
        y = dict.get('y', 20)  # Default y is 20
        color = dict.get('color', 'black')  # Default color is 'black'
        return AdvancedPoint(x, y, color)

# Example Usage:
p1 = AdvancedPoint(1, 2, 'red') # Create a point with coordinates (1, 2) and color 'red'
print(p1)  # Will print object reference unless __str__ is defined in ColorPoint

AdvancedPoint.add_color('amber') # Add a new color 'amber' to the allowed COLORS

p2 = AdvancedPoint(1, 2, 'amber') # Create a new point using the newly added color
print(p2.color)  # Should print 'amber'

p2.color = 'blue' # Change p2's color to 'blue'
print(p2)  # Will print object reference unless __str__ is defined

print(AdvancedPoint.distance_2_points(p1, p2)) # Calculate the distance between p1 and p2

p3 = AdvancedPoint.from_dictionary({'x': 100, 'y': 200}) # Create a point from a dictionary (color is missing, defaults to 'black')
print(p3)