from ...Keys.Constants import TILE_HEIGHT, TILE_WIDTH
from ..Vector2.Vector2 import Vector2
from ..Drawing.Drawing import Drawing

class Tile():
    """Represents a tile in a game.

    Attributes:
        _sprite (None): The sprite associated with the tile.
        _position (Vector2): The tile's position in the game world.
        _passable (True): A boolean indicating whether the tile is passable.
        drawing (Drawing): An object for drawing the tile.
        height (int): The height of the tile.
        width (int): The width of the tile.
        type (str): The type of the tile.
        line_color (None): The color of the tile's outline.
        limited (bool): A boolean indicating if the tile is limited.
    """
    def __init__(self):
        """Initializes a new Tile object."""
        self._sprite = None
        self._position:Vector2 = Vector2(0, 0)
        self._passable:bool = True
        self.drawing = Drawing()
        self.height = TILE_HEIGHT
        self.width = TILE_WIDTH
        self.type = "Base Tile"
        self.line_color = None
        self.limited = False

    def is_coordinate(self, new_coordinate:Vector2):
        """Checks if the provided object is a valid 2D vector.

        Args:
            new_coordinate (Vector2): The object to check.

        Returns:
            bool: True if the object is a Vector2, False otherwise.
        """
        if type(new_coordinate) != Vector2:
            print('not a 2d vector: tile')
            print(type(new_coordinate))
            return False
        return True

    def is_string(self, test_string:str):
        """Checks if the provided object is a valid string.

        Args:
            test_string (str): The object to check.

        Returns:
            bool: True if the object is a string, False otherwise.
        """
        if type(test_string) !=str:
            print(test_string)
            print("not a string")
            return False
        return True
    
    def is_bool(self, test_bool:bool):
        """Checks if the provided object is a valid boolean.

        Args:
            test_bool (bool): The object to check.

        Returns:
            bool: True if the object is a boolean, False otherwise.
        """
        if type(test_bool) != bool:
            print(test_bool)
            print("Not Bool")
            return False
        return True

    def is_int(self, test_int:int):
        """Checks if the provided object is a valid integer.

        Args:
            test_int (int): The object to check.

        Returns:
            bool: True if the object is an integer, False otherwise.
        """
        if type(test_int) != int:
            print(test_int)
            print("Not Int")
            return False
        return True

    def get_position(self):
        """Returns the tile's position.

        Returns:
            Vector2: The tile's position.
        """
        return self._position

    def is_passable(self):
        """Returns whether the tile is passable.

        Returns:
            bool: True if the tile is passable, False otherwise.
        """
        return self._passable
    
    def get_sprite(self):
        """Returns the sprite associated with the tile.

        Returns:
            None: The sprite associated with the tile.
        """
        return self._sprite

    def set_position(self, new_position:Vector2):
        """Sets the tile's position.

        Args:
            new_position (Vector2): The new position for the tile.
        """
        if not self.is_coordinate(new_position):
            return
        self._position = new_position

    def set_is_passable(self, new_state:bool):
        """Sets whether the tile is passable.

        Args:
            new_state (bool): The new state of the tile's passability.
        """
        if not self.is_bool(new_state):
            return
        self._passable = new_state

    def set_sprite(self, sprite):
        """Sets the sprite associated with the tile.

        Args:
            sprite: The sprite to associate with the tile.
        """
        self._sprite = sprite

    def draw(self, surface):
        """Draws the tile on the given surface. Base class passes,

        Args:
            surface (Surface): The surface to draw on.
        """
        pass