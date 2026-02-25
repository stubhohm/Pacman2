from ...Keys.Keys import point_value, is_power_up
from ..Vector2.Vector2 import Vector2

class Dot():
    """Represents a dot in a game.

    Attributes:
        _is_eaten (bool): Indicates whether the dot has been eaten.
        _is_powerup (bool): Indicates whether the dot is a power-up dot.
        _point_value (int): The point value of the dot.
    """
    def __init__(self):
        """Initializes a new Dot object.

        Sets the initial state of the dot:
            _is_eaten to False
            _is_powerup to False
            _point_value to 10
        """
        self._is_eaten:bool = False
        self._is_powerup:bool = False
        self._point_value = 10

    def is_bool(self, new_state:bool):
        """Checks if the given input is a boolean.

        Args:
            new_state (bool): The input to check.

        Returns:
            bool: True if the input is a boolean, False otherwise.
        """
        if type(new_state) != bool:
            print('Not an bool')
            print(new_state)
            return False
        return True
    
    def is_int(self, new_value:int):
        """Checks if the given input is an integer.

        Args:
            new_value (int): The input to check.

        Returns:
            bool: True if the input is an integer, False otherwise.
        """
        if type(new_value) != int:
            print('Not an int')
            print(new_value)
            return False
        return True           

    def get_point_value(self):
        """Retrieves the point value of the dot.

        Returns:
            int: The point value of the dot.
        """
        return self._point_value

    def set_point_value(self, new_value:int):
        """Sets the point value of the dot.

        Args:
            new_value (int): The new point value.

        Returns:
            None: Returns silently if the input is not an integer.
        """
        if not self.is_int(new_value):
            return
        self._point_value = new_value

    def get_is_eaten(self):
        """Retrieves the eaten state of the dot.

        Returns:
            bool: True if the dot has been eaten, False otherwise.
        """
        return self._is_eaten
    
    def set_is_eaten(self, new_state:bool):
        """Sets the eaten state of the dot.

        Args:
            new_state (bool): The new eaten state.

        Returns:
            None: Returns silently if the input is not a boolean.
        """
        if not self.is_bool(new_state):
            return
        self._is_eaten = new_state

    def get_is_powerup(self):
        """Retrieves the power-up state of the dot.

        Returns:
            bool: True if the dot is a power-up dot, False otherwise.
        """
        return self._is_powerup

    def set_is_powerup(self, new_state:bool):
        """Sets the power-up state of the dot.

        Args:
            new_state (bool): The new power-up state.

        Returns:
            None: Returns silently if the input is not a boolean.
        """
        if not self.is_bool(new_state):
            return
        self._is_powerup = new_state

    def eat(self):
        """Simulates eating the dot.

        Returns:
            dict: A dictionary containing the point value and power-up status of the dot.
                  Returns None if the dot has already been eaten.
        """
        if self._is_eaten:
            return None
        self.set_is_eaten(True)
        contents = {point_value: self._point_value,
                    is_power_up: self._is_powerup}
        return contents