from ..Ghost import Ghost, Vector2, up, down, left, right, directions
from ....Keys.Constants import ROWS, COLUMNS
from ....Keys.Keys import inky as new_name
from ....Sprites.Sprite_Images import Inky_Array

class Inky(Ghost):
    """Represents the Inky ghost in the game.

    Inherits from the Ghost class, providing specific behavior and
    attributes for the Inky character.
    """
    def __init__(self):
        """
        Initializes the Inky ghost with specific attributes.

        Sets the ghost's name, image array, initial position, and
        retreat position.
        """
        super().__init__()
        self.set_name(new_name)
        self.ghost_images = Inky_Array
        self.set_position(Vector2(21,4), True)
        self.set_retreat_position(Vector2(ROWS, COLUMNS))
    
    def chase_input_function(self, vector_1:Vector2, vector_2:Vector2):
        """
        Implements the chase behavior for the Inky ghost, targeting
        the pacman based on the provided vectors.

        Calculates the vector from blinky to pacman and doubles its
        length to determine the target position for the Inky ghost.
        """
        # Get vector from blinky to pacman and double its length
        diff_vec = vector_1.differnece(vector_2).scale(2)
        target_position = vector_1.add(diff_vec)
        self.move_ghost(target_position)

    def move_ghost(self, pacman_position):
        """
        Moves the ghost towards the given pacman position.

        This method calls the superclass's move_ghost method to handle
        the actual movement logic.
        """
        super().move_ghost(pacman_position)