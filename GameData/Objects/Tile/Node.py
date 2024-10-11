from .Path import Path, Dot
from ..Keys.Keys import up, right, down, left, directions

class Node(Path):
    def __init__(self):
        super().__init__()
        self._directional_nodes = {}
        for direction in directions:
            self.set_directional_nodes(direction, None)
   
    def set_directional_nodes(self, direction:str, node_position:tuple[int,int]):
        if direction not in directions:
            print(direction)
            print("Not in directions")
            return
        if not self.is_coordinate(node_position):
            if node_position != None:
                print(node_position)
                print("Not a coordinate")
                return
              
        self._directional_nodes[direction] = node_position