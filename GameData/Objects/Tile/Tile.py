from ...Keys.Constants import TILE_HEIGHT, TILE_WIDTH
from ..Vector2.Vector2 import Vector2
from ..Drawing.Drawing import Drawing

class Tile():
    def __init__(self):
        self._sprite = None
        self._position:Vector2 = Vector2(0, 0)
        self._passable:bool = True
        self.drawing = Drawing()
        self.height = TILE_HEIGHT
        self.width = TILE_WIDTH
        self.type = "Base Tile"
        self.line_color = None

    def is_coordinate(self, new_coordinate:Vector2):
        if type(new_coordinate) != Vector2:
            print('not a 2d vector: tile')
            print(type(new_coordinate))
            return False
        return True

    def is_string(self, test_string:str):
        if type(test_string) !=str:
            print(test_string)
            print("not a string")
            return False
        return True
    
    def is_bool(self, test_bool:bool):
        if type(test_bool) != bool:
            print(test_bool)
            print("Not Bool")
            return False
        return True

    def is_int(self, test_int:int):
        if type(test_int) != int:
            print(test_int)
            print("Not Int")
            return False
        return True

    def get_position(self):
        return self._position

    def is_passable(self):
        return self._passable
    
    def get_sprite(self):
        return self._sprite

    def set_position(self, new_position:Vector2):
        if not self.is_coordinate(new_position):
            return
        self._position = new_position

    def set_is_passable(self, new_state:bool):
        if not self.is_bool(new_state):
            return
        self._passable = new_state

    def set_sprite(self, sprite):
        self._sprite = sprite

    def draw(self, surface):
        pass