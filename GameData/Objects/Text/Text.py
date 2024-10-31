from ...Keys.Colors import BLACK, WHITE
from ...Dependecies.Dependencies import pygame, os
from ..Vector2.Vector2 import Vector3, Vector2

font_path = os.path.join("GameData", "Font", "Quinquefive-ALoRM.ttf")

class Text():
    def __init__(self) -> None:
        self.font_path = os.path.join("GameData", "Font", "Quinquefive-ALoRM.ttf")
        self.position:Vector2 = Vector2()
        self.string:str = ""
        self.size:int = 0
        self.color:Vector3 = Vector3()

    def set_string(self, new_string:str):
        if type(new_string) != str:
            return
        self.string = new_string

    def set_position(self, new_position:Vector2):
        if type(new_position)!= Vector2:
            return
        self.position = new_position

    def set_color(self, new_color:Vector3):
        if type(new_color) != Vector3:
            return
        self.color = new_color

    def define_font(self, text:str = "", position:Vector2 = Vector2(), size:int = 12, color:Vector3 = Vector3()):
        self.font = pygame.font.Font(self.font_path, size)
        self.set_string(text)
        self.set_position(position)
        self.set_color(color)
        self.size = size

    def render_font(self, surface:pygame.surface.Surface):
        text_surface = self.font.render(self.string, False, self.color.get_value())
        surface.blit(text_surface, self.position.get_value())