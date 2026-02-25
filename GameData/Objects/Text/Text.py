from ...Keys.Colors import BLACK, WHITE
from ...Dependecies.Dependencies import pygame, os, Surface
from ..Vector2.Vector2 import Vector3, Vector2
from ..Drawing.Drawing import Drawing

font_path = os.path.join("GameData", "Font", "Quinquefive-ALoRM.ttf")

class Text():
    """Represents a text object to be rendered on a surface.

    Attributes:
        font_path (str): Path to the font file.
        position (Vector2): The position of the text on the screen.
        string (str): The text to be rendered.
        size (int): The font size.
        color (Vector3): The color of the text.
        text_surface (Surface): The rendered text surface.
        draw (Drawing): An instance of the Drawing class.
    """
    def __init__(self) -> None:
        """Initializes a new Text object."""
        self.font_path = os.path.join("GameData", "Font", "Quinquefive-ALoRM.ttf")
        self.position:Vector2 = Vector2()
        self.string:str = ""
        self.size:int = 0
        self.color:Vector3 = Vector3()
        self.text_surface = None
        self.draw = Drawing()

    def set_string(self, new_string:str):
        """Sets the text string to be rendered.

        Args:
            new_string (str): The new text string.
        """
        if type(new_string) != str:
            self.string = "Not Valid String"
            return
        self.string = new_string

    def set_position(self, new_position:Vector2):
        """Sets the position of the text.

        Args:
            new_position (Vector2): The new position of the text.
        """
        if type(new_position)!= Vector2:
            return
        self.position = new_position

    def set_color(self, new_color:Vector3):
        """Sets the color of the text.

        Args:
            new_color (Vector3): The new color of the text.
        """
        if type(new_color) != Vector3:
            return
        self.color = new_color

    def define_font(self, text:str = "blank", position:Vector2 = Vector2(), size:int = 12, color:Vector3 = Vector3()):
        """Defines the font for the text.

        Args:
            text (str, optional): The text to render. Defaults to "blank".
            position (Vector2, optional): The position of the text. Defaults to Vector2().
            size (int, optional): The font size. Defaults to 12.
            color (Vector3, optional): The color of the text. Defaults to Vector3().
        """
        self.font = pygame.font.Font(self.font_path, size)
        self.set_string(text)
        self.set_position(position)
        self.set_color(color)
        self.size = size
        self.render_font()

    def draw_font(self, surface):
        """Draws the text on the given surface.

        Args:
            surface (Surface): The surface to draw the text on.
        """
        if self.text_surface:
            position = self.position.get_value()
            surface.blit(self.text_surface, position)

    def render_font(self):
        """Renders the text surface."""
        self.text_surface = self.font.render(self.string, True, self.color.get_value())


