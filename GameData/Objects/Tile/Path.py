from .Tile import Tile
from ..Dot.Dot import Dot

class Path(Tile):
    def __init__(self):
        super().__init__()
        self.set_is_passable(True)
        self._dot = None
    
    def add_dot(self, new_dot:Dot):
        if not isinstance(new_dot, Dot):
            print("Not a dot")
            return
        self._dot = new_dot
        