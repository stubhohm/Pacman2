from ...Dependecies.Dependencies import math, time
from .Text import Text, Vector2, Vector3
from ...Keys.Colors import WHITE
from ...Keys.Constants import CENTER, TILE_HEIGHT



class BonusPointText(Text):
    def __init__(self) -> None:
        super().__init__()
        self.time = time.time() + 5
        self.starting_point:Vector2 = Vector2()
        self.ticks = 1

    def define_font(self, text: str = "blank", starting_position: Vector2 = CENTER, size: int = 6, color: Vector3 = WHITE):
        self.starting_point = starting_position.add(Vector2())
        self.set_starting_point(starting_position)
        return super().define_font(text, starting_position, size, color)

    def set_starting_point(self, new_starting_point:Vector2):
        self.set_position(new_starting_point)

    def move_text(self):
        if self.time < time.time():
            return False
        self.ticks += 1
        x = self.position.getX()
        if self.ticks % 10 == 0:
            print(self.ticks)
            x -= 1
            self.starting_point = self.starting_point.add(Vector2(0,-1))

        delta_x = self.starting_point.differnece(self.position).getX()
        y_offset = TILE_HEIGHT / 4 * math.sin(delta_x * .5)
        y = int(self.starting_point.getY() + y_offset)

        self.position.set_value(x, y)
        return True

