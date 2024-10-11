from ..Ghost import Ghost
from ...Keys.Keys import clyde as new_name

class Clyde(Ghost):
    def __init__(self):
        super().__init__()
        self.set_name(new_name)