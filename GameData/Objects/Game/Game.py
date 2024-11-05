from ..GameWindow.GameWindow import GameWindow    
from ...Dependecies.Dependencies import pygame
from ..Map.Map import Map
from ..Text.Text import Text
from ..Tile.TileTypes import Wall, Node, Path
from ...Keys.Keys import quit_game, select
from ...Keys.Constants import FPS
from ...Dependecies.Dependencies import make_timer, start_time, sum_time, end_time

class Game():
    def __init__(self):
        self.init_clock()
        self.init_game_window()
        self.init_tiles()
        self.init_fonts()
        self.tile_timer = make_timer("Tile Timer")
        self.loop_count = 0

    def init_fonts(self):
        self.large_font = Text()
        self.medium_font = Text()
        self.small_font = Text()
        self.large_font.define_font(size=15)
        self.medium_font.define_font(size=12)
        self.small_font.define_font(size=8)
        self.font_instances:list[Text] = []

    def init_clock(self):
        self.clock = pygame.time.Clock()
        self.clock.tick(FPS)
    
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
        self.loop_count += 1
        self.tile_timer = start_time(self.tile_timer)
        self.window.draw_tiles(self.map.get_grid())
        self.tile_timer = sum_time(self.tile_timer)
        self.map.draw(self.window.draw_window)
        if self.loop_count % 240 == 0:
            self.loop_count = 1
            print()
            self.tile_timer = end_time(self.tile_timer)

    def check_interactions(self):
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
            
