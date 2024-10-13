from ..Tile.TileTypes import Tile, Wall
from ...Keys.Colors import ColorMixer, WHITE, RED
from ...Keys.Constants import DEBUG, ROWS, COLUMNS, HEIGHT, WIDTH, TILE_HEIGHT, TILE_WIDTH
from ...Keys.Keys import ghost_names, blinky, clyde, inky, pinky
from ..Ghosts.GhostList import Blinky, Clyde, Inky, Pinky, Ghost
from ..Pacman.Pacman import Pacman
from ..Vector2.Vector2 import Vector2
from .GridArray import imported_grid_array
from ..Drawing.Drawing import Drawing

class Map():
    def __init__(self):
        self._grid = []
        self.set_grid(imported_grid_array)
        self.__define_ghosts()
        self.__define_pacman()
        self.drawing = Drawing()
        self.color_mixer = ColorMixer()
        
    def __define_ghosts(self):
        self._ghosts:dict[str, Ghost] = {}
        self._ghosts[blinky] = Blinky()
        self._ghosts[clyde] = Clyde()
        self._ghosts[inky] = Inky()
        self._ghosts[pinky] = Pinky()
        for ghost_names in self._ghosts.keys():
            self._ghosts.get(ghost_names).set_map_grid(self.get_grid())

    def __define_pacman(self):
        self._pacman = Pacman()
        self._pacman.set_map_grid(self.get_grid())

    def __validate_grid(self, grid_array:list[list[Tile]]):
        for y, column in enumerate(grid_array):
            if type(column) != list:
                return False
            for x, tile in enumerate(column):
                if not isinstance(tile, Tile):
                    return False
                tile.set_position(Vector2(x,y))
                if type(tile) == Wall:
                    tile.define_wall_draw(grid_array)
        for column in grid_array:
            for tile in column:
                if type(tile) == Wall:
                    tile.define_wall_draw(grid_array, True)
                
        return True

    def set_grid(self, grid_array:list[list[Tile]]):
        if type(grid_array) != list:
            print("Not a list")
            return
        if not self.__validate_grid(grid_array):
            print('Failed Array Check')
            return
        self._grid = grid_array
    
    def get_grid(self):
        return self._grid

    def get_player_position(self):
        return self._pacman.get_position()

    def move_player(self, player_input):
        self._pacman.handle_input(player_input)

    def move_ghosts(self):
        pacman_pos = self._pacman.get_position()
        pacman_vel = self._pacman.get_velocity()
        for ghost_name in self._ghosts.keys():
            ghost = self._ghosts.get(ghost_name)
            if ghost_name == pinky:
                ghost.chase_input_function(pacman_pos, pacman_vel)
            elif ghost_name == inky:
                pacman_space_two_forward = pacman_vel.scale(2)
                blinky_space = self._ghosts[blinky].get_position()
                ghost.chase_input_function(pacman_space_two_forward, blinky_space)
            else:
                ghost.chase_input_function(pacman_pos)

    def draw_grid(self, surface):
        if not DEBUG:
            return
        start_color = WHITE
        end_color = RED
        for i in range(COLUMNS):
            color = self.color_mixer.blend_colors(start_color, end_color, (i/COLUMNS))
            h_pos = (i+1) * TILE_HEIGHT
            start = Vector2(h_pos ,0)
            end = Vector2(h_pos ,HEIGHT)
            self.drawing.draw_line(surface, start, end, color)
        for i in range(ROWS):
            color = self.color_mixer.blend_colors(start_color, end_color, (i/ROWS))
            v_pos = (i+1) * TILE_WIDTH
            start = Vector2(0, v_pos)
            end =  Vector2(WIDTH, v_pos)
            self.drawing.draw_line(surface, start, end, color)

    def draw(self, surface):
        self.draw_grid(surface)
        self._pacman.draw_sprite(surface)
        self.drawing.draw_circle(surface, 2, position=self._pacman.get_coordinate(), color=RED)
        for ghost_name in self._ghosts.keys():
            ghost = self._ghosts[ghost_name] 
            ghost.draw_sprite(surface)