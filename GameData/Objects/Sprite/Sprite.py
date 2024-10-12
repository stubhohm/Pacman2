from ...Dependecies.Dependencies import Rect, Surface
from ..Vector2.Vector2 import Vector2

class Sprite():
    def __init__(self):
        self.sprite:Surface = None
        self.sprite_array = []
        self.frame = 1
        self.fps = 45
        self.ticks = 0

    def draw(self, window:Surface, position:Vector2):
        self.incriment_sprite()
        self.set_frame()
        if not self.sprite and not type(self.sprite) == Surface:
            return
        window.blit(self.sprite, position.get_value())
        
    def incriment_sprite(self):
        self.ticks += 1
        if self.fps > self.ticks:
            return
        self.ticks = 0
        total_frames = len(self.sprite_array) 
        self.frame += 1
        self.frame = self.frame % total_frames

    def set_frame(self):
        self.sprite = self.sprite_array[self.frame]
