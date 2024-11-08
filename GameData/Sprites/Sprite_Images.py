from ..Dependecies.Dependencies import Image, Transform, os
from ..Keys.Keys import up, down, left, right
from ..Keys.Keys import Apple, Bell, Cherry, Galaxian, Key, Melon, Orange, Strawberry 

base_path = os.path.join("GameData", "Sprites")

Pacman_Arrary = [
    Image.load(os.path.join(base_path, "Pacman", "Pacman(1).png")),
    Image.load(os.path.join(base_path, "Pacman", "Pacman(2).png")),
    Image.load(os.path.join(base_path, "Pacman", "Pacman(3).png")),
    Image.load(os.path.join(base_path, "Pacman", "Pacman(4).png")),
    Image.load(os.path.join(base_path, "Pacman", "Pacman(5).png")),
    Image.load(os.path.join(base_path, "Pacman", "Pacman(6).png")),
    Image.load(os.path.join(base_path, "Pacman", "Pacman(7).png")),
    Image.load(os.path.join(base_path, "Pacman", "Pacman(8).png")),
]

new_list = []
for image in Pacman_Arrary:
    new_list.append(Transform.scale_by(image, 2))
Pacman_Arrary = new_list

Pacman_Image_dict:dict[str, list] = {}
for direction in [left, right, up, down]:
    if direction == left:
        left_images = []
        for image in list(Pacman_Arrary):
            img_copy = image.copy()
            left_images.append(Transform.flip(img_copy, True, False))
        Pacman_Image_dict[left] = left_images
    if direction == right:
        right_images = []
        for image in list(Pacman_Arrary):
            right_images.append(image.copy())
        Pacman_Image_dict[right] = right_images
    if direction == up:
        up_images = []
        for image in list(Pacman_Arrary):
            img_copy = image.copy()
            up_images.append(Transform.rotate(img_copy, 90))
        Pacman_Image_dict[up] = up_images
    if direction == down:
        down_images = []
        for image in list(Pacman_Arrary):
            img_copy = image.copy()
            down_images.append(Transform.rotate(img_copy, -90))
        Pacman_Image_dict[down] = down_images
            

Ghost_eyes = { 
    up: Image.load(os.path.join(base_path, "Eyes", "eyes_up.png")),
    left : Image.load(os.path.join(base_path, "Eyes", "eyes_left.png")),
    right: Image.load(os.path.join(base_path, "Eyes", "eyes_right.png")),
    down : Image.load(os.path.join(base_path, "Eyes", "eyes_down.png"))
}
new_dict = {}
for image in Ghost_eyes.keys():

    new_dict[image] = (Transform.scale_by(Ghost_eyes[image], 1.7))
Ghost_eyes = new_dict

Blinky_Array = [
    Image.load(os.path.join(base_path, "Blinky", "Blinky_1.png")),
    Image.load(os.path.join(base_path, "Blinky", "Blinky_2.png"))
]

new_list = []
for image in Blinky_Array:
    new_list.append(Transform.scale_by(image, 1.7))
Blinky_Array = new_list

Clyde_Array = [
    Image.load(os.path.join(base_path, "Clyde", "Clyde_1.png")),
    Image.load(os.path.join(base_path, "Clyde", "Clyde_2.png"))
]

new_list = []
for image in Clyde_Array:
    new_list.append(Transform.scale_by(image, 1.7))
Clyde_Array = new_list

Inky_Array = [
    Image.load(os.path.join(base_path, "Inky", "Inky_1.png")),
    Image.load(os.path.join(base_path, "Inky", "Inky_2.png"))
]

new_list = []
for image in Inky_Array:
    new_list.append(Transform.scale_by(image, 1.7))
Inky_Array = new_list

Pinky_Array = [
    Image.load(os.path.join(base_path, "Pinky", "Pinky_1.png")),
    Image.load(os.path.join(base_path, "Pinky", "Pinky_2.png"))
]

new_list = []
for image in Pinky_Array:
    new_list.append(Transform.scale_by(image, 1.7))
Pinky_Array = new_list

Frightend_Array = [ 
    Image.load(os.path.join(base_path, "Frightened", "Frightened_1.png")),
    Image.load(os.path.join(base_path, "Frightened", "Frightened_2.png")),
    Image.load(os.path.join(base_path, "Frightened", "Frightened_3.png")),
    Image.load(os.path.join(base_path, "Frightened", "Frightened_4.png"))
]

new_list = []
for image in Frightend_Array:
    new_list.append(Transform.scale_by(image, 1.7))
Frightend_Array = new_list

Eaten_Image = [Image.load(os.path.join(base_path, "Eaten", "eaten.png"))]

new_list = []
for image in Eaten_Image:
    new_list.append(Transform.scale_by(image, 1.7))
Eaten_Image = new_list

Fruit_Images = {Apple : Image.load(os.path.join(base_path, "Fruit", "Apple.png")), 
                Bell : Image.load(os.path.join(base_path, "Fruit", "Bell.png")), 
                Cherry : Image.load(os.path.join(base_path, "Fruit", "Cherry.png")), 
                Galaxian : Image.load(os.path.join(base_path, "Fruit", "Galaxian.png")), 
                Key : Image.load(os.path.join(base_path, "Fruit", "Key.png")),
                Melon : Image.load(os.path.join(base_path, "Fruit", "Melon.png")),
                Orange : Image.load(os.path.join(base_path, "Fruit", "Orange.png")),
                Strawberry : Image.load(os.path.join(base_path, "Fruit", "Strawberry.png")),}

new_dict[str, Image] = {}
for key in Fruit_Images.keys():
    image = Fruit_Images.get(key)
    new_dict[key] = (Transform.scale_by(image, 2))
Fruit_Images = new_dict