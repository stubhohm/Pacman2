from ..Ghost import Ghost, Vector2, up, down, left, right, directions
from ....Keys.Constants import ROWS
from ....Keys.Colors import ORANGE
from ....Keys.Keys import clyde as new_name
from ....Sprites.Sprite_Images import Clyde_Array

class Clyde(Ghost):
    """Represents the Clyde ghost in the game.

    Inherits from the Ghost class, defining Clyde's specific attributes
    and behaviors.
    """
    def __init__(self):
        """Initializes the Clyde ghost with its attributes.

        Sets the name, image array, initial position, retreat
        position, and color.
        """
        super().__init__()
        self.set_name(new_name)
        self.ghost_images = Clyde_Array
        self.set_position(Vector2(12,4), True)
        self.set_retreat_position(Vector2(0, ROWS))
        self.color = ORANGE

    def find_best_option(self, target_position, viable_options):
        """Determines the best movement option for Clyde.

        Analyzes the target position and viable options to select
        the optimal movement direction.
        If he is within 8 Tiles of Pacman he turns to his retreat position.
        Otherwise he moves straight towards Pacman.
        """
        # if close to pacman target position is runaway spot
        tgt_x, tgt_y = target_position.get_value()
        p_x, p_y = self.get_position().get_value()
        if Vector2(p_x - tgt_x, p_y - tgt_y).quick_magnitude() < 64:
            target_position = self.get_retreat_position()
        return super().find_best_option(target_position, viable_options)
        