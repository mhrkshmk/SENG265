from circle import Circle
from svg_canvas import SvgCanvas
from html_doc import HtmlDoc
from coordinates import Coordinates
from color import Color

def main() -> None:
    html_doc = HtmlDoc("My Art", "part1.html")
    svg_art = SvgCanvas(1000, 3000)
    shapes = [
        Circle(Coordinates(50, 50), 50, Color(255, 0, 0, 1.0)),
        Circle(Coordinates(150, 50), 50, Color(255, 0, 0, 1.0)),
        Circle(Coordinates(250, 50), 50, Color(255, 0, 0, 1.0)),
        Circle(Coordinates(350, 50), 50, Color(255, 0, 0, 1.0)),
        Circle(Coordinates(450, 50), 50, Color(255, 0, 0, 1.0)),
        Circle(Coordinates(50, 250), 50, Color(0, 0, 255, 1.0)),
        Circle(Coordinates(150, 250), 50, Color(0, 0, 255, 1.0)),
        Circle(Coordinates(250, 250), 50, Color(0, 0, 255, 1.0)),
        Circle(Coordinates(350, 250), 50, Color(0, 0, 255, 1.0)),
        Circle(Coordinates(450, 250), 50, Color(0, 0, 255, 1.0))
    ]
    svg_art.gen_art(shapes)
    html_doc.write_html_footer()

if __name__ == "__main__":
    main()