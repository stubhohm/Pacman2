from ..Vector2.Vector2 import Vector2
from ...Keys.Constants import DEBUG
from ...Keys.Colors import WHITE
from ..Actor.Actor import Actor, directions, up, down, left, right, stop, velocity_to_direction, direction_to_velocity
from ...Keys.Keys import direction_flips
from ..Sprite.Sprite import EyeSprite, Surface
from ...Sprites.Sprite_Images import Eaten_Image, Ghost_eyes, Frightend_Array

class Ghost(Actor):
    def __init__(self):
        super().__init__()
        self._name = 'Unnamed Ghost'
        self._target_position:Vector2 = Vector2(0,0)
        self._retreat_position:Vector2 = Vector2(0,0)
        self._ghost_eye_sprite:EyeSprite = EyeSprite()
        self.ghost_images:list[Surface] = []
        self.fightened_images = Frightend_Array
        self.eaten_image = Eaten_Image
        self._is_eaten:bool = False
        self._is_scared:bool = False
        self.actor_type = "Ghost"
        self.last_direction = stop
        self.set_ghost_eyes()
        self.skipped_frames_per_second = 30
        self.in_node = False
        self.color = WHITE

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
        if self._is_eaten:
            self.set_is_scared(False)

    def set_is_scared(self, new_state:bool):
        if not self.is_bool(new_state):
            return
        self._is_scared = new_state

    def set_last_direction(self, direction):
        self._ghost_eye_sprite.last_direction = direction
        self.last_direction = direction

    def set_ghost_eyes(self):
        self._ghost_eye_sprite.sprite_array = Ghost_eyes

    def chase_input_function(self, vector_1:Vector2, vector_2:Vector2 = None):
        self.move_ghost(vector_1)

    def shuffle_list(self, list):
        for i in range(len(list) - 1, 0, -1):
            # Generate a random index to swap with
            j = int(i * (1 / (i + 1)))
            # Swap the elements
            list[i], list[j] = list[j], list[i]
        return list

    def find_best_option(self, target_position:Vector2, viable_options:list[str]):
        refined_array = []
        shortest = None
        tgt_x, tgt_y = target_position.get_value()
        self.set_target_position(target_position)
        for option in viable_options:
            x, y = direction_to_velocity.get(option)
            p_x, p_y = self.get_position().get_value()
            vec = Vector2((p_x + x - tgt_x), (p_y + y - tgt_y))
            magnitude = vec.quick_magnitude()
            if not shortest:
                shortest = magnitude
            if magnitude == shortest:
                refined_array.append(option)
            if magnitude < shortest:
                refined_array = [option]
        if len(refined_array) > 1:
            refined_array = self.shuffle_list(refined_array)
        print(refined_array)
        return refined_array[0]

    def get_viable_options(self):
        options = list(directions)
        # Remove stop option and the flip option
        options.remove(stop)
        print(options)
        if direction_flips.get(self.last_direction) in options:
            options.remove(direction_flips.get(self.last_direction))
        refined_options = list(options)
        for option in options:
            x , y = direction_to_velocity.get(option)
            vec = Vector2(2 * x, 2 * y)
            tile = self.get_target_tile(vec)
            if tile and tile.is_passable():
                continue
            else:
                refined_options.remove(option)
        return refined_options
        
    def select_direction(self, best_direction:str):
        return best_direction
 
    def move_ghost(self, pacman_position:Vector2):
        current_tile = self.get_target_tile(Vector2())
        if current_tile.type != "Node":
            self.in_node = False
        if current_tile.type == "Node" and self.is_centered(True) and not self.in_node:
            self.in_node = True
            print("\n+++ START DIR +++")
            print(self.last_direction)
            self.in_node = True
            viable_options = self.get_viable_options()
            print(viable_options)
            best_direction = self.find_best_option(pacman_position, viable_options)
            print(best_direction)
            best_available = self.select_direction(best_direction)
            print(best_available)
            if best_available != stop:
                self.set_last_direction(best_available)
            print(self.last_direction)
            print("+++ END DIR +++\n")
        self.set_velocity(self.last_direction)
        self.move()

    def draw_sprite(self, surface):
        if not DEBUG:
            self.drawing.draw_line(surface, self.get_coordinate(), self.get_coordinate_from_position(self.get_target_position()), self.color, 3)
        if self._is_scared and not self._is_eaten:
            self.sprite.sprite_array = self.fightened_images
        elif self._is_eaten:
            self.sprite.sprite_array = self.eaten_image
        else:
            self.sprite.sprite_array = self.ghost_images
        super().draw_sprite(surface)
        if self._ghost_eye_sprite and not self._is_scared:
            self._ghost_eye_sprite.draw(surface, self.get_sprite_coordinate())