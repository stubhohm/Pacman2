from ..Actor.Actor import Actor, Vector2
from ...Keys.Keys import right
from ...Keys.Keys import point_value, is_power_up, is_ghost, is_fruit
from ...Keys.Constants import TILE_HEIGHT, TILE_WIDTH
from ...Keys.Colors import WHITE
from ...Sprites.Sprite_Images import Pacman_Image_dict
from ...Dependecies.Dependencies import time
from ..Text.PointText import BonusPointText
from ..Text.Text import Text

class Pacman(Actor):
    """Represents the Pac-Man character in the game.

    Attributes:
        actor_type (str): The type of the actor, which is "Player".
        steps (int): The number of steps taken by Pac-Man.
        power_up_ending (int): The time at which the power-up effect ends.
        power_up_duration (int): The duration of the power-up effect in seconds.
        eaten_ghosts (int): The number of ghosts eaten by Pac-Man.
        score (int): The current score of Pac-Man.
        score_text (Text): An object to display the score.
        full_sprite_sheet (dict): A dictionary containing the sprite images for Pac-Man.
        power_up (bool): A boolean indicating whether Pac-Man is in a power-up state.
        update_direction (bool): A boolean indicating whether the sprite rotation needs to be updated.
        lives (int): The current number of lives of Pac-Man.
        text_instances (list): A list of BonusPointText objects to display bonus points.
        sprite_array (list): The sprite array used for rendering Pac-Man's sprite.
        position (Vector2): The position of Pac-Man.
    """
    def __init__(self, pacman_dict:dict = {}):
        """Initializes the Pacman object.

        Args:
            pacman_dict (dict, optional): A dictionary containing initial game data for Pac-Man. Defaults to {}.
        """
        super().__init__()
        self.actor_type = "Player"
        self.steps = 0
        self.power_up_ending = 0
        self.power_up_duration = 7
        self.eaten_ghosts = 0
        self.score = pacman_dict.get("Score", 0)
        self.score_text = Text()
        self.full_sprite_sheet = Pacman_Image_dict
        self.power_up = False
        self.update_direction = False
        self.lives = pacman_dict.get("Lives", 3)
        self.text_instances:list[BonusPointText] = []
        self.set_sprite_array(right)
        self.set_position(Vector2(13,20), True)
        self.define_score_text()
        self.force_velocity(right)

    def define_score_text(self):
        """Defines the font and text for the score display."""
        self.score_text.define_font(str(self.score), Vector2(5,5), 16, WHITE)

    def handle_input(self, input_direction):
        """Handles user input to control Pac-Man's movement.

        Args:
            input_direction (str): The input direction from the user.
        """
        start_vel = self.get_velocity().get_value()
        if input_direction == "p":
            self.print()
        self.set_velocity(input_direction)
        self.move()
        if self.get_velocity().get_value() != Vector2().get_value():
            self.steps += 1
            self.incriment = True
            if self.steps % 5 == 0:
                self.steps = 0
                while self.sprite.ticks != 0:
                    self.sprite.incriment_sprite()
        else: self.incriment = False
        if self.power_up and time.time() > self.power_up_ending:
            self.power_up = False
            self.eaten_ghosts = 0
        end_vel = self.get_velocity().get_value()
        if start_vel != end_vel:
            self.update_direction = True

    def set_sprite_array(self, direction:str):
        """Sets the sprite array for Pac-Man based on the given direction.

        Args:
            direction (str): The direction to set the sprite array.
        """
        if self.lives == 0:
            self.sprite.sprite_array = self.full_sprite_sheet.get(direction)
        eat_slice = self.full_sprite_sheet.get(direction)[:3]
        for image in list(eat_slice):
            eat_slice.insert(3, image)
        self.sprite.sprite_array = eat_slice

    def eat_object(self, object_dict:dict[str, any]):
        """Handles the event when Pac-Man eats an object.

        Args:
            object_dict (dict): A dictionary containing information about the object eaten.
        """
        if not object_dict:
            return
        draw = False
        if object_dict.get(is_ghost):
            self.eaten_ghosts += 1
            object_dict[point_value] = object_dict.get(point_value) * (2**self.eaten_ghosts)
            draw = True
        if object_dict.get(is_fruit):
            draw = True
        if draw:
            text = BonusPointText()
            text.define_font(str(object_dict.get(point_value)), self.get_coordinate().add(Vector2(-TILE_WIDTH, -TILE_HEIGHT)))
            self.text_instances.append(text)
        if points :=object_dict.get(point_value):
            self.score += points
        if object_dict.get(is_power_up):
            self.power_up = True
            self.power_up_ending = time.time() + self.power_up_duration

    def update_bonuspoint_text(self):
        """Updates the bonus point text objects."""
        for text in list(self.text_instances):
            if not text:
                self.text_instances.remove(text)
                continue
            if not text.move_text():
                self.text_instances.remove(text)

    def set_sprite_rotation(self):
        """Updates the sprite rotation based on the current velocity."""
        self.update_direction = False
        direction = self.velocity_to_direction.get(self.get_velocity().get_value())
        if direction not in self.full_sprite_sheet.keys():
            return
        self.set_sprite_array(direction)
        
    def draw_sprite(self, surface):
        """Draws the Pac-Man sprite and related text on the surface.

        Args:
            surface (pygame.Surface): The surface to draw on.
        """
        if self.update_direction:
            self.set_sprite_rotation()
        super().draw_sprite(surface)
        self.update_bonuspoint_text()
        self.define_score_text()
        self.score_text.draw_font(surface)
        for text in list(self.text_instances):
            text.draw_font(surface)

    def print(self):
        """Prints Pac-Man's direction, position, velocity, and target tile to the console."""
        print(self.get_direction())
        print("Pacman pos")
        print(self.get_position().get_value())
        print(self.get_coordinate().get_value())
        print("Vels")
        print(self.get_velocity().get_value())
        print(self.get_desired_velocity().get_value())
        print(self.get_target_tile(self.get_velocity()).type)
