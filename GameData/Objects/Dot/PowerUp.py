from .Dot import Dot, point_value, is_power_up

class PowerUp(Dot):
    """Represents a power-up item in the game.

    Inherits properties and methods from the Dot class,
    specifically designed to represent a power-up.
    """
    def __init__(self):
        """
        Initializes a PowerUp object.

        Calls the __init__ method of the parent class (Dot)
        and sets the point value to 100 and the is_powerup
        flag to True.
        """
        super().__init__()
        self.set_point_value(100)
        self.set_is_powerup(True)

    def eat(self):
        """
        Simulates the consumption of the power-up.

        Calls the eat method of the parent class (Dot)
        to handle the consumption logic.
        """
        return super().eat()