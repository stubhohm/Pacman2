from ..Ghost import Ghost, Vector2, up, down, left, right, directions
from ....Keys.Colors import RASPBERRY
from ....Keys.Keys import pinky as new_name
from ....Sprites.Sprite_Images import Pinky_Array

class Pinky(Ghost):
    """Represents the Pinky ghost in the game.

    Inherits from the Ghost class, providing a specific implementation
    for the Pinky ghost's behavior and appearance.
    """
    def __init__(self):
        """Initializes the Pinky ghost object.

        This method calls the initializer of the parent class
        (Ghost) and sets various attributes for the Pinky ghost,
        including its name, images, position, retreat position,
        and color.
        """
        super().__init__()
        self.set_name(new_name)
        self.ghost_images = Pinky_Array
        self.set_position(Vector2(12,4), True)
        self.set_retreat_position(Vector2(0,3))
        self.color = RASPBERRY
    
    def chase_input_function(self, vector_1:Vector2):
        """Moves the ghost based on the given chase input.

        This method takes a Vector2 object as input, representing
        the desired direction for the ghost to chase after.
        It then calls the move_ghost method to actually move the ghost
        in that direction.
        """
        self.move_ghost(vector_1)

    def move_ghost(self, pacman_position):
        """Moves the ghost towards the specified pacman position.

        This method moves the ghost towards the given pacman position,
        utilizing the functionality inherited from the Ghost class.
        """
        super().move_ghost(pacman_position)