from ..Vector2.Vector2 import Vector2
from ..Sprite.Sprite import Sprite
from ...Keys.Keys import up, down, left, right, stop, directions
from ...Keys.Constants import TILE_HEIGHT, TILE_WIDTH
from ..Tile.TileTypes import Tile

velocity_switch = {
    up:(0,-1),
    down:(0,1),
    left:(-1, 0),
    right:(1,0),
    stop:(0,0)
}

direction_switch = {
    (0,-1):up,
    (0,1): down,
    (-1, 0):left,
    (1,0):right,
    (0,0):stop
}

class Actor():
    def __init__(self):
        self._position:Vector2 = Vector2()
        self._coordiate:Vector2 = Vector2()
        self._velocity:Vector2 = Vector2()
        self.sprite:Sprite = Sprite()
        self.actor_type = "Unassigned"

    def is_coordinate(self, test_coordiante:Vector2):
        if type(test_coordiante) != Vector2:
            print('not a vector')
            print(test_coordiante)
            return False
        return True

    def is_bool(self, test_state):
        if type(test_state) != bool:
            print(test_state)
            print("Not Bool")
            return False
        return True

    def is_string(self, test_string):
        if type(test_string) != str:
            print(test_string)
            print("Not a string")
            return False
        return True

    def get_direction(self):
        vel = self.get_velocity().get_value()
        return direction_switch.get(vel, None)

    def get_position(self):
        return self._position

    def get_coordinate(self):
        return self._coordiate

    def set_position(self, new_position:Vector2, pull_coordinate:bool = False):
        if not self.is_coordinate(new_position):
            return
        x = new_position.getX()
        y = new_position.getY()
        self._position.set_value(x,y)
        if pull_coordinate:
            x = new_position.getX() * TILE_WIDTH
            y = new_position.getY() * TILE_HEIGHT
            self._coordiate.set_value(x, y)

    def get_velocity(self):
        return self._velocity
    
    def set_velocity(self, input_direction:str):
        if not self.is_string(input_direction) or input_direction not in directions:
            print("failed")
            print(self.is_string(input_direction))
            print(input_direction not in directions)
            return
        x, y = velocity_switch.get(input_direction, (None, None))
        print(x,y)
        self._velocity.set_value(x, y)

    def check_wall_collision(self, direction, map_grid):
        """
        returns true if the next tile is not passable
        """
        target_space = None
        x, y = self.get_position().get_value()
        if direction == up:
            target_space = map_grid[y - 1][x]
        elif direction == down:
            target_space = map_grid[y + 1][x]
        elif direction == left:
            target_space = map_grid[y][x - 1]
        elif direction == right:
            target_space = map_grid[y][x + 1]

        if type(target_space) == Tile:
            print("testing")
            if target_space.is_passable():
                print(target_space.is_passable())
                print(self.get_position().get_value())
                return True
        return False
    
    def move(self, map_grid):
        if self.check_wall_collision(self.get_direction(), map_grid):
            return
        new_coordinate = self.get_velocity().add(self._coordiate)
        if type(new_coordinate) != Vector2:
            return
        self._coordiate = new_coordinate
        
        x = int(new_coordinate.getX() / TILE_WIDTH)
        y = int(new_coordinate.getY() / TILE_HEIGHT)
        self.set_position(Vector2(x,y), False)

    def draw_sprite(self, surface):
        self.sprite.draw(surface, self._coordiate)