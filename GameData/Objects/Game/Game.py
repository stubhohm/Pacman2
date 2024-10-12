from ..GameWindow.GameWindow import GameWindow    
from ...Dependecies.Dependencies import pygame
from ..Map.Map import Map
from ..Tile.TileTypes import Wall, Node, Path
from ...Keys.Keys import quit_game, select

class Game():
    def __init__(self):
        self.init_clock()
        self.init_game_window()
        self.init_tiles()

    def init_clock(self):
        self.clock = pygame.time.Clock()
        self.clock.tick(60)
    
    def init_game_window(self):
        self.window = GameWindow()

    def init_tiles(self):
        self.map = Map()

    def user_input(self):
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
        
    def draw_map(self):
        self.map.draw(self.window.draw_window)
        self.window.draw_tiles(self.map.get_grid())