from ..Dependecies.Dependencies import Image, Transform, os
from ..Keys.Keys import up, down, left, right

base_path = os.path.join("GameData", "Sprites")

Pacman_Arrary = [
    Image.load(base_path + "\\Pacman\\Pacman(1).png"),
    Image.load(base_path + "\\Pacman\\Pacman(2).png"),
    Image.load(base_path + "\\Pacman\\Pacman(3).png"),
    Image.load(base_path + "\\Pacman\\Pacman(4).png"),
    Image.load(base_path + "\\Pacman\\Pacman(5).png"),
    Image.load(base_path + "\\Pacman\\Pacman(6).png"),
    Image.load(base_path + "\\Pacman\\Pacman(7).png"),
    Image.load(base_path + "\\Pacman\\Pacman(8).png"),
]

Ghost_eyes = { 
    up: Image.load(base_path + "\\Eyes\\eyes_up.png"),
    left : Image.load(base_path + "\\Eyes\\eyes_left.png"),
    right: Image.load(base_path + "\\Eyes\\eyes_right.png"),
    down : Image.load(base_path + "\\Eyes\\eyes_down.png")
}

Blinky_Array = [
    Image.load(base_path + "\\Blinky\\Blinky_1.png"),
    Image.load(base_path + "\\Blinky\\Blinky_2.png")
]

Clyde_Array = [
    Image.load(base_path + "\\Clyde\\Clyde_1.png"),
    Image.load(base_path + "\\Clyde\\Clyde_2.png")
]

Inky_Array = [
    Image.load(base_path + "\\Inky\\Inky_1.png"),
    Image.load(base_path + "\\Inky\\Inky_2.png")
]

Pinky_Array = [
    Image.load(base_path + "\\Pinky\\Pinky_1.png"),
    Image.load(base_path + "\\Pinky\\Pinky_2.png")
]

Frightend_Array = [ 
    Image.load(base_path + "\\Frightened\\Frightened_1.png"),
    Image.load(base_path + "\\Frightened\\Frightened_2.png"),
    Image.load(base_path + "\\Frightened\\Frightened_3.png"),
    Image.load(base_path + "\\Frightened\\Frightened_4.png")
]

Eaten_Image = Image.load(base_path + "\\Eaten\\eaten.png")
