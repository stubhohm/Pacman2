from ..Keys.Keys import quit_game, select
from ..Dependecies.Dependencies import pygame
from GameData.Objects.Tile.TileTypes import Tile, Wall, Path, Node
from GameData.Objects.Map.Map import Map
from GameData.Objects.Dot.PowerUp import PowerUp, Dot
from GameData.Objects.Game.Game import Game

def init():
    pygame.init()
    pygame.font.init()
    game = Game()
    return game

     