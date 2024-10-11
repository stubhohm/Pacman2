from .Dot import Dot, point_value, is_power_up

class PowerUp(Dot):
    def __init__(self):
        super().__init__()
        self.set_point_value(100)
        self.set_is_powerup(True)

    def eat(self):
        return super().eat()