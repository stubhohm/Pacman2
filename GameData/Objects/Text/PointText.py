from ...Dependecies.Dependencies import math, time
from .Text import Text, Vector2, Vector3
from ...Keys.Colors import WHITE
from ...Keys.Constants import CENTER, TILE_HEIGHT



class BonusPointText(Text):
    """Represents a bonus point text element with animated movement.

    This class extends the Text class to provide specialized functionality
    for displaying a bonus point, including time-based fading and
    movement along a curved path.
    """
    def __init__(self) -> None:
        """Initializes the BonusPointText object.

        Sets the initial time for fading, starting point, and tick counter.
        """
        super().__init__()
        self.time = time.time() + 5
        self.starting_point:Vector2 = Vector2()
        self.ticks = 1

    def define_font(self, text: str = "blank", starting_position: Vector2 = CENTER, size: int = 6, color: Vector3 = WHITE):
        """Defines the font properties for the text element.

        Updates the starting position and calls the superclass's
        define_font method to handle font configuration.

        Args:
            text (str, optional): The text to display. Defaults to "blank".
            starting_position (Vector2, optional): The initial position of the text. Defaults to CENTER.
            size (int, optional): The font size. Defaults to 6.
            color (Vector3, optional): The text color. Defaults to WHITE.

        Returns:
            bool: True if the font definition was successful.
        """
        self.starting_point = starting_position.add(Vector2())
        self.set_starting_point(starting_position)
        return super().define_font(text, starting_position, size, color)

    def set_starting_point(self, new_starting_point:Vector2):
        """Sets the starting point for the text element's movement.

        Updates the starting point attribute to the provided value.

        Args:
            new_starting_point (Vector2): The new starting point.
        """
        self.set_position(new_starting_point)

    def move_text(self):
        """Moves the text element based on its defined logic.

        Simulates the animated movement of the bonus point, including fading
        and curved path movement.

        Returns:
            bool: True if the movement was successful, False otherwise.
        """
        if self.time < time.time():
            return False
        self.ticks += 1
        x = self.position.getX()
        if self.ticks % 10 == 0:
            x -= 1
            self.starting_point = self.starting_point.add(Vector2(0,-1))

        delta_x = self.starting_point.differnece(self.position).getX()
        y_offset = TILE_HEIGHT / 4 * math.sin(delta_x * .5)
        y = int(self.starting_point.getY() + y_offset)

        self.position.set_value(x, y)
        return True

