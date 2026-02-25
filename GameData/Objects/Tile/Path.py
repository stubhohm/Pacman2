from .Tile import Tile
from ..Dot.PowerUp import Dot, PowerUp
from ..Vector2.Vector2 import Vector2
from ...Keys.Colors import WHITE

class Path(Tile):
    """Represents a path tile in the game.

    Attributes:
        type (str): The type of the tile, which is always "Path".
        _dot (Dot): The dot currently located on this path tile.
        dot_coordinate (Vector2): The coordinates of the dot on this tile.
    """
    def __init__(self):
        """Initializes a new Path instance.

        This constructor calls the initializer of the parent class (Tile)
        and sets the tile's properties.
        """
        super().__init__()
        self.set_is_passable(True)
        self._dot = None
        self.dot_coordinate:Vector2 = Vector2()
        self.type = "Path"
    
    def add_dot(self, new_dot:Dot):
        """Adds a dot to this path tile.

        Args:
            new_dot (Dot): The dot to add to the path tile.
        """
        if not isinstance(new_dot, Dot):
            print("Not a dot: path")
            print(type(new_dot))
            return
        self._dot = new_dot

    def eat_dot(self):
        """Removes a dot from this path tile and returns its data.

        Returns:
            dict: A dictionary containing the data of the eaten dot.
                  Returns None if no dot was present on the tile.
        """
        if not self._dot:
            return None
        dot_dict = self._dot.eat()
        self._dot = None
        return dot_dict

    def get_dot(self):
        """Returns the dot currently located on this path tile.

        Returns:
            Dot: The dot object if one is present, otherwise None.
        """
        return self._dot

    def set_position(self, new_position):
        """Sets the position of this path tile.

        Args:
            new_position (Vector2): The new position to set the tile to.
        """
        super().set_position(new_position)
        dot_x = self.width * self.get_position().getX() + (self.width >> 1)
        dot_y = self.height * self.get_position().getY() + (self.height >> 1)
        self.dot_coordinate.set_value(dot_x, dot_y)

    def draw(self, surface):
        """Draws this path tile and its associated dot on the given surface.

        Args:
            surface (Surface): The surface to draw on.
        """
        dot = self.get_dot()
        if dot:
            radius = (self.height + self.width) >> 4
            if dot.get_is_powerup():
                radius = (radius << 1) + radius
            self.drawing.draw_circle(surface, radius, self.dot_coordinate, WHITE)