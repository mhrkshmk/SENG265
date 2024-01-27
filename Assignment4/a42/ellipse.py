from typing import NamedTuple
from coordinates import Coordinates
from color import Color

class EllipseTuple(NamedTuple):
    """
    A NamedTuple for holding the values required to represent the x and y radius of the Ellipse shape.

    Values:
        rad_x (int): The value for the x-radius.
        rad_y (int): The value for the y-radius.
    """
    rad_x: int
    rad_y: int

    def __str__(self) -> str:
        """
        Creates an HTML line for the radiuses of the Ellipse shape.

        Returns:
            str: The created HTML line.
        """
        return f'rx=\"{self.rad_x}\" ry=\"{self.rad_y}\"'


class Ellipse:
    """
    This class holds and writes to HTML document the values needed to create an ellipse.
    """

    def __init__(self, cor: Coordinates, rad: EllipseTuple, color: Color):
        """
        Creates a new instance of the class.

        Args:
            cor (Coordinates): The coordinates for the middle of the ellipse shape.
            rad (EllipseTuple): The values for the x and y radius of the ellipse.
            color (Color): The values for the color of the ellipse.
        """
        self.cor = cor
        self.rad = rad
        self.color = color

    def __str__(self) -> str:
        """
        Creates a HTML line for an ellipse with the given specifications.

        Returns:
            str: The created HTML line.
        """
        return f"<ellipse {self.cor} {self.rad} {self.color}></ellipse>\n"