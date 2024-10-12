from ...Keys.Keys import point_value, is_power_up
from ..Vector2.Vector2 import Vector2

class Dot():
    def __init__(self):
        self._is_eaten:bool = False
        self._is_powerup:bool = False
        self._point_value = 10

    def is_bool(self, new_state:bool):
        if type(new_state) != bool:
            print('Not an bool')
            print(new_state)
            return False
        return True
    
    def is_int(self, new_value:int):
        if type(new_value) != int:
            print('Not an int')
            print(new_value)
            return False
        return True           

    def get_point_value(self):
        return self._point_value

    def set_point_value(self, new_value:int):
        if type(new_value) != int:
            print('Not an int')
            print(new_value)
            return
        self._point_value = new_value

    def get_is_eaten(self):
        return self._is_eaten
    
    def set_is_eaten(self, new_state:bool):
        if not self.is_bool(new_state):
            return
        self._is_eaten = new_state

    def get_is_powerup(self):
        return self._is_powerup

    def set_is_powerup(self, new_state:bool):
        if not self.is_bool(new_state):
            return
        self._is_powerup = new_state

    def eat(self):
        if self._is_eaten:
            return 0
        self.set_is_eaten(True)
        contents = {point_value: self._point_value,
                    is_power_up: self._is_powerup}
        return contents