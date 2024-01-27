

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
        self.body = f"<div style=\"position: absolute; color: {self.color}; top: 50%; left: 50%; transform: translate(-50%, -50%);\"><h1>ART CREATED BY MHRKSHMK</h1></div>"
        print(self.header + self.body)
    
    def write_html_footer(self) -> None:
        """
        Writes and prints the HTML footer.
        """
        self.footer = "</body>\n</html>\n"
        print(self.footer)
