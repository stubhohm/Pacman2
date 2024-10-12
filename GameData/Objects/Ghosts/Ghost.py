from ..Vector2.Vector2 import Vector2
from ..Actor.Actor import Actor

class Ghost(Actor):
    def __init__(self):
        self._name = 'Unnamed Ghost'
        self._target_position:Vector2 = Vector2(0,0)
        self._retreat_position:Vector2 = Vector2(0,0)
        self._is_eaten:bool = False
        self._is_scared:bool = False
        self.actor_type = "Ghost"

    def get_name(self):
        return self._name

    def get_target_position(self):
        return self._target_position

    def get_retreat_position(self):
        return self._retreat_position
    
    def get_is_eaten(self):
        return self._is_eaten
    
    def get_is_scared(self):
        return self._is_scared

    def set_name(self, new_name:str):
        if not self.is_string(new_name):
            return
        self._name = new_name

    def set_target_position(self, new_position:Vector2):
        if not self.is_coordinate(new_position):
            return
        self._target_position = new_position

    def set_retreat_position(self, new_position:Vector2):
        if not self.is_coordinate(new_position):
            return
        self._retreat_position = new_position
    
    def set_is_eaten(self, new_state:bool):
        if not self.is_bool(new_state):
            return
        self._is_eaten = new_state

    def set_is_scared(self, new_state:bool):
        if not self.is_bool(new_state):
            return
        self._is_scared = new_state