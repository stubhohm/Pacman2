from ...Dependecies.Dependencies import Rect, Surface
from ..Vector2.Vector2 import Vector2
from ...Keys.Constants import TILE_HEIGHT, TILE_WIDTH
from ...Keys.Keys import up, down, left, right
directions = [up, down, left, right]

class Sprite():
    def __init__(self):
        self.sprite:Surface = None
        self.sprite_array = []
        self.frame = 1
        self.fps = 45
        self.ticks = 0

    def get_height(self):
        if not self.sprite:
            return TILE_HEIGHT
        return self.sprite.get_height()

    def get_width(self):
        if not self.sprite:
            return TILE_WIDTH
        return self.sprite.get_width()

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
        if total_frames == 0:
            self.frame = 0
            return
        self.frame = self.frame % total_frames

    def set_frame(self):
        if not self.sprite_array:
            self.sprite = None
            return
        self.sprite = self.sprite_array[self.frame]

class EyeSprite(Sprite):
    def __init__(self):
        super().__init__()
        self.last_direction = None

    def set_frame(self):
        if self.last_direction not in directions:
            self.last_direction = down
        if not self.sprite_array:
            self.sprite = None
            return
        self.sprite = self.sprite_array[self.last_direction]

    def incriment_sprite(self):
        pass