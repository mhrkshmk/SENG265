

class HtmlDoc:
    """
    This class holds ands writes to HTML document the required string values for a HTML header, body, footer.
    """

    def __init__(self, title, color: str):
        """
        Initializes a new instance of HtmlDoc.

        Args:
            title (str): The title of the HTML page.
            color (str): A string for the color value of text written in the middle of the screen.
        """
        self.title = title
        self.color = color
        self.write_html_header()

    def write_html_header(self) -> None:
        """
        Writes and prints the HTML header and the body.
        """
        self.header = f"<html>\n<head>\n<title>{self.title}</title>\n</head>\n<body>\n"
        print(self.header)

    def write_html_footer(self) -> None:
        """
        Writes and prints the HTML footer.
        """
        self.footer = "</body>\n</html>\n"
        print(self.footer)
