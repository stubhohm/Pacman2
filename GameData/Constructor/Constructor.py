from GameData.Keys.Keys import quit_game, select
from GameData.Dependecies.Dependencies import pygame
from GameData.Objects.Tile.TileTypes import Tile, Wall, Path, Node
from GameData.Objects.Map.Map import Map
from GameData.Objects.Dot.PowerUp import PowerUp, Dot
from GameData.Objects.Game.Game import Game

def init():
    """Initializes the game environment.

    This function initializes the pygame library, font, and creates an instance of the Game class.
    It then returns the initialized game object.
    """
    pygame.init()
    pygame.font.init()
    game = Game()
    return game

     