from .Tile import Tile, Vector2
from ...Keys.Colors import BLUE
from ...Keys.Keys import horizontal, vertical
from ...Keys.Constants import PI, ROWS, COLUMNS

class Wall(Tile):
    def __init__(self):
        super().__init__()
        self.set_is_passable(False)
        self.draw_function = None
        self.corner_coordinate:Vector2 = Vector2()
        self.orientation = None
        self.type = "Wall"
        self.line_color = BLUE

    def pair_matching(self, tile_1, tile_2):
        if type(tile_1) != type(tile_2): 
            return False
        if type(tile_1) != Wall:
            return False
        return True

    def draw_arc(self, surface):
        self.drawing.draw_arc(surface, self.start, self.end, self.corner_coordinate, self.line_color, 5)

    def draw_line(self, surface):
        self.drawing.draw_line(surface, self.start, self.end, self.line_color, 5)

    def draw(self, surface):
        if self.draw_function:
            self.draw_function(surface)

    def set_position(self, new_position):
        super().set_position(new_position)
        corner_x = self.width * self.get_position().getX()
        corner_y = self.height * self.get_position().getY()
        self.corner_coordinate.set_value(corner_x, corner_y)

    def get_corner(self):
        corner_x = self.width * self.get_position().getX()
        corner_y = self.height * self.get_position().getY()
        self.corner_coordinate.set_value(corner_x, corner_y)

    def select_line_draw_function(self, up_tile, left_tile, right_tile, down_tile):
        self.get_corner()
        position = self.corner_coordinate
        pos_x = position.getX()
        pos_y = position.getY()
        mid_y = pos_y + int(self.height / 2)
        mid_x = pos_x + int(self.width / 2)
        bottom_x = pos_x + self.width
        bottom_y = pos_y + self.height
        # Fully enclosed
        type_list = [type(up_tile), type(left_tile), type(right_tile), type(down_tile)]
        wall_or_tile = (Wall or Tile)
        if type_list.count(wall_or_tile) == 4:
            return
        
        # Lines
            # Horizontal
        if self.pair_matching(left_tile, right_tile):
            self.start = Vector2(pos_x, mid_y)
            self.end = Vector2(bottom_x, mid_y)
            self.draw_function = self.draw_line
            self.orientation = horizontal
            return
            # Vertical
        elif self.pair_matching(up_tile, down_tile):
            self.start = Vector2(mid_x, pos_y)
            self.end = Vector2(mid_x, bottom_y)
            self.draw_function = self.draw_line
            self.orientation = vertical
            return

    def define_arc(self, start:float, stop:float, width_scale = 1, height_scale = 1, width_shift = 2, height_shift = 2):
        self.get_corner()
        position = self.corner_coordinate
        pos_x = position.getX()
        pos_y = position.getY()
        self.start = start * PI
        self.end = stop * PI
        new_x = pos_x + (int(self.width / 2) * width_scale) + width_shift
        new_y = pos_y + (int(self.height / 2) * height_scale) + height_shift
        self.draw_function = self.draw_arc
        self.corner_coordinate.set_value(new_x, new_y)

    def select_arc_draw_function(self, up_tile, left_tile, right_tile, down_tile):
        # Mostly enclosed
        type_list = [type(up_tile), type(left_tile), type(right_tile), type(down_tile)]
        wall_or_tile = (Wall or Tile)
        if type_list.count(wall_or_tile) == 4:
            if type(left_tile) == Wall and left_tile.orientation == horizontal:
                    if type(down_tile) == Wall and down_tile.orientation == vertical:
                        self.define_arc(1.95, 0.55, -1, 1, 0, 0)
                        return
                    if type(up_tile) == Wall and up_tile.orientation == vertical:
                        self.define_arc(1.45, 2.05, -1, -1, 0, 0)
                        return
            if type(right_tile) == Wall and right_tile.orientation == horizontal:
                if type(down_tile) == Wall and down_tile.orientation == vertical:
                    self.define_arc(0.45, 1.05, 1, 1, 0, 0)
                    return
                if type(up_tile) == Wall and up_tile.orientation == vertical:
                    self.define_arc(0.95, 1.55, 1, -1, 0, 0)
                    return
            return
        
        # Curves
            # Upper Left
        if self.pair_matching(up_tile, left_tile):
            self.define_arc(1.45, 2.05, -1, -1, 0, 0)

            # Upper Right
        elif self.pair_matching(up_tile, right_tile):
            self.define_arc(0.95, 1.55, 1, -1, 0, 0)

            # Lower Left
        elif self.pair_matching(down_tile, left_tile):
            self.define_arc(1.95, 0.55, -1, 1, 0, 0)

            # Lower Right
        elif self.pair_matching(down_tile, right_tile):
            self.define_arc(0.45, 1.05, 1, 1, 0, 0)
        
    def define_wall_draw(self, grid_array, arcs = False):
        if self.draw_function:
            return
        x = self.get_position().getX()
        y = self.get_position().getY()
        if y == 3:
            up = Wall()
        else:
            up = grid_array[y - 1][x]

        if y == 33:
            down = Wall()
        else:
            down = grid_array[y + 1][x]
        
        if x == 0:
            left = Wall()
        else:
            left = grid_array[y][x - 1]
        
        if x == COLUMNS or x == len(grid_array[0]) - 1:
            right = Wall()
        else:
            right = grid_array[y][x + 1]
        if arcs:
            self.select_arc_draw_function(up, left, right, down)
        else:
            self.select_line_draw_function(up, left, right, down)