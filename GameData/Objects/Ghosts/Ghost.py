from ..Vector2.Vector2 import Vector2
from ...Keys.Constants import DEBUG
from ...Keys.Colors import WHITE
from ..Actor.Actor import Actor, directions, up, down, left, right, stop
from ...Keys.Keys import direction_flips, point_value, is_ghost
from ..Sprite.Sprite import EyeSprite, Surface
from ...Sprites.Sprite_Images import Eaten_Image, Ghost_eyes, Frightend_Array

class Ghost(Actor):
    """Represents a ghost in the game.

    Attributes:
        _name (str): The name of the ghost. Defaults to 'Unnamed Ghost'.
        _target_position (Vector2): The ghost's target position.
        _retreat_position (Vector2): The ghost's retreat position.
        _ghost_eye_sprite (EyeSprite): The ghost's eye sprite.
        ghost_images (List[Surface]): A list of ghost images to use for animation.
        fightened_images (Frightend_Array): A list of frightened ghost images.
        eaten_image (Eaten_Image): The image to display when the ghost is eaten.
        _is_eaten (bool): A boolean indicating if the ghost has been eaten. Defaults to False.
        _is_scared (bool): A boolean indicating if the ghost is scared. Defaults to False.
        actor_type (str): The type of the actor. Defaults to "Ghost".
        last_direction (str): The last direction the ghost moved in. Defaults to 'stop'.
        skipped_frames_per_second (int): The number of frames to skip per second. Defaults to 30.
        in_node (bool): A boolean indicating whether the ghost is in a node. Defaults to False.
        color (str): The color of the ghost. Defaults to 'WHITE'.
    """
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
        """Returns the name of the ghost.

        Returns:
            str: The name of the ghost.
        """
        return self._name

    def get_target_position(self):
        """Returns the target position of the ghost.

        Returns:
            Vector2: The target position of the ghost.
        """
        return self._target_position

    def get_retreat_position(self):
        """Returns the retreat position of the ghost.

        Returns:
            Vector2: The retreat position of the ghost.
        """
        return self._retreat_position
    
    def get_is_eaten(self):
        """Returns True if the ghost has been eaten, False otherwise.

        Returns:
            bool: True if the ghost has been eaten, False otherwise.
        """
        return self._is_eaten
    
    def get_is_scared(self):
        """Returns True if the ghost is scared, False otherwise.

        Returns:
            bool: True if the ghost is scared, False otherwise.
        """
        return self._is_scared

    def set_name(self, new_name:str):
        """Sets the name of the ghost.

        Args:
            new_name (str): The new name for the ghost.
        """
        if not self.is_string(new_name):
            return
        self._name = new_name

    def set_target_position(self, new_position:Vector2):
        """Sets the target position of the ghost.

        Args:
            new_position (Vector2): The new target position.
        """
        if not self.is_coordinate(new_position):
            return
        self._target_position = new_position

    def set_retreat_position(self, new_position:Vector2):
        """Sets the retreat position of the ghost.

        Args:
            new_position (Vector2): The new retreat position.
        """
        if not self.is_coordinate(new_position):
            return
        self._retreat_position = new_position
    
    def set_is_eaten(self, new_state:bool):
        """Sets whether the ghost is eaten.

        Args:
            new_state (bool): True if the ghost is eaten, False otherwise.
        """
        if not self.is_bool(new_state):
            return
        self._is_eaten = new_state
        if self._is_eaten:
            self.set_is_scared(False)
            self.skipped_frames_per_second = 0

    def set_is_scared(self, new_state:bool):
        """Sets whether the ghost is scared.

        Args:
            new_state (bool): True if the ghost is scared, False otherwise.
        """
        if not self.is_bool(new_state):
            return
        if self._is_eaten:
            return
        self._is_scared = new_state
        if self._is_scared:
            self.skipped_frames_per_second = 60
            self.sprite.frame = 0
        else:
            self.skipped_frames_per_second = 30

    def set_last_direction(self, direction):
        """Sets the last direction the ghost moved in.

        Args:
            direction (str): The last direction the ghost moved in.
        """
        self._ghost_eye_sprite.last_direction = direction
        self.last_direction = direction

    def set_ghost_eyes(self):
        """Sets the ghost's eyes sprite.
        """
        self._ghost_eye_sprite.sprite_array = Ghost_eyes

    def chase_input_function(self, vector_1:Vector2, vector_2:Vector2 = None):
        """Moves the ghost towards the target position based on input.

        Args:
            vector_1 (Vector2): The first input vector.
            vector_2 (Vector2, optional): The second input vector. Defaults to None.
        """
        self.move_ghost(vector_1)

    def shuffle_list(self, list):
        """Shuffles a list in place.

        Args:
            list (List[Surface]): The list to shuffle.

        Returns:
            List[Surface]: The shuffled list.
        """
        for i in range(len(list) - 1, 0, -1):
            # Generate a random index to swap with
            j = int(i * (1 / (i + 1)))
            # Swap the elements
            list[i], list[j] = list[j], list[i]
        return list

    def eat_ghost(self):
        """Simulates the ghost eating another ghost.

        Returns:
            dict: A dictionary containing the points awarded and whether the eaten ghost is a ghost.
        """
        if self._is_scared and not self._is_eaten:
            self.set_is_eaten(True)
            return {point_value : 100 ,
                    is_ghost : True}
        return None

    def find_best_option(self, target_position:Vector2, viable_options:list[str]):
        """Finds the best option to move to from a given position.

        Args:
            target_position (Vector2): The target position.
            viable_options (List[str]): A list of viable options.

        Returns:
            str: The best option to move to.
        """
        if self._is_eaten:
            target_position = Vector2(14,14)

        refined_array = []
        shortest = None
        tgt_x, tgt_y = target_position.get_value()
        self.set_target_position(target_position)
        for option in viable_options:
            x, y = self.direction_to_velocity.get(option)
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
        return refined_array[0]

    def get_viable_options(self):
        options = list(directions)
        # Remove stop option and the flip option
        options.remove(stop)
        tile = self.get_target_tile(Vector2())
        if tile.limited:
            options.remove(up)
        if direction_flips.get(self.last_direction) in options:
            options.remove(direction_flips.get(self.last_direction))
        refined_options = list(options)
        for option in options:
            x , y = self.direction_to_velocity.get(option)
            vec = Vector2(2 * x, 2 * y)
            tile = self.get_target_tile(vec)
            if tile and tile.is_passable():
                continue
            else:
                refined_options.remove(option)
        return refined_options
        
    def select_direction(self, best_direction:str):
        return best_direction
 
    def move_ghost(self, target_position:Vector2):
        """Moves the ghost in the specified direction.

        Args:
            direction (str): The direction to move in.
        """
        current_tile = self.get_target_tile(Vector2())
        if "Node" not in current_tile.type:
            self.in_node = False
        if "Node" in current_tile.type and self.is_centered(True) and not self.in_node:
            self.in_node = True
            viable_options = self.get_viable_options()
            best_direction = self.find_best_option(target_position, viable_options)
            best_available = self.select_direction(best_direction)
            if best_available != stop:
                self.set_last_direction(best_available)
        self.set_velocity(self.last_direction)
        self.move()
        if self.get_position().get_value() == Vector2(14,14).get_value() and self.get_is_eaten():
            self.set_is_eaten(False)
            self.set_is_scared(False)

    def draw_sprite(self, surface):
        if DEBUG:
            self.drawing.draw_line(surface, self.get_coordinate(), self.get_coordinate_from_position(self.get_target_position()), self.color, 3)
        
        self.sprite.sprite_array = self.ghost_images
        
        if self._is_eaten:
            self.sprite.sprite_array = self.eaten_image

        if self._is_scared and not self._is_eaten:
            self.sprite.sprite_array = self.fightened_images

            
        super().draw_sprite(surface)
        if self._ghost_eye_sprite and (not self._is_scared or self._is_eaten):
            self._ghost_eye_sprite.draw(surface, self.get_sprite_coordinate())