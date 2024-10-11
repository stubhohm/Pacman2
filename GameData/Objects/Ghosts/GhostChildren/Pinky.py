from ..Ghost import Ghost
from ....Keys.Keys import pinky as new_name

class Pinky(Ghost):
    def __init__(self):
        super().__init__()
        self.set_name(new_name)