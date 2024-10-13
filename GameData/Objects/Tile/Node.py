from .Path import Path, Dot, Vector2
from ...Keys.Keys import up, right, down, left, directions

class Node(Path):
    def __init__(self):
        super().__init__()
        self._directional_nodes = {}
        for direction in directions:
            self.set_directional_nodes(direction, None)
        self.type = "Node"
   
    def set_directional_nodes(self, direction:str, node_position:Vector2):
        if direction not in directions:
            print(direction)
            print("Not in directions")
            return
        if node_position:
            if not self.is_coordinate(node_position):
                node_position = None
        self._directional_nodes[direction] = node_position

    def draw(self, surface):
        super().draw(surface)
        x = self.width * self.get_position().getX() + (self.width >> 1)
        y = self.height * self.get_position().getY() + (self.height >> 1)
        coordinate = Vector2(x, y)
        self.drawing.draw_circle(surface, 6, coordinate)