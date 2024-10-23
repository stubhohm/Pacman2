from ..Ghost import Ghost, Vector2, up, down, left, right, directions
from ....Keys.Constants import ROWS, COLUMNS
from ....Keys.Keys import inky as new_name
from ....Sprites.Sprite_Images import Inky_Array

class Inky(Ghost):
    def __init__(self):
        super().__init__()
        self.set_name(new_name)
        self.ghost_images = Inky_Array
        self.set_position(Vector2(21,4), True)
        self.set_retreat_position(Vector2(ROWS, COLUMNS))
    
    def chase_input_function(self, vector_1:Vector2, vector_2:Vector2):
        # Get vector from blinky to pacman and double its length
        diff_vec = vector_1.differnece(vector_2).scale(2)
        target_position = vector_1.add(diff_vec)
        print(vector_1.get_value())
        print(diff_vec.get_value())
        print(target_position.get_value())

        self.move_ghost(target_position)

    def move_ghost(self, pacman_position):
        super().move_ghost(pacman_position)