from ..Ghost import Ghost, Vector2, up, down, left, right, directions
from ....Keys.Constants import ROWS
from ....Keys.Keys import clyde as new_name
from ....Sprites.Sprite_Images import Clyde_Array

class Clyde(Ghost):
    def __init__(self):
        super().__init__()
        self.set_name(new_name)
        self.ghost_images = Clyde_Array
        self.set_position(Vector2(12,4), True)
        self.set_retreat_position(Vector2(0, ROWS))

    def find_best_option(self, target_position, viable_options):
        # if close to pacman target position is runaway spot
        tgt_x, tgt_y = target_position.get_value()
        p_x, p_y = self.get_position().get_value()
        if Vector2(p_x - tgt_x, p_y - tgt_y).quick_magnitude() < 64:
            target_position = self.get_retreat_position()
        return super().find_best_option(target_position, viable_options)
        