class Tile():
    def __init__(self):
        self._sprite = None
        self._position:tuple[int,int]
        self._passable:bool = True

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

    def is_string(self, test_string:str):
        if type(test_string) !=str:
            print(test_string)
            print("not a string")
            return False
        return True
    
    def is_bool(self, test_bool:bool):
        if type(test_bool) != bool:
            print(test_bool)
            print("Not Bool")
            return False
        return True

    def is_int(self, test_int:int):
        if type(test_int) != int:
            print(test_int)
            print("Not Int")
            return False
        return True

    def get_position(self):
        return self._position

    def is_passable(self):
        return self._passable
    
    def get_sprite(self):
        return self._sprite

    def set_position(self, new_position:tuple[int, int]):
        if not self.is_coordinate(new_position):
            return
        self._position = new_position

    def set_is_passable(self, new_state:bool):
        if not self.is_bool(new_state):
            return
        self._passable = new_state

    def set_sprite(self, sprite):
        self._sprite = sprite