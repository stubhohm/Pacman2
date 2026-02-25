from ...Dependecies.Dependencies import Draw, Rect
from ...Keys.Constants import TILE_HEIGHT,TILE_WIDTH
from ...Keys.Colors import WHITE
from ..Vector2.Vector2 import Vector2, Vector3
origin = Vector2()

class Drawing():
    """
    A class for handling drawing operations on a surface.

    This class provides methods to draw various shapes such as circles, lines, and arcs.
    It utilizes a Draw object to perform the actual drawing operations.
    """
    def __init__(self):
        """
        Initializes the Drawing object.

        This constructor initializes the self.draw attribute to the Draw object.
        """
        self.draw = Draw

    def draw_circle(self, surface, radius:int = 1, position:Vector2 = origin, color:Vector3 = WHITE, boarder:int = 0):
        """
        Draws a circle on the given surface.

        Args:
            surface: The surface on which to draw the circle.
            radius (int, optional): The radius of the circle. Defaults to 1.
            position (Vector2, optional): The position of the circle's center. Defaults to origin.
            color (Vector3, optional): The color of the circle. Defaults to WHITE.
            boarder (int, optional): The width of the circle's border. Defaults to 0.
        """
        self.draw.circle(surface, color.get_value(), position.get_value(), radius, boarder)
    
    def draw_line(self, surface, start_pos:Vector2 = origin, end_pos:Vector2 = origin, color:Vector3 = WHITE, width:int = 1):
        """
        Draws a line on the given surface.

        Args:
            surface: The surface on which to draw the line.
            start_pos (Vector2, optional): The starting position of the line. Defaults to origin.
            end_pos (Vector2, optional): The ending position of the line. Defaults to origin.
            color (Vector3, optional): The color of the line. Defaults to WHITE.
            width (int, optional): The width of the line. Defaults to 1.
        """
        self.draw.line(surface, color.get_value(), start_pos.get_value(), end_pos.get_value(), width)

    def draw_arc(self, surface, start:float, stop:float, position:Vector2 = origin, color:Vector3 = WHITE, width:int = 1):
        """
        Draws an arc on the given surface within a rectangular region.

        Args:
            surface: The surface on which to draw the arc.
            start (float, optional): The starting angle of the arc in degrees. Defaults to 0.
            stop (float, optional): The stopping angle of the arc in degrees. Defaults to 0.
            position (Vector2, optional): The position of the rectangle's top-left corner. Defaults to origin.
            color (Vector3, optional): The color of the arc. Defaults to WHITE.
            width (int, optional): The width of the arc. Defaults to 1.
        """
        rect = Rect(position.getX(), position.getY(), TILE_WIDTH, TILE_HEIGHT)
        self.draw.arc(surface, color.get_value(), rect, start, stop, width)