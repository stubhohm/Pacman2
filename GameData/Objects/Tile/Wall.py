from .Tile import Tile

class Wall(Tile):
    def __init__(self):
        super().__init__()
        self.set_is_passable(False)