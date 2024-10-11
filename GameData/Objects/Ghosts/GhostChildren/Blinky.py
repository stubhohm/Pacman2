from ..Ghost import Ghost
from ....Keys.Keys import blinky as new_name

class Blinky(Ghost):
    def __init__(self):
        super().__init__()
        self.set_name(new_name)