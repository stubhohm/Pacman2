from ..Tile.TileTypes import Tile, Wall, Path
from ...Keys.Colors import ColorMixer, WHITE, RED
from ...Keys.Constants import DEBUG, ROWS, COLUMNS, HEIGHT, WIDTH, TILE_HEIGHT, TILE_WIDTH
from ...Keys.Keys import ghost_names, blinky, clyde, inky, pinky
from ..Ghosts.GhostList import Blinky, Clyde, Inky, Pinky, Ghost
from ..Pacman.Pacman import Pacman
from ..Vector2.Vector2 import Vector2
from .GridArray import make_grid_array
from ..Drawing.Drawing import Drawing
from ..Fruit.Fruit import Fruit
from ...Dependecies.Dependencies import copy

class Map():
    """
    Represents the game map.

    Attributes:
        _grid (list[list[Tile]]): The 2D grid representing the game map.
        dots_eaten (int): The number of dots eaten by Pacman.
        _ghosts (dict[str, Ghost]): A dictionary mapping ghost names to their Ghost objects.
        _pacman (Pacman): The Pacman object.
        drawing (Drawing): The drawing object.
        color_mixer (ColorMixer): The color mixing object.
        fruit_1 (Fruit): The first fruit object.
        fruit_2 (Fruit): The second fruit object.
    """
    def __init__(self, level:int, fruit_dict:dict, pacman_dict = {}):
        """
        Initializes the Map object.

        Args:
            level (int): The current level of the game.
            fruit_dict (dict): A dictionary containing information about the fruits.
            pacman_dict (dict, optional): A dictionary containing information about Pacman. Defaults to {}.
        """
        self._grid = []
        self.dots_eaten = 0
        self.set_grid(make_grid_array())
        self.__define_ghosts()
        self.__define_pacman(pacman_dict)
        self.drawing = Drawing()
        self.color_mixer = ColorMixer()
        self.fruit_1 = Fruit(fruit_dict.get("Fruit 1"), True)
        self.fruit_2 = Fruit(fruit_dict.get("Fruit 2"), False)
        
    def __define_ghosts(self):
        """
        Initializes the ghost objects in the _ghosts dictionary.
        """
        self._ghosts:dict[str, Ghost] = {}
        self._ghosts[blinky] = Blinky()
        self._ghosts[clyde] = Clyde()
        self._ghosts[inky] = Inky()
        self._ghosts[pinky] = Pinky()
        for ghost_names in self._ghosts.keys():
            self._ghosts.get(ghost_names).set_map_grid(self.get_grid())

    def __define_pacman(self, pacman_dict:dict):
        """
        Initializes the Pacman object.

        Args:
            pacman_dict (dict): A dictionary containing information about Pacman.
        """
        self._pacman = Pacman(pacman_dict)
        self._pacman.set_map_grid(self.get_grid())

    def __validate_grid(self, grid_array:list[list[Tile]]):
        """
        Validates the grid array to ensure it meets the required criteria.

        Args:
            grid_array (list[list[Tile]]): The grid array to validate.

        Returns:
            bool: True if the grid array is valid, False otherwise.
        """
        for y, column in enumerate(grid_array):
            if type(column) != list:
                return False
            for x, tile in enumerate(column):
                if not isinstance(tile, Tile):
                    return False
                tile.set_position(Vector2(x,y))
                if type(tile) == Wall:
                    tile.define_wall_draw(grid_array, False)
        for column in grid_array:
            for tile in column:
                if type(tile) == Wall:
                    tile.define_wall_draw(grid_array, True)
                
        return True

    def set_grid(self, grid_array:list[list[Tile]]):
        """
        Sets the grid of the map.

        Args:
            grid_array (list[list[Tile]]): The 2D grid to set.
        """
        if type(grid_array) != list:
            print("Not a list")
            return
        print(copy.__doc__)
        if not self.__validate_grid(grid_array):
            print('Failed Array Check')
            return
        self._grid = grid_array
    
    def get_grid(self):
        """
        Returns the grid of the map.

        Returns:
            list[list[Tile]]: The 2D grid.
        """
        return self._grid

    def get_ghosts(self):
        """
        Returns the ghosts.

        Returns:
            dict[str, Ghost]: The ghosts.
        """
        return self._ghosts

    def get_tile(self, position:Vector2):
        """
        Returns the tile at the given position.

        Args:
            position (Vector2): The position to get the tile from.

        Returns:
            Tile: The tile at the given position.
        """
        x, y = position.get_value()
        if COLUMNS <= x: x = COLUMNS -1
        if x < 0: x = 0
        if y < 0: y = 0
        if ROWS <= y: y = ROWS - 1
        try:
            tile = self.get_grid()[y][x]
        except IndexError:
            print(x)
            print(len(self.get_grid()[0]))
        return tile

    def get_player_position(self):
        """
        Returns the player's position.

        Returns:
            Vector2: The player's position.
        """
        return self._pacman.get_position()

    def get_player(self):
        """
        Returns the player.

        Returns:
            Pacman: The player.
        """
        return self._pacman

    def move_player(self, player_input):
        """
        Moves the player based on the given input.

        Args:
            player_input (str): The player input.
        """
        pacman = self.get_player()
        power_up_start = pacman.power_up
        pacman.handle_input(player_input)
        self.update_fruit()
        tile = self.get_tile(self.get_player_position())
        if not isinstance(tile, Path):
            return 
        if tile.get_dot():
            self.get_player().eat_object(tile.eat_dot())
            self.dots_eaten += 1
            print(self.dots_eaten)
        if power_up_start != pacman.power_up:
            self.set_ghost_fear_state(pacman.power_up)
            
    def set_ghost_fear_state(self, state:bool):
        """
        Sets the fear state of the ghosts.

        Args:
            state (bool): The fear state.
        """
        for ghost in self._ghosts.values():
            ghost.set_is_scared(state)

    def move_ghosts(self):
        """
        Moves the ghosts.
        """
        pacman_pos = self.get_player_position()
        pacman_vel = self.get_player().get_velocity()
        ghosts = self.get_ghosts()
        for ghost_name in ghosts.keys():
            ghost = ghosts.get(ghost_name)
            if ghost_name == pinky:
                ghost.chase_input_function(pacman_pos.add(pacman_vel.scale(4)))
            elif ghost_name == inky:
                pacman_space_two_forward = pacman_pos.add(pacman_vel.scale(2))
                blinky_space = ghosts.get(blinky).get_position()
                ghost.chase_input_function(pacman_space_two_forward, blinky_space)
            else:
                ghost.chase_input_function(pacman_pos)

    def update_fruit(self):
        """
        Updates the visibility of the fruits.
        """
        self.fruit_1.update_visibility(self.dots_eaten, False)
        self.fruit_2.update_visibility(self.dots_eaten, self.fruit_1.is_visible)
        fruit_x, fruit_y = self.fruit_1.get_coordinate().get_value()
        player_x , player_y = self.get_player().get_coordinate().get_value()
        if player_y + 2 > fruit_y > player_y - 2 and (player_x + int(TILE_WIDTH / 2) > fruit_x > player_x - int(TILE_WIDTH / 2)):
            self.get_player().eat_object(self.fruit_1.eat_fruit())
            self.get_player().eat_object(self.fruit_2.eat_fruit())

    def draw_grid(self, surface):
        """
        Draws a grid over the map is debug is enabled.
        """
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
        """
        Draws the map.
        """
        self.draw_grid(surface)
        self.fruit_1.draw_sprite(surface)
        self.fruit_2.draw_sprite(surface)
        self.get_player().draw_sprite(surface)
        for ghost_name in self.get_ghosts().keys():
            ghost = self.get_ghosts().get(ghost_name) 
            ghost.draw_sprite(surface)