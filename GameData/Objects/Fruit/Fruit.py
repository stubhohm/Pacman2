from ...Dependecies.Dependencies import time
from ...Keys.Constants import TILE_WIDTH, TILE_HEIGHT
from ...Keys.Keys import fruit_values, point_value, Key, is_fruit
from ..Actor.Actor import Actor, Vector2
from ...Sprites.Sprite_Images import Fruit_Images

class Fruit(Actor):
    def __init__(self, fruit:str, first_fruit:bool):
        super().__init__()
        self.actor_type = "Fruit"
        if not fruit:
            fruit = Key
        self.fruit_type = fruit
        self.is_eaten = False
        self.is_visible = False
        self.timer = None
        self.duration = 9.5
        if first_fruit:
            self.dot_appearance = 70
        else:
            self.dot_appearance = 170
        self.select_image()

    def select_image(self):
        image = Fruit_Images.get(self.fruit_type)
        self.sprite.sprite_array = [image]
        coordinate = self.get_coordinate_from_position(Vector2(13, 20))
        coordinate = coordinate.add(Vector2(TILE_WIDTH, int(TILE_HEIGHT / 2)))
        self.set_coordinate(coordinate)
        self.value = fruit_values.get(self.fruit_type)

    def update_visibility(self, dots_eaten:int, can_see_previous_fruit:bool):
        if can_see_previous_fruit:
            self.is_visible = False
            return
        if self.is_eaten:
            self.is_visible = False
            return
        if self.timer and time.time() > self.timer:
            self.is_visible = False
            return
        if not self.is_visible and not self.is_eaten and dots_eaten >= self.dot_appearance:
            self.is_visible = True
            self.timer = time.time() + self.duration

    def eat_fruit(self):
        if not self.is_visible:
            return False
        if self.is_eaten:
            return False
        self.is_eaten = True
        return {point_value : self.value,
                is_fruit : True}

    def draw_sprite(self, surface):
        if not self.is_visible:
            return
        super().draw_sprite(surface)