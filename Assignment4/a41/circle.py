from coordinates import Coordinates
from color import Color

class Circle:
    """
    This class holds and writes to HTML document the values needed to create a circle.
    """

    def __init__(self, cor: Coordinates, radius: int, color: Color):
        """
        Creates a new instance of the class.

        Args:
            cor (Coordinates): The coordinates for the middle of the circle.
            radius (int): The radius of the circle.
            color (Color): The color of the circle.
        """
        self.cor = cor
        self.radius = radius
        self.color = color

    def __str__(self) -> str:
        """
        Creates a HTML line for a circle with the given specifications.

        Returns:
            str: The created HTML line.
        """
        return f"<circle {self.cor} r=\"{self.radius}\" {self.color}></circle>\n"