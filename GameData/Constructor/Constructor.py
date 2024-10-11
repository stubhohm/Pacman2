from ..Keys.Keys import quit_game, select
from ..Dependecies.Dependencies import pygame
from GameData.Objects.Tile.TileTypes import Tile, Wall, Path, Node
from GameData.Objects.Map.Map import Map
from GameData.Objects.Dot.PowerUp import PowerUp, Dot

def init():
    pygame.init()
    clock = pygame.time.Clock()
    clock.tick(60)

def user_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return quit_game
        elif event.type == pygame.KEYDOWN:
            pressed = event.key
            name = pygame.key.name(pressed)
        elif event.type == pygame.KEYUP:
            released = event.key
            up_name = pygame.key.name(released)
        if up_name == 'return':
            up_name = select
        return up_name      