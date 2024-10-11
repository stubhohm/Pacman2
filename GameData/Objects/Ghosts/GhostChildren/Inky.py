from ..Ghost import Ghost
from ....Keys.Keys import inky as new_name

class Inky(Ghost):
    def __init__(self):
        super().__init__()
        self.set_name(new_name)