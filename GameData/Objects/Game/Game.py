from ..GameWindow.GameWindow import GameWindow    
from ...Dependecies.Dependencies import pygame
from ..Map.Map import Map
from ..Text.Text import Text
from ...Keys.Keys import quit_game, select, fruit_dict
from ...Keys.Constants import FPS
from ...Dependecies.Dependencies import make_timer, start_time, sum_time, end_time

class Game():
    """
    The main game class.

    This class manages the game state, including level progression,
    user input, drawing, and interactions with game objects.
    """
    def __init__(self):
        """
        Initializes the Game object.

        Sets the initial level, initializes the clock, game window,
        tiles, and fonts.
        """
        self.level = 1
        self.init_clock()
        self.init_game_window()
        self.init_tiles()
        self.init_fonts()

    def level_up(self):
        """
        Increments the level and updates the tiles.

        This method increases the game level by one and reinitializes
        the tiles with updated parameters.
        """
        self.level += 1
        pacman = self.map.get_player()
        pacman_dict = {"Lives" : pacman.lives,
                       "Score" : pacman.score}
        self.init_tiles(pacman_dict)

    def init_fonts(self):
        """
        Initializes the game fonts.

        This method creates three Text objects with different sizes
        for displaying text in the game.
        """
        self.large_font = Text()
        self.medium_font = Text()
        self.small_font = Text()
        self.large_font.define_font(size=15)
        self.medium_font.define_font(size=12)
        self.small_font.define_font(size=8)
        self.font_instances:list[Text] = []

    def init_clock(self):
        """
        Initializes the game clock.

        This method creates a pygame.time.Clock object with a specified
        framerate (FPS).
        """
        self.clock = pygame.time.Clock()
        self.clock.tick(FPS)
    
    def init_game_window(self):
        """
        Initializes the game window.

        This method creates a GameWindow object to handle the game's
        visual display.
        """
        self.window = GameWindow()

    def init_tiles(self, pacman_dict:dict = {}):
        """
        Initializes the game tiles and map.

        This method creates a Map object with the current level and
        fruit data. It also initializes the player's data.
        """
        self.map = Map(self.level, fruit_dict.get(self.level), pacman_dict)

    def user_input(self):
        """
        Handles user input events.

        This method processes pygame events, detecting key presses
        for quitting the game or selecting an action.
        """
        name = None
        for event in pygame.event.get():
            if event.type == 32787:
                return quit_game
            elif event.type == pygame.KEYDOWN:
                pressed = event.key
                name = pygame.key.name(pressed)
            if name == 'q':
                name = quit_game
            if name == 'return':
                name = select
            return name

    def draw(self):
        """
        Draws the game elements.

        This method calls the draw_map function to render the map
        and updates the display using the game window.
        """
        self.draw_map()
        self.window.update_display()
        self.clock.tick(FPS)

    def draw_map(self):
        """
        Draws the map tiles and the map object.

        This method draws the tiles of the map using the
        GameWindow and also draws the map object itself.
        """
        self.window.draw_tiles(self.map.get_grid())
        self.map.draw(self.window.draw_window)

    def check_interactions(self):
        """
        Checks for interactions between game objects.

        This method checks for collisions between the player and
        ghosts, and triggers a level up if the player eats 250 dots.
        """
        pacman = self.map.get_player()
        for ghost in self.map.get_ghosts().values():
            if pacman.get_position().get_value() != ghost.get_position().get_value():
                continue
            if ghost.get_is_eaten():
                continue
            if ghost.get_is_scared():
                before_score = pacman.score
                pacman.eat_object(ghost.eat_ghost())
                if pacman.score - before_score > 100:
                    print(pacman.score-before_score)
        if self.map.dots_eaten == 250:
            self.level_up()
            
