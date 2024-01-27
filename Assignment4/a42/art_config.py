from random import randint
from color import Color
from rectangle import RectangleTuple
from ellipse import EllipseTuple
from coordinates import Coordinates

class ArtConfig:
    """
    This class is for creation, holding, and printing the value shapes.
    The class variables hold the default minimum and maximum value for the ranges given in the table as a tuple.
    """

    cnt: int = 0
    shape_rng = (0, 3)
    circ_rad_rng = (0, 100)
    x_cor_rng = (0, 3072)
    y_cor_rng = (0, 1920)
    rect_side_rng = (10, 100)
    ell_rad_rng = (10, 30)
    color_rng = (0, 255)
    op_rng = (0, 10)
    shapes: list = [
        ["CNT", "SHA", "X", "Y", "RAD", "RX", "RY", "W", "H", "R", "G", "B", "OP"]
    ]

    def __init__(self, color: Color = Color(255, 0, 0, 0.5)):
        """Initializes the values for the new instance of ArtConfig

        Args:
            color (Color, optional): The values we want. If a value is set to -1, we randomly generate it again. Defaults to Color(255, 0, 0, 0.5).
        """
        self.fill = color

    def create_color(self):
        """
        Randomly creates values for the shape we are creating, except for the values that are given by default.
        """
        r, g, b, op = self.fill
        if r == -1:
            r = randint(self.color_rng[0], self.color_rng[1])
        if g == -1:
            g = randint(self.color_rng[0], self.color_rng[1])
        if b == -1:
            b = randint(self.color_rng[0], self.color_rng[1])
        if op == -1:
            op = randint(self.op_rng[0], self.op_rng[1]) / 10
        self.color = Color(r, g, b, op)

    def create_sides(self):
        """
        Creates random values for the height and width of a rectangle.
        """
        height = randint(self.rect_side_rng[0], self.rect_side_rng[1])
        width = randint(self.rect_side_rng[0], self.rect_side_rng[1])
        self.side = RectangleTuple(height = height, width = width)

    def create_circle(self):
        """
        Creates random value for the radius of a circle.
        """
        self.rad = randint(self.circ_rad_rng[0], self.circ_rad_rng[1])

    def create_ellipse(self):
        """
        Creates the x and y radius for an ellipse shape.
        """
        rx = randint(self.ell_rad_rng[0], self.ell_rad_rng[1])
        ry = randint(self.ell_rad_rng[0], self.ell_rad_rng[1])
        self.ell_rad = EllipseTuple(rad_x = rx, rad_y = ry)

    def create_coordinates(self):
        """
        Creates random values for the coordinates of the shape.
        """
        x = randint(self.x_cor_rng[0], self.x_cor_rng[1])
        y = randint(self.y_cor_rng[0], self.y_cor_rng[1])
        self.cor = Coordinates(x, y)

    def gen_shape(self):
        """
        Creates a list of random specifications, then appends the created value as a new item to list of shapes already created.
        """
        self.sha = randint(self.shape_rng[0], self.shape_rng[1])
        self.create_color()
        self.create_circle()
        self.create_ellipse()
        self.create_coordinates()
        self.create_sides()
        self.shapes.append([self.cnt, self.sha, self.cor.x, self.cor.y, self.rad, self.ell_rad.rad_x, self.ell_rad.rad_y, self.side.width, self.side.height, self.color.r, self.color.g, self.color.b, self.color.op])
        self.cnt += 1

    def print_table(self):
        """
        Creates a right justified table of values for each shape.
        """
        col = [max(len(str(row[i])) for row in self.shapes) for i in range(len(self.shapes[0]))]
        for row in self.shapes:
            for i in range(len(row)):
                val = str(row[i])
                print(val.rjust(col[i]), end=" ")
            print()