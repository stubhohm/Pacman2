from ..Objects.Vector3.Vector3 import Vector3

WHITE = Vector3(255,255,255)
BLACK = Vector3(0,0,0)

RED = Vector3(255, 0, 0)
ORANGE = Vector3(255, 125, 0)
YELLOW = Vector3(255, 125, 0)
SPRING_GREEN = Vector3(125, 255, 0)
GREEN = Vector3(0, 255, 0)
TURQUISE = Vector3(0, 255, 125)
CYAN = Vector3(0, 255, 255)
OCEAN = Vector3(0, 125, 125)
BLUE = Vector3(0, 0, 255)
VIOLET = Vector3(125, 0, 255)
MAGENTA = Vector3(255, 0, 255)
RASPBERRY = Vector3(255, 0, 125)


class ColorMixer():
    """
    A class for mixing and adjusting colors.

    Attributes:
        None

    Methods:
        is_RGB_color(color: Vector3)
        blend_colors(color_1: Vector3, color_2: Vector3, gradient: float)
        adjust_color_saturation(color: tuple[int, int, int], saturation: float)
        adjust_color_brightness(color: tuple[int, int, int], brightness: float)
    """
    def __init__(self):
        """
        Initializes the ColorMixer object.
        """
        pass

    def is_RGB_color(self, color:Vector3):
        """
        Checks if a given color is a valid RGB color.

        Args:
            color (Vector3): The color to check.

        Returns:
            bool: True if the color is a valid RGB color, False otherwise.
        """
        if type(color) != Vector3:
            print("not a Vector 3")
            return False
        return True

    def blend_colors(self,color_1:Vector3, color_2:Vector3, gradient:float):
        """
        Blends two RGB colors based on a gradient.

        Args:
            color_1 (Vector3): The first RGB color.
            color_2 (Vector3): The second RGB color.
            gradient (float): The blending gradient between 0 and 1.

        Returns:
            Vector3: The blended RGB color.
        """
        if gradient > 1 or gradient < 0:
            gradient = gradient % 1
        if not self.is_RGB_color(color_1) or not self.is_RGB_color(color_2):
            print('Not a valid RGB color')
            return
        # Get Color Tuples for iteration
        color_1_tuple = color_1.get_value()
        color_2_tuple = color_2.get_value()
        
        # Get the distnace between the colors at each rgb value and scale based on gradient
        delta_list = []
        for i in range(len(color_1_tuple)):
            delta_list.append(int((color_2_tuple[i] - color_1_tuple[i]) * gradient))
        
        # Make a new color based on the scaled shift, added to the base color
        new_color_tuple = []
        for i, value in enumerate(delta_list):
            new_color_tuple.append(color_1_tuple[i] + value)

        # package up as vector to export
        r , g , b = new_color_tuple[0], new_color_tuple[1], new_color_tuple[2]

        return Vector3(r, g, b)

    def adjust_color_saturation(self, color:tuple[int,int,int], saturation:float):
        """
        Adjusts the saturation of a color.

        Args:
            color (tuple[int, int, int]): The RGB color to adjust.
            saturation (float): The saturation value between 0 and 1.

        Returns:
            Vector3: The adjusted RGB color.
        """
        return self.blend_colors(WHITE, color, saturation)

    def adjust_color_brightness(self, color:tuple[int,int,int], brightness:float):
        """
        Adjusts the brightness of a color.

        Args:
            color (tuple[int, int, int]): The RGB color to adjust.
            brightness (float): The brightness value between 0 and 1.

        Returns:
            Vector3: The adjusted RGB color.
        """
        return self.blend_colors(BLACK, color, brightness)
        

"""
Color_Mixer = ColorMixer()
new_color = BLUE
print(new_color)
new_color = Color_Mixer.adjust_color_brightness(new_color, 1)
print(new_color)
new_color = Color_Mixer.adjust_color_saturation(new_color, .5)
print(new_color)
new_color = Color_Mixer.blend_colors(new_color, RED, .5)
print(new_color)
"""