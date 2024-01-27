from typing import NamedTuple

class Color(NamedTuple):
    """
    A NamedTuple for holding the values required to represent that color and its opacity in HTML.

    Values:
        r (int): The value for red in rgb.
        g (int): The value for green in rgb.
        b (int): The value for blue in rgb.
        op (float): The value for the opacity of the color.
    """
    r: int
    g: int
    b: int
    op: float

    def __str__(self) -> str:
        """
        Creates an HTML line to add color and opacity to the line.

        Returns:
            str: The created HTML line.
        """
        return f'fill=\"rgb({self.r}, {self.g}, {self.b})\" fill-opacity=\"{self.op}\"'