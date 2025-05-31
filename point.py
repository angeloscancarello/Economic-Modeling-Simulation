import random

class Point:
    def __init__(self, x, y):
        """
        Initialize a Point object with x and y coordinates.

        :param x: The x-coordinate (int or float).
        :param y: The y-coordinate (int or float).
        """
        self.x = x
        self.y = y

    def __str__(self):
        """
        Return a readable string representation of the point.

        :return: A string in the format "(x, y)".
        """
        return f'<{self.x}, {self.y}>'

    def __repr__(self):
        """
        Return the official string representation of the point, used for debugging and printing lists.

        :return: A string in the format "(x, y)".
        """
        return self.__str__()

    def distance_orig(self):
        """
        Compute the Euclidean distance from the origin (0, 0) to this point.

        :return: Distance as a float.
        """
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __gt__(self, other):
        """
        Compare two points based on their distance from the origin.

        :param other: Another Point object to compare against.
        :return: True if this point is farther from the origin than the other point.
        """
        return self.distance_orig() > other.distance_orig()

    def __eq__(self, other):
        """
        Check if two points are equally distant from the origin.

        :param other: Another Point object to compare against.
        :return: True if both points have the same distance from the origin.
        """
        return self.distance_orig() == other.distance_orig()

if __name__ == '__main__':
    """
    It creates random points, sorts them by distance, and tests
    how often two randomly generated points have the same distance.
    """

    # Create 5 random Point objects with x and y in range [-100, 100]
    points = [Point(random.randint(-100, 100), random.randint(-100, 100)) for i in range(5)]

    print('Unsorted points')
    for point in points:
        print(point)

    print('Sorted points')
    # Sort the points by distance from origin using __gt__ method
    points.sort()
    print(points)

#Equal Distance Simulation
    found_equal = 0  # Number of times we find two equal-distance points
    count = 0        # Total trials run

    while True:
        if found_equal == 10:
            break  # Stop after finding 10 matching-distance pairs

        # Generate two random points
        p1 = Point(random.randint(-100, 100), random.randint(-100, 100))
        p2 = Point(random.randint(-100, 100), random.randint(-100, 100))
        count += 1

        # Check if they have equal distance from the origin
        if p1 == p2:
            # Line below: print the matching pair
            # print(p1, p2)
            found_equal += 1

    # Estimate how rare it is to get two random points with the same distance
    print('probability of equal distance:', count / found_equal)