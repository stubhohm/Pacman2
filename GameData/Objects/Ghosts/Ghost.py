class Ghost():
    def __init__(self):
        self._name = 'Unnamed Ghost'
        self._position:tuple[int, int] = (0,0)
        self._target_position:tuple[int, int] = (0,0)
        self._retreat_position:tuple[int, int] = (0,0)
        self._sprite = None
        self._is_eaten:bool = False
        self._is_scared:bool = False

    def is_coordinate(self, test_coordiante:tuple[int,int]):
        passed = True
        if type(test_coordiante) != tuple:
            print('not a tuple')
            passed = False
        if passed and len(test_coordiante) != 2:
            print('not two items')
            passed = False
        if passed and (type(test_coordiante[0]) != int or type(test_coordiante[-1]) != int):
            print("one was not an int")
            passed = False
        if not passed:
            print(test_coordiante)
        return passed

    def is_bool(self, test_state):
        if type(test_state) != bool:
            print(test_state)
            print("Not Bool")
            return False
        return True

    def is_string(self, test_string):
        if type(test_string) != str:
            print(test_string)
            print("Not a string")
            return False
        return True

    def get_name(self):
        return self._name

    def get_position(self):
        return self._position

    def get_target_position(self):
        return self._target_position

    def get_retreat_position(self):
        return self._retreat_position
    
    def get_sprite(self):
        return self._sprite

    def get_is_eaten(self):
        return self._is_eaten
    
    def get_is_scared(self):
        return self._is_scared

    def set_name(self, new_name:str):
        if not self.is_string(new_name):
            return
        self._name = new_name

    def set_position(self, new_position:tuple[int, int]):
        if not self.is_coordinate(new_position):
            return
        self._position = new_position

    def set_target_position(self, new_position:tuple[int, int]):
        if not self.is_coordinate(new_position):
            return
        self._target_position = new_position

    def set_retreat_position(self, new_position:tuple[int, int]):
        if not self.is_coordinate(new_position):
            return
        self._retreat_position = new_position
    
    def set_sprite(self, new_sprite):
        self._sprite = new_sprite
    
    def set_is_eaten(self, new_state:bool):
        if not self.is_bool(new_state):
            return
        self._is_eaten = new_state

    def set_is_scared(self, new_state:bool):
        if not self.is_bool(new_state):
            return
        self._is_scared = new_state