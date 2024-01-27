from typing import NamedTuple


class Coordinates(NamedTuple):
    """
    A NamedTuple for holding the values required to represent the coordinates for Circle and Ellipse shapes.

    Values:
        x (int): The value for the x-coordinate.
        y (int): The value for the y-coordinate.
    """
    x: int
    y: int

    def __str__(self) -> str:
        """
        Creates an HTML line for coordinates of Circle and Ellipse shapes.

        Returns:
            str: The created HTML line.
        """
        return f"cx=\"{self.x}\" cy=\"{self.y}\""

class RectangleCoordinates(NamedTuple):
    """
    A NamedTuple for holding the values required to represent the coordinates for Rectangle shapes.

    Values:
        x (int): The value for the x-coordinate.
        y (int): The value for the y-coordinate.
    """
    x: int
    y: int

    def __str__(self) -> str:
        """
        Creates an HTML line for coordinates of Rectangle shapes.

        Returns:
            str: The created HTML line.
        """
        return f'x=\"{self.x}\" y=\"{self.y}\"'