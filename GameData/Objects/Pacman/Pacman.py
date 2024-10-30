from ..Actor.Actor import Actor, Vector2
from ...Keys.Keys import up, down, left, right, stop, directions
from ...Keys.Keys import point_value, is_power_up, is_ghost
from ...Sprites.Sprite_Images import Pacman_Arrary
from ...Dependecies.Dependencies import time

class Pacman(Actor):
    def __init__(self):
        super().__init__()
        self.actor_type = "Player"
        self.power_up_ending = 0
        self.power_up_duration = 7
        self.eaten_ghosts = 0
        self.score = 0
        self.full_sprite_sheet = Pacman_Arrary
        self.power_up = False
        self.lives = 3
        self.set_sprite_array()
        self.set_position(Vector2(1,4), True)

    def handle_input(self, input_direction):
        if input_direction == "p":
            self.print()
        self.set_velocity(input_direction)
        self.move()
        if self.power_up and time.time() > self.power_up_ending:
            self.power_up = False
            self.eaten_ghosts = 0

    def set_sprite_array(self):
        if self.lives == 0:
            self.sprite.sprite_array = self.full_sprite_sheet
        eat_slice = self.full_sprite_sheet[:3]
        for image in list(eat_slice):
            eat_slice.insert(3, image)
        self.sprite.sprite_array = eat_slice

    def eat_object(self, object_dict:dict[str, any]):
        if not object_dict:
            return
        if object_dict.get(is_ghost):
            self.eaten_ghosts += 1
            object_dict[point_value] = object_dict.get(point_value) * (2**self.eaten_ghosts)
        if points :=object_dict.get(point_value):
            self.score += points
        if object_dict.get(is_power_up):
            self.power_up = True
            self.power_up_ending = time.time() + self.power_up_duration
        
    def print(self):
        print(self.get_direction())
        print("Pacman pos")
        print(self.get_position().get_value())
        print(self.get_coordinate().get_value())
        print("Vels")
        print(self.get_velocity().get_value())
        print(self.get_desired_velocity().get_value())
        print(self.get_target_tile(self.get_velocity()).type)
