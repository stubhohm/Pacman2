from ..Ghost import Ghost, Vector2, up, down, left, right, directions
from ....Keys.Keys import pinky as new_name
from ....Sprites.Sprite_Images import Pinky_Array

class Pinky(Ghost):
    def __init__(self):
        super().__init__()
        self.set_name(new_name)
        self.ghost_images = Pinky_Array
        self.set_position(Vector2(12,4), True)
        self.set_retreat_position(Vector2(0,3))
    
    def chase_input_function(self, vector_1:Vector2, vector_2:Vector2):
        vector_2 = vector_2.scale(4)
        target_position = vector_1.add(vector_2)
        self.move_ghost(target_position)

    def move_ghost(self, pacman_position):
        super().move_ghost(pacman_position)