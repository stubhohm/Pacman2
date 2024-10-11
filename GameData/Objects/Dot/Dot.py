from ..Keys.Keys import point_value, is_power_up

class Dot():
    def __init__(self):
        self._coordiante:tuple[int,int] = (0,0)
        self._is_eaten:bool = False
        self._is_powerup:bool = False
        self._point_value = 10

    def is_coordinate(self, new_coordinate:tuple[int,int]):
        passed = True
        if type(new_coordinate) != tuple:
            print('not a tuple')
            passed = False
        if passed and len(new_coordinate) != 2:
            print('not two items')
            passed = False
        if passed and (not self.is_int(new_coordinate[0]) or not self.is_int(new_coordinate[-1])):
            print("one was not an int")
            passed = False
        if not passed:
            print(new_coordinate)
        return passed

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

    def get_coordinate(self):
        return self._coordiante
    
    def set_coordinate(self, new_coordinate:tuple[int, int]):
        if not self.is_coordinate(new_coordinate):
            return
        self._coordiante = new_coordinate

    def get_is_eaten(self):
        return self._is_eaten
    
    def set_is_eaten(self, new_state:bool):
        if not self.is_bool(new_state):
            return
        self._is_eaten = new_state

    def get_is_powerup(self):
        return self._is_powerup

    def set_is_powerup(self, new_state):
        if not self.is_bool(new_state):
            return
        self._is_powerup = new_state

    def eat(self):
        if self._is_eaten:
            return 0
        self.set_is_eaten(True)
        contents = {"value": self._point_value,
                    "powerup": self._is_powerup}
        return contents