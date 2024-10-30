from .Tile import Tile
from ..Dot.PowerUp import Dot, PowerUp
from ..Vector2.Vector2 import Vector2
from ...Keys.Colors import WHITE

class Path(Tile):
    def __init__(self):
        super().__init__()
        self.set_is_passable(True)
        self._dot = None
        self.dot_coordinate:Vector2 = Vector2()
        self.type = "Path"
    
    def add_dot(self, new_dot:Dot):
        if not isinstance(new_dot, Dot):
            print("Not a dot: path")
            print(type(new_dot))
            return
        self._dot = new_dot

    def get_dot(self):
        return self._dot

    def set_position(self, new_position):
        super().set_position(new_position)
        dot_x = self.width * self.get_position().getX() + (self.width >> 1)
        dot_y = self.height * self.get_position().getY() + (self.height >> 1)
        self.dot_coordinate.set_value(dot_x, dot_y)

    def draw(self, surface):
        dot = self.get_dot()
        if dot:
            radius = (self.height + self.width) >> 4
            if dot.get_is_powerup():
                radius = (radius << 1) + radius
            self.drawing.draw_circle(surface, radius, self.dot_coordinate, WHITE)