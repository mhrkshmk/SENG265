from rectangle import Rectangle


class SvgCanvas:
    """
    This class adds the created shapes to the HTML document.
    """

    def __init__(self, width: int, height: int) -> None:
        """
        Initializes a new instance of SvgCanvas.

        Args:
            width (int): The width of the canvas.
            height (int): The height of the canvas.
        """
        self.width = width
        self.height = height
        self.canvas = f"<svg width=\"{self.width}\" height=\"{self.height}\">\n"

    def gen_art(self, shapes: list) -> None:
        """
        It adds html lines that are based on the description provided in shapes argument, to its canvas attribute.

        Args:
            shapes (list): A list containing instances of Circle, Rectangle, or Ellipse
        """
        for shape in shapes:
            self.canvas += str(shape)
        self.close_canvas_tag()

    def close_canvas_tag(self) -> None:
        """
        adds an enclosing tag to the canvas attribute.
        """
        self.canvas += "</svg>"
        print(self.canvas)
