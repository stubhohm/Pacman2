from ..Tile.TileTypes import Tile
from ..Keys.Keys import ghost_names, blinky, clyde, inky, pinky
from ..Ghosts.GhostList import Blinky, Clyde, Inky, Pinky

class Map():
    def __init__(self):
        self._grid = []
        self.__define_ghosts()
        self._pacman = None

    def __define_ghosts(self):
        self._ghosts = {}
        self._ghosts[blinky] = Blinky()
        self._ghosts[clyde] = Clyde()
        self._ghosts[inky] = Inky()
        self._ghosts[pinky] = Pinky()

    def __validate_grid(self, grid_array:list[list[Tile]]):
        passed = True
        for y, column in enumerate(grid_array):
            if type(column) != list:
                return False
            for x, tile in enumerate(column):
                if not isinstance(tile, Tile):
                    return False
                tile.set_position((x,y))
        return passed

    def set_grid(self, grid_array:list[list[Tile]]):
        test_tile = Tile()
        if type(grid_array) != list:
            print("Not a list")
            return
        if not self.__validate_grid(grid_array):
            print('Failed Array Check')
            return
