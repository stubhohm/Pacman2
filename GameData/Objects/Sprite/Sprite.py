from ...Dependecies.Dependencies import Rect, Surface
from ..Vector2.Vector2 import Vector2
from ...Keys.Constants import TILE_HEIGHT, TILE_WIDTH
from ...Keys.Keys import up, down, left, right
directions = [up, down, left, right]

class Sprite():
    """Base class for sprites.

    Attributes:
        sprite (Surface): The sprite surface.
        sprite_array (list): A list of sprite frames.
        frame (int): The current frame index.
        fps (int): Frames per second.
        ticks (int): The current tick count.
    """
    def __init__(self):
        """Initializes a Sprite object."""
        self.sprite:Surface = None
        self.sprite_array = []
        self.frame = 1
        self.fps = 45
        self.ticks = 0

    def get_height(self):
        """Gets the height of the sprite.

        Returns:
            int: The height of the sprite. Defaults to TILE_HEIGHT if sprite is None.
        """
        if not self.sprite:
            return TILE_HEIGHT
        return self.sprite.get_height()

    def get_width(self):
        """Gets the width of the sprite.

        Returns:
            int: The width of the sprite. Defaults to TILE_WIDTH if sprite is None.
        """
        if not self.sprite:
            return TILE_WIDTH
        return self.sprite.get_width()

    def draw(self, window:Surface, position:Vector2, incriment:bool):
        """Draws the sprite on the window.

        Args:
            window (Surface): The window to draw on.
            position (Vector2): The position to draw the sprite at.
            incriment (bool): Whether to increment the sprite frame.
        """
        if incriment:
            self.incriment_sprite()
        self.set_frame()
        if not self.sprite and not type(self.sprite) == Surface:
            return
        window.blit(self.sprite, position.get_value())
        
    def incriment_sprite(self):
        """Increments the sprite frame."""
        self.ticks += 1
        if self.fps > self.ticks:
            return
        self.ticks = 0
        total_frames = len(self.sprite_array) 
        self.frame += 1
        if total_frames == 0:
            self.frame = 0
            return
        self.frame = self.frame % total_frames

    def set_frame(self):
        """Sets the sprite frame, and prevents frame overflow based on length of the Sprite Array """
        if not self.sprite_array:
            self.sprite = None
            return
        self.frame = self.frame % len(self.sprite_array)
        self.sprite = self.sprite_array[self.frame]

class EyeSprite(Sprite):
    """Represents an eye sprite.

    Attributes:
        last_direction (int): The last direction the eye was facing.
    """
    def __init__(self):
        """Initializes an EyeSprite object."""
        super().__init__()
        self.last_direction = None

    def set_frame(self):
        """Sets the frame of the eye sprite based on the last direction."""
        if self.last_direction not in directions:
            self.last_direction = down
        if not self.sprite_array:
            self.sprite = None
            return
        self.sprite = self.sprite_array[self.last_direction]

    def incriment_sprite(self):
        """Skips incrementing of the sprite frame."""
        pass

    def draw(self, window, position):
        """Draws the eye sprite on the window.

        Args:
            window (Surface): The window to draw on.
            position (Vector2): The position to draw the sprite at.
        """
        return super().draw(window, position, False)
    
class LivesSprite(Sprite):
    """Represents a lives sprite.

    Attributes:
        number_of_lives (int): The number of lives the player has.
    """
    def __init__(self):
        """Initializes a LivesSprite object."""
        super().__init__()

    def incriment_sprite(self):
        """Skips incrementing of the sprite frame."""
        pass

    def draw(self, window, position):
        """Draws the lives sprite on the window.

        Args:
            window (Surface): The window to draw on.
            position (Vector2): The position to draw the sprite at.
        """
        return super().draw(window, position, False)