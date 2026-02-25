from .Path import Path, Dot, Vector2
from ...Keys.Keys import up, right, down, left, directions
from ...Keys.Colors import WHITE, GREEN

class Node(Path):
    """Represents a node in the game.

    Attributes:
        directional_nodes (dict): A dictionary to store directional nodes.
        color (Color): The color of the node. Defaults to WHITE.
        type (str): The type of the node. Defaults to "Node".
    """
    def __init__(self):
        """Initializes a new Node object.

        Calls the initializer of the parent class (Path) and sets default attributes.
        """
        super().__init__()
        self.directional_nodes = {}
        self.color = WHITE
        self.type = "Node"
        

    def draw(self, surface):
        """Draws the node on the surface.

        This method calls the draw method of the parent class (Path) to draw the path,
        and then adds specific drawing logic for the node.
        """
        super().draw(surface)