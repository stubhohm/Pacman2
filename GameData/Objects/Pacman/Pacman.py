from ..Actor.Actor import Actor, Vector2
from ...Keys.Keys import up, down, left, right, directions
from ...Sprites.Sprite_Images import Pacman_Arrary

class Pacman(Actor):
    def __init__(self):
        super().__init__()
        self.actor_type = "Player"
        self.full_sprite_sheet = Pacman_Arrary
        self.lives = 3
        self.set_sprite_array()
        self.set_position(Vector2(15,14), True)

    def handle_input(self, input_direction, tile_map):
        if input_direction == "p":
            self.print()
        if input_direction not in directions:
            input_direction = self.get_direction()
        if self.check_wall_collision(input_direction, tile_map):
            self.set_velocity("STOP")
        else:
            self.set_velocity(input_direction)
        self.move(tile_map)

    def set_sprite_array(self):
        if self.lives == 0:
            self.sprite.sprite_array = self.full_sprite_sheet
        eat_slice = self.full_sprite_sheet[:3]
        for image in list(eat_slice):
            eat_slice.insert(3, image)
        self.sprite.sprite_array = eat_slice

    def print(self):
        print(self.get_direction())
        print(self.get_position().get_value())
        print(self.get_coordinate().get_value())
        print(self.get_velocity().get_value())
