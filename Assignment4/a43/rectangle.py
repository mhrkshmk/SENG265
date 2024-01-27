from typing import NamedTuple
from coordinates import RectangleCoordinates
from color import Color

class RectangleTuple(NamedTuple):
    """
    A NamedTuple for holding the values required to represent the width and height of the Rectangle shape.

    Values:
        width (int): The value for the width of the rectangle.
        height (int): The value for the height of the rectangle.
    """
    width: int
    height: int

    def __str__(self) -> str:
        """
        Creates an HTML line for the sides of the Rectangle.

        Returns:
            str: The created HTML line.
        """
        return f'width=\"{self.width}\" height=\"{self.height}\"'

class Rectangle:
    """
    This class holds and writes to HTML document the values needed to create a rectangle.
    """

    def __init__(self, cor: RectangleCoordinates, sides: RectangleTuple, color: Color):
        """
        Creates a new instance of the class.

        Args:
            cor (RectangleCoordinates): The coordinates for the top-left of the rectangle shape.
            sides (RectangleTuple): The values for the sides of the rectangle.
            color (Color): The color and opacity values for the rectangle shape.
        """
        self.cor = cor
        self.sides = sides
        self.color = color

    def __str__(self) -> str:
        """
        Creates a new HTML line for a rectangle with the given specifications.

        Returns:
            str: The created HTML line.
        """
        return f"<rect {self.cor} {self.sides} {self.color}></rect>\n"