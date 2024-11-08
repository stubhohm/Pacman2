# Directions
up, down, left, right, stop = "up", "down", "left", "right", "stop"
directions = [up, down, left, right, stop]
direction_flips = {up:down, down:up, left:right, right:left}

# Ghost Names
inky, pinky, blinky, clyde = "Inky", "Pinky", "Blinky", "Clyde"
ghost_names = [blinky, clyde, inky, pinky]
is_ghost = "Is Ghost"

# Dot Keys
point_value, is_power_up = "point value", "is power up"

# Orientations
horizontal, vertical = "horizontal", "vertical"

# Gameplay Keys
quit_game = "quit game"
select = "select"

#Fruit Keys
is_fruit = "Is Fruit"
Apple, Bell, Cherry, Galaxian, Key, Melon, Orange, Strawberry = "Apple", "Bell", "Cherry", "Galaxian", "Key", "Melon", "Orange", "Strawberry"

fruit_values = {Apple : 700, Bell : 3000, Cherry: 100, Galaxian: 2000, Key: 5000, Melon: 1000, Orange: 500, Strawberry: 300}

fruit_dict = {1 : {"Fruit 1" : Cherry, "Fruit 2": Strawberry},
              2 : {"Fruit 1" : Strawberry, "Fruit 2": Orange},
              3 : {"Fruit 1" : Orange, "Fruit 2": Apple},
              4 : {"Fruit 1" : Orange, "Fruit 2": Apple},
              5 : {"Fruit 1" : Apple, "Fruit 2": Melon},
              6 : {"Fruit 1" : Apple, "Fruit 2": Melon},
              7 : {"Fruit 1" : Melon, "Fruit 2": Galaxian},
              8 : {"Fruit 1" : Melon, "Fruit 2": Galaxian},
              9 : {"Fruit 1" : Galaxian, "Fruit 2": Bell},
              10: {"Fruit 1" : Galaxian, "Fruit 2": Bell},
              11: {"Fruit 1" : Bell, "Fruit 2": Key},
              12: {"Fruit 1" : Bell, "Fruit 2": Key},
              13: {"Fruit 1" : Key, "Fruit 2": Key},
              }