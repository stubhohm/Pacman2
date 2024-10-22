from ..Ghost import Ghost, Vector2, up, down, left, right, directions
from ....Keys.Keys import blinky as new_name
from ....Keys.Colors import RED
from ....Keys.Constants import COLUMNS
from ....Sprites.Sprite_Images import Blinky_Array

class Blinky(Ghost):
    def __init__(self):
        super().__init__()
        self.set_name(new_name)
        self.ghost_images = Blinky_Array
        self.set_position(Vector2(12,4), True)
        self.set_retreat_position(Vector2(0,COLUMNS - 3))
        self.color = RED