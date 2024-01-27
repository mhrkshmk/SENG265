from art_config import ArtConfig
from circle import Circle
from ellipse import Ellipse, EllipseTuple
from html_doc import HtmlDoc
from rectangle import Rectangle, RectangleTuple, RectangleCoordinates
from svg_canvas import SvgCanvas
from color import Color
from coordinates import Coordinates
import random

def main():
    html_doc = HtmlDoc("My Creation for SENG 265", color = "white")
    number_of_shapes = random.randint(19220, 41970)
    art = ArtConfig(Color(r = -1, g = -1, b = -1, op = -1))
    for i in range (number_of_shapes):
        art.gen_shape()
    designs = []
    for shape in art.shapes:
        if shape[1] == 0:
            designs.append(Circle(Coordinates(shape[2], shape[3]), shape[4], Color(shape[9], shape[10], shape[11], shape[12])))
        elif shape[1] == 1:
            designs.append(Ellipse(Coordinates(shape[2], shape[3]), EllipseTuple(shape[5], shape[6]), Color(shape[9], shape[10], shape[11], shape[12])))
        elif shape[1] == 2:
            designs.append(Rectangle(RectangleCoordinates(shape[2], shape[3]), RectangleTuple(shape[7], shape[8]), Color(shape[9], shape[10], shape[11], shape[12])))
    create_art = SvgCanvas(height=1500, width=3000)
    create_art.gen_art(designs)
    html_doc.write_html_footer()


if __name__ == "__main__":
    main()