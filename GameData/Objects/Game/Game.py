from ..GameWindow.GameWindow import GameWindow    
from ...Dependecies.Dependencies import pygame
from ..Map.Map import Map
from ..Text.Text import Text
from ...Keys.Keys import quit_game, select, fruit_dict
from ...Keys.Constants import FPS
from ...Dependecies.Dependencies import make_timer, start_time, sum_time, end_time

class Game():
    def __init__(self):
        self.level = 1
        self.init_clock()
        self.init_game_window()
        self.init_tiles()
        self.init_fonts()

    def level_up(self):
        self.level += 1
        pacman = self.map.get_player()
        pacman_dict = {"Lives" : pacman.lives,
                       "Score" : pacman.score}
        self.init_tiles(pacman_dict)

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

    def init_tiles(self, pacman_dict:dict = {}):
        self.map = Map(self.level, fruit_dict.get(self.level), pacman_dict)

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

    def draw(self):
        self.draw_map()
        self.window.update_display()
        self.clock.tick(FPS)

    def draw_map(self):
        self.window.draw_tiles(self.map.get_grid())
        self.map.draw(self.window.draw_window)

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
        if self.map.dots_eaten == 250:
            self.level_up()
            
