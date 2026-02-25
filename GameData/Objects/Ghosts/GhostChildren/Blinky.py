from ..Ghost import Ghost, Vector2, up, down, left, right, directions
from ....Keys.Keys import blinky as new_name
from ....Keys.Colors import RED
from ....Keys.Constants import COLUMNS
from ....Sprites.Sprite_Images import Blinky_Array

class Blinky(Ghost):
    """Represents a ghost in the game.

    Inherits from the Ghost class, providing a specific implementation
    for this particular ghost.
    """
    def __init__(self):
        """
        Initializes the Blinky ghost with its properties.

        This constructor calls the parent class's constructor and
        sets up the ghost's name, images, starting position,
        retreat position, and color.
        """
        super().__init__()
        self.set_name(new_name)
        self.ghost_images = Blinky_Array
        self.set_position(Vector2(12,4), True)
        self.set_retreat_position(Vector2(0,COLUMNS - 3))
        self.color = RED

    def find_best_option(self, target_position, viable_options):
        """
        Blinky Moves Straight Towards Pacman. This is unchanged from the Ghost Class Method.
        """
        return super().find_best_option(target_position, viable_options)