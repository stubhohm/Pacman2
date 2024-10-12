from ...Dependecies.Dependencies import Draw, Rect
from ...Keys.Constants import TILE_HEIGHT,TILE_WIDTH
from ...Keys.Colors import WHITE
from ..Vector2.Vector2 import Vector2, Vector3
origin = Vector2()

class Drawing():
    def __init__(self):
        self.draw = Draw

    def draw_circle(self, surface, radius:int = 1, position:Vector2 = origin, color:Vector3 = WHITE, boarder:int = 0):
        self.draw.circle(surface, color.get_value(), position.get_value(), radius, boarder)
    
    def draw_line(self, surface, start_pos:Vector2 = origin, end_pos:Vector2 = origin, color:Vector3 = WHITE, width:int = 1):
        self.draw.line(surface, color.get_value(), start_pos.get_value(), end_pos.get_value(), width)

    def draw_arc(self, surface, start:float, stop:float, position:Vector2 = origin, color:Vector3 = WHITE, width:int = 1):
        rect = Rect(position.getX(), position.getY(), TILE_WIDTH, TILE_HEIGHT)
        self.draw.arc(surface, color.get_value(), rect, start, stop, width)