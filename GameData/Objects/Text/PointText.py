from ...Dependecies.Dependencies import math, time
from .Text import Text, Vector2, Vector3

class BonusPointText(Text):
    def __init__(self) -> None:
        super().__init__()
        self.time = time.time() + 5
        self.starting_point:Vector2 = Vector2()

    def define_font(self, text: str = "", starting_position: Vector2 = ..., size: int = 12, color: Vector3 = ...):
        starting_pos = Vector2(starting_position.getX(), starting_position.getY())
        self.set_starting_point(starting_pos)
        return super().define_font(text, starting_pos, size, color)

    def set_starting_point(self, new_starting_point:Vector2):
        self.set_position(new_starting_point)

    def move_text(self):
        if self.time < time.time():
            self = None
            return
        x = self.position.getX() - 1
        delta = self.position.differnece(self.starting_point)
        print()
        print("Delta")
        print(delta.get_value())
        delta_x = delta.getX()
        print("Delta x")
        print(delta_x)
        print("starting pos")
        print(self.starting_point.get_value())
        y_offset = math.sin(delta_x) #+ 2 / math.sqrt(delta_x)
        y = self.position.getY() + y_offset
        self.position.set_value(x, y)
        print("Y offset")
        print(y_offset)
        print("current pos")
        print(self.position.get_value())

