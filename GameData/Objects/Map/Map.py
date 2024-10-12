from ..Tile.TileTypes import Tile, Wall
from ...Keys.Keys import ghost_names, blinky, clyde, inky, pinky
from ..Ghosts.GhostList import Blinky, Clyde, Inky, Pinky
from ..Pacman.Pacman import Pacman
from ..Vector2.Vector2 import Vector2
from .GridArray import imported_grid_array

class Map():
    def __init__(self):
        self._grid = []
        self.__define_ghosts()
        self._pacman = Pacman()
        self.set_grid(imported_grid_array)

    def __define_ghosts(self):
        self._ghosts = {}
        self._ghosts[blinky] = Blinky()
        self._ghosts[clyde] = Clyde()
        self._ghosts[inky] = Inky()
        self._ghosts[pinky] = Pinky()

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
    
    def move_player(self, player_input):
        self._pacman.handle_input(player_input, self.get_grid())

    def draw(self, surface):
        self._pacman.draw_sprite(surface)
        for ghost_name in self._ghosts.keys():
            continue
            ghost:Blinky = self._ghosts[ghost_name] 
            ghost.draw_sprite(surface)