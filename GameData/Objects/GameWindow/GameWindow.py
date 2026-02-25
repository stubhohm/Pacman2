from ...Keys.Constants import HEIGHT, WIDTH, ROWS, COLUMNS, TILE_WIDTH, TILE_HEIGHT, DEBUG
from ...Dependecies.Dependencies import pygame
from ...Keys.Colors import ColorMixer, MAGENTA, OCEAN, WHITE, CYAN, ORANGE, RASPBERRY, RED, BLACK
from ..Drawing.Drawing import Drawing, Vector2, Vector3
from ..Tile.Tile import Tile
from ...Dependecies.Dependencies import make_timer, start_time, sum_time, end_time



class GameWindow():
    """Represents the main window of the Pacman game.

    This class handles the window creation, display setup, and drawing 
    operations for the game.
    """
    def __init__(self):
        """Initializes the GameWindow with its dimensions and settings."""
        self.height = HEIGHT
        self.width = WIDTH
        self.set_scale(Vector2(self.width, self.height))
        self.create_display()
        self.set_caption("Pacman")
        self.color_mixer = ColorMixer()
        self.draw = Drawing()

    def __is_tuple(self, test_tuple):
        """Checks if the given input is a tuple.

        Args:
            test_tuple (object): The input to check.

        Returns:
            bool: True if the input is a tuple, False otherwise.
        """
        if type(test_tuple) != tuple:
            return False
        return True

    def __is_int(self, test_int):
        """Checks if the given input is an integer.

        Args:
            test_int (object): The input to check.

        Returns:
            bool: True if the input is an integer, False otherwise.
        """
        if type(test_int) != int:
            return False
        return True

    def set_caption(self, caption:str):
        """Sets the title of the game window.

        Args:
            caption (str): The desired title for the window.
        """
        pygame.display.set_caption(caption)

    def set_background(self, color:Vector3):
        """Sets the background color of the game window.

        Args:
            color (Vector3): The RGB color to set as the background.
        """
        if not self.color_mixer.is_RGB_color(color):
            return
        self.draw_window.fill(color)

    def set_scale(self, scale:Vector2):
        """Sets the scaling factor for the game window.

        Args:
            scale (Vector2): The scaling factor as a Vector2 object.
        """
        if type(scale) != Vector2:
            return
        self.scale = scale

    def create_display(self):
        """Creates the Pygame display window.

        Sets up the Pygame display surface with the specified dimensions.
        """
        self.display = pygame.display
        self.draw_window = self.display.set_mode(self.scale.get_value())

    def draw_circle(self, position:Vector2, radius = 1, color:Vector3 = WHITE, boarder:int = 0 ):
        """Draws a circle on the game window.

        Args:
            position (Vector2): The center coordinates of the circle.
            radius (int, optional): The radius of the circle. Defaults to 1.
            color (Vector3, optional): The color of the circle. Defaults to WHITE.
            boarder (int, optional): The width of the circle border. Defaults to 0.
        """
        raw_coordinate = Vector2(TILE_WIDTH * position.getX(), TILE_HEIGHT * position.getY())
        self.draw.draw_circle(self.draw_window, radius, raw_coordinate, color, boarder)

    def draw_tiles(self, tiles:list[list[Tile]]):
        """Draws a list of tiles on the game window.

        Args:
            tiles (list[list[Tile]]): A 2D list of Tile objects to draw.
        """
        for y_row in tiles:
            for tile in y_row:
                tile.draw(self.draw_window)


    def update_display(self):
        """Updates the Pygame display, handling events and drawing.

        This method ensures that the game window is updated with the latest 
        drawings and events.
        """
        self.display.update()
        self.draw_window.fill(BLACK.get_value())