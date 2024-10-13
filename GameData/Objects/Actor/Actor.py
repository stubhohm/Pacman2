from ..Vector2.Vector2 import Vector2
from ..Sprite.Sprite import Sprite
from ...Keys.Colors import RED
from ...Keys.Constants import DEBUG, FPS
from ...Keys.Keys import up, down, left, right, stop, directions
from ...Keys.Constants import TILE_HEIGHT, TILE_WIDTH, ROWS, COLUMNS, WIDTH
from ..Tile.TileTypes import Tile

direction_to_velocity = {
    up:(0,-1),
    down:(0,1),
    left:(-1, 0),
    right:(1,0),
    stop:(0,0)
}

velocity_to_direction = {
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
        self._target_coordinate:Vector2 = Vector2()
        self._velocity:Vector2 = Vector2()
        self._desired_velocity:Vector2 = Vector2()
        self.sprite:Sprite = Sprite()
        self.actor_type = "Unassigned"
        self._map_grid = None
        self.skipped_frames_per_second = 20
        self.ticks = 0

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
            return False
        return True

    def is_centered(self, check_both = False):   
        if check_both:
            self._desired_velocity = Vector2(1,0)
            left_right = self.is_centered()
            self._desired_velocity = Vector2(0,1)
            up_down = self.is_centered()
            return(up_down and left_right)   
        desired_direction = velocity_to_direction.get(self.get_desired_velocity().get_value())
        if self.get_target_tile(Vector2(0,0)).type != "Node":
            if self.get_velocity().getX() * self.get_desired_velocity().getX() == -1:
                return True
            if self.get_velocity().getY() * self.get_desired_velocity().getY() == -1:
                return True
            return False
        if desired_direction in (stop):
            return False
        pos_x, pos_y = self.get_position().get_value()
        coord_x, coord_y = self.get_coordinate().get_value()
        buffer = 1
        # If desired direction is left right, are we in the middle of a Y tile
        
        if desired_direction in (left, right):
            # Get tile up and tile down coordinates
            y_down = int(self.get_coordinate_from_position(Vector2(pos_x, pos_y + 1)).getY() + (TILE_HEIGHT / 2))
            y_up = int(self.get_coordinate_from_position(Vector2(pos_x, pos_y - 1)).getY() + (TILE_HEIGHT / 2))
            avg = int((y_up + y_down)/2)
            if coord_y - buffer <= avg <= coord_y + buffer:
                return True   
        # if the desired direction is up down, are we centered in an X tile
        elif desired_direction in (up, down):
            # Get tile up and tile down coordinates
            x_right = int(self.get_coordinate_from_position(Vector2(pos_x + 1, pos_y)).getX() + (TILE_WIDTH / 2))
            x_left = int(self.get_coordinate_from_position(Vector2(pos_x - 1, pos_y)).getX() + (TILE_WIDTH / 2))
            avg = int((x_left + x_right)/2)
            if coord_x - buffer <= avg <= coord_x + buffer:
                return True  
        else:
            return False

    def get_direction(self):
        vel = self.get_velocity().get_value()
        return velocity_to_direction.get(vel, None)

    def get_position(self):
        return self._position

    def get_position_from_coordinate(self, coordinate:Vector2):
        """
        Takes an absolute coordinate value and returns the grid position
        """
        p_x, p_y = coordinate.get_value()
        x = int(p_x / TILE_WIDTH)
        y = int(p_y / TILE_HEIGHT)
        return Vector2(x,y)

    def get_coordinate_from_position(self, position:Vector2):
        """
        Takes a grid positionan value and returns an absolute coordinate global value
        """
        c_x, c_y = position.get_value()
        x = int(c_x * TILE_WIDTH)
        y = int(c_y * TILE_HEIGHT)
        return Vector2(x,y)

    def get_coordinate(self):
        return self._coordiate

    def get_sprite_coordinate(self):
        x ,y  = self.get_coordinate().get_value()
        x = (x) - int(self.sprite.get_width() / 2)
        y = (y) - int(self.sprite.get_height() / 2)
        return Vector2(x, y)

    def set_position(self, new_position:Vector2, pull_coordinate:bool = False):
        if not self.is_coordinate(new_position):
            return
        x = new_position.getX()
        y = new_position.getY()
        self._position.set_value(x,y)
        if pull_coordinate:
            x = (x * TILE_WIDTH) + int(TILE_WIDTH / 2)
            y = (y * TILE_HEIGHT) + int(TILE_HEIGHT / 2)
            self._coordiate.set_value(x, y)

    def _validate_velocity(self):
        # new instance vector for vel before validation process
        initial_vel = Vector2(int(self.get_velocity().getX()), int(self.get_velocity().getY()))
        
        # Centering Check for if desired and current vels are different
        if self._velocity.get_value() != self._desired_velocity.get_value():
            if self.is_centered():
                x, y = self._desired_velocity.get_value()
                self._velocity.set_value(x,y)
        
        target_tile = self.get_target_tile(self._velocity)
        if not target_tile:
            print("no tile, stopped")
            x, y = direction_to_velocity[stop]
            self._velocity.set_value(x,y)
            self._desired_velocity.set_value(x,y)
            return
        
        # if the new velocity puts me into a wall revert to inital vel and check if we need to stop
        if self.check_wall_collision(target_tile):
            self._velocity = initial_vel

        target_tile = self.get_target_tile(self._velocity)
        if self.check_wall_collision(target_tile):
            x , y = direction_to_velocity.get(stop)
            self._velocity.set_value(x,y)
            self._desired_velocity.set_value(x,y)
            self.set_position(self.get_position(), True)
            target_tile.line_color = RED
        
    def get_velocity(self):
        return self._velocity
    
    def get_desired_velocity(self):
        return self._desired_velocity

    def set_velocity(self, input_direction:str):
        if input_direction in directions:
            x, y = direction_to_velocity.get(input_direction)
            self._desired_velocity.set_value(x,y)
            if self._map_grid:
                self._validate_velocity()

    def set_map_grid(self, map_grid):
        self._map_grid = map_grid   

    def get_target_tile(self, velocity:Vector2) -> Tile | None:
        if not self._map_grid:
            return None
        x_mod, y_mod = velocity.get_value()
        x, y = self.get_coordinate().get_value()
        x_adj = x + (x_mod * ((TILE_WIDTH / 2)) + 3)
        y_adj = y + (y_mod * ((TILE_HEIGHT / 2)) + 3)
        tile_x, tile_y = self.get_position_from_coordinate(Vector2(x_adj,y_adj)).get_value()
        tile_x = tile_x % COLUMNS
        tile:Tile = self._map_grid[tile_y][tile_x]
        return tile

    def check_wall_collision(self, target_tile:Tile):
        """
        returns true if the next tile is not passable
        """
        if not target_tile:
            return True
        if not target_tile.is_passable():
            return True
        return False
    
    def step_frame(self):
        """
        Returns True if the actor moves this frame, false if it does not.
        """
        skipped_frames_per_second = max(1, self.skipped_frames_per_second)
        self.ticks += 1

        if self.ticks >= FPS:
            self.ticks = 0

        skip_interval = FPS / skipped_frames_per_second
        
        # Check if the current tick should be skipped
        if int(self.ticks % skip_interval) == 0:
            return False  # Skip movement at this interval
        
        return True  # Move the actor otherwise

    def check_teleport(self):
        pos_x = None
        x_position = self.get_coordinate().getX()
        sprite_width = (self.sprite.get_width())
        if x_position - sprite_width > WIDTH:
            pos_x = -1
        if x_position + sprite_width < 0:
            pos_x = COLUMNS
        if type(pos_x) == int:
            pox_y = self.get_position().getY()
            self.set_position(Vector2(pos_x, pox_y), True)

    def move(self):
        if not self.step_frame():
            return
        # Check to make sure current Velocity does not have actor moving into a wall
        self._validate_velocity()
        if self.check_wall_collision(self.get_target_tile(self.get_velocity())):
            return      
        if new_coordinate := self._coordiate.add(self.get_velocity()):
            self._coordiate = new_coordinate
            x = int(new_coordinate.getX() / TILE_WIDTH)
            y = int(new_coordinate.getY() / TILE_HEIGHT)
            self.set_position(Vector2(x,y))
            self.check_teleport()

    def draw_sprite(self, surface):
        self.sprite.draw(surface, self.get_sprite_coordinate())

    def dbprint(self):
        if not DEBUG:
            return
        print(self.get_desired_velocity().get_value())
        print(self.get_velocity().get_value())
        print(self.get_coordinate().get_value())
        print(self.get_position().get_value())