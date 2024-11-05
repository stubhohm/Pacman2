from .Path import Path, Dot, Vector2
from ...Keys.Keys import up, right, down, left, directions
from ...Keys.Colors import WHITE, GREEN

class Node(Path):
    def __init__(self):
        super().__init__()
        self.directional_nodes = {}
        self.color = WHITE
        self.type = "Node"
        

    def draw(self, surface):
        super().draw(surface)