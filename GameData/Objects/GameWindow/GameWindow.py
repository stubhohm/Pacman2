from ...Keys.Constants import HEIGHT, WIDTH, ROWS, COLUMNS, TILE_WIDTH, TILE_HEIGHT, DEBUG
from ...Dependecies.Dependencies import pygame
from ...Keys.Colors import ColorMixer, MAGENTA, OCEAN, WHITE, CYAN, ORANGE, RASPBERRY, RED, BLACK
from ..Drawing.Drawing import Drawing, Vector2, Vector3
from ..Tile.Tile import Tile

class GameWindow():
    def __init__(self):
        self.height = HEIGHT
        self.width = WIDTH
        self.set_scale(Vector2(self.width, self.height))
        self.create_display()
        self.set_caption("Pacman")
        self.color_mixer = ColorMixer()
        self.draw = Drawing()

    def __is_tuple(self, test_tuple):
        if type(test_tuple) != tuple:
            return False
        return True

    def __is_int(self, test_int):
        if type(test_int) != int:
            return False
        return True

    def set_caption(self, caption:str):
        pygame.display.set_caption(caption)

    def set_background(self, color:Vector3):
        if not self.color_mixer.is_RGB_color(color):
            return
        self.draw_window.fill(color)

    def set_scale(self, scale:Vector2):
        if type(scale) != Vector2:
            return
        self.scale = scale

    def create_display(self):
        self.display = pygame.display
        self.draw_window = self.display.set_mode(self.scale.get_value())

    def draw_circle(self, position:Vector2, radius = 1, color:Vector3 = WHITE, boarder:int = 0 ):
        raw_coordinate = Vector2(TILE_WIDTH * position.getX(), TILE_HEIGHT * position.getY())
        self.draw.draw_circle(self.draw_window, radius, raw_coordinate, color, boarder)

    def draw_tiles(self, tiles:list[list[Tile]]):
        for y_row in tiles:
            for tile in y_row:
                tile.draw(self.draw_window)

    def update_display(self):
        self.display.update()
        self.draw_window.fill(BLACK.get_value())