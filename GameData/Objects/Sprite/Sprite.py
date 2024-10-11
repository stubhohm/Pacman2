from ...Dependecies.Dependencies import Rect, Surface

class Sprite():
    def __init__(self):
        self.sprite = Rect()
        self.sprite_sheet = None
        self.sheet_horizontal = 1
        self.sheet_vertical = 1
        self.frame = 1
        self.fps = 10
        self.ticks = 0

    def draw(self, window:Surface):
        self.incriment_sprite()
        self.set_frame()
        

    def incriment_sprite(self):
        self.ticks += 1
        if self.fps < self.ticks:
            return
        self.ticks = 0
        total_frames = self.sheet_horizontal * self.sheet_vertical
        self.frame += 1
        self.frame = self.frame % total_frames

    def set_frame(self):
        pass