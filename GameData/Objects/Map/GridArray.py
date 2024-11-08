from ...Keys.Constants import ROWS, COLUMNS
from ..Tile.TileTypes import Node, Wall, Path, Tile
from ..Dot.PowerUp import PowerUp, Dot

def make_dot_path():
    path = make_path()
    path.add_dot(Dot())
    return path

def make_dot_node():
    node = make_node()
    dot = Dot()
    node.add_dot(dot)
    return node

def make_powerup_path():
    path = make_path()
    powerup = PowerUp()
    path.add_dot(powerup)
    return path

def make_powerup_node():
    node = make_node()
    node.add_dot(PowerUp())
    return node

def make_wall():
    return Wall()

def make_node():
    return Node()

def make_path():
    return Path()

def make_tile():
    return Tile()

def make_limited_node():
    node = make_node()
    node.limited = True
    return node

def make_limited_dot_node():
    node = make_limited_node()
    node.add_dot(Dot())
    node.limited = True
    return node

def construct_row(dot_nodes:tuple = (), walls:tuple = (), power_ups:tuple= (), 
                  empty_tiles:tuple = (), empty_nodes:tuple = (), power_up_nodes:tuple = (), 
                  limited_nodes:tuple = (), limited_dot_nodes:tuple = (), path_tiles:tuple = ()):
    row = []
    for i in range(COLUMNS):
        if i in dot_nodes:
            row.append(make_dot_node())
        elif i in walls:
            row.append(make_wall())
        elif i in power_ups:
            row.append(make_powerup_path())
        elif i in empty_tiles:
            row.append(make_tile())
        elif i in empty_nodes:
            row.append(make_node())
        elif i in power_up_nodes:
            row.append(make_powerup_node())
        elif i in limited_nodes:
            row.append(make_limited_node())
        elif i in limited_dot_nodes:
            row.append(make_limited_dot_node())
        elif i in path_tiles:
            row.append(make_path())
        else:
            if i in (0, 27):
                row.append(make_wall())
            else:
                row.append(make_dot_path())
    return row

def make_grid_array():

    empty_row = []
    wall_row_top = []
    wall_row_bottom = []
    dot_path_row = []

    for i in range(COLUMNS):
        empty_row.append(make_tile())
        wall_row_top.append(make_wall())
        wall_row_bottom.append(make_wall())

    # rows 1,
    dot_nodes = (1, 6, 12, 15, 21, 26)
    walls = (13 , 14)
    row_1 = construct_row(dot_nodes, walls)
    dot_nodes = (1, 6, 9, 12, 15, 18, 21, 26)
    row_20 = construct_row(dot_nodes, walls)
    dot_nodes = (1, 12, 15, 26)
    row_29 = construct_row(dot_nodes)

    # Rows 2, 3, 4
    dot_nodes = ()
    walls = (2, 3, 4, 5, 7, 8, 9, 10, 11, 13, 14, 16, 17, 18,19, 20, 22, 23, 24, 25)
    power_ups = (1, 26)
    row_2 = construct_row(dot_nodes, walls)
    row_3 = construct_row(dot_nodes, walls, power_ups)
    row_4 = construct_row(dot_nodes, walls)
    walls = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25)
    row_27 = construct_row(dot_nodes, walls)
    row_28 = construct_row(dot_nodes, walls)

    # Rows 5, last
    dot_nodes = (1, 6, 9, 12, 15, 18, 21, 26)
    walls = ()
    power_ups = ()
    row_5 = construct_row(dot_nodes, walls)

    # Row 6, 7
    dot_nodes = ()
    walls = (2, 3, 4, 5, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 19, 20, 22, 23, 24, 25)
    power_ups = ()
    row_6 = construct_row(dot_nodes, walls)
    row_7 = construct_row(dot_nodes, walls)

    # row 8
    dot_nodes = (1, 6, 9, 12, 15, 18, 21, 26)
    walls = (7, 8, 13, 14, 19, 20)
    power_ups = ()
    row_8 = construct_row(dot_nodes, walls)
    dot_nodes = (1, 3, 6, 9, 12, 15, 18, 21, 24, 26)
    row_26 = construct_row(dot_nodes, walls)

    # row 9
    dot_nodes = ()
    walls = (1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 13, 14, 16, 17, 18, 19, 20, 22, 23, 24, 25, 26)
    power_ups = ()
    row_9 = construct_row(dot_nodes, walls)

    # row 10
    dot_nodes = ()
    walls = (0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 13, 14, 16, 17, 18, 19, 20, 22, 23, 24, 25, 26, 27)
    power_ups = ()
    #empty_tiles = (0, 1, 2, 3, 4, 23, 24, 25, 26, 27)
    row_10 = construct_row(dot_nodes, walls, power_ups)

    # row 11
    dot_nodes = ()
    empty_nodes = (9, 18)
    walls = (0, 1, 2, 3, 4, 5, 7, 8, 19, 20, 22, 23, 24, 25, 26, 27)
    power_ups = ()
    empty_tiles = (10, 11, 13, 14, 16, 17)
    limited_nodes = (12, 15)
    row_11 = construct_row(dot_nodes, walls, power_ups, empty_tiles, empty_nodes, limited_nodes=limited_nodes)

    # row 12
    dot_nodes = ()
    empty_nodes = ()
    walls = (0, 1, 2, 3, 4, 5, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 19, 20, 22, 23, 24, 25, 26, 27)
    power_ups = ()
    empty_tiles = (9, 18)
    row_12 = construct_row(dot_nodes, walls, power_ups, empty_tiles, empty_nodes)
    row_16 = construct_row(dot_nodes, walls, power_ups, empty_tiles, empty_nodes)
    row_18 = construct_row(dot_nodes, walls, power_ups, empty_tiles, empty_nodes)


    # row 13
    dot_nodes = ()
    empty_nodes = ()
    walls = (0, 1, 2, 3, 4, 5, 7, 8, 10, 17, 19, 20, 22, 23, 24, 25, 26, 27)
    power_ups = ()
    empty_tiles = ( 9, 11, 12, 13, 14, 15, 16, 18)
    row_13 = construct_row(dot_nodes, walls, power_ups, empty_tiles, empty_nodes)
    row_15 = construct_row(dot_nodes, walls, power_ups, empty_tiles, empty_nodes)


    # row 14
    dot_nodes = (6, 21)
    empty_nodes = (9, 18)
    walls = (10, 17)
    power_ups = ()
    empty_tiles = (0, 1, 2, 3, 4, 5, 7, 8, 11, 12, 14, 13, 15, 16, 19, 20, 22, 23, 24, 25, 26, 27)
    row_14 = construct_row(dot_nodes, walls, power_ups, empty_tiles, empty_nodes)

    # Row 17
    dot_nodes = ()
    empty_nodes = (9, 18)
    walls = (0, 1, 2, 3, 4, 5, 7, 8, 19, 20, 22, 23, 24, 25, 26, 27)
    power_ups = ()
    empty_path_tiles = (10, 11, 12, 13, 14, 15, 16, 17)
    row_17 = construct_row(dot_nodes, walls, power_ups, path_tiles=empty_path_tiles, empty_nodes=empty_nodes)

    # Row 19
    dot_nodes = ()
    empty_nodes = ()
    walls = (0, 1, 2, 3, 4, 5, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 19, 20, 22, 23, 24, 25, 26, 27)
    power_ups = ()
    empty_tiles = (9, 18)
    row_19 = construct_row(dot_nodes, walls, power_ups, empty_tiles, empty_nodes)

    # Row 21, 22
    dot_nodes = ()
    walls = (2, 3, 4, 5, 7, 8, 9, 10, 11, 13, 14, 16, 17, 18, 19, 20, 22, 23, 24, 25)
    power_ups = ()
    row_21 = construct_row(dot_nodes, walls)
    row_22 = construct_row(dot_nodes, walls)

    # row 23
    dot_nodes = (3, 6, 9, 18, 21, 24)
    power_ups_node = (1, 26)
    walls = (4 ,5, 22, 23)
    limited_dot_nodes = (12, 15)
    row_23 = construct_row(dot_nodes, walls, (), (), (), power_ups_node, limited_dot_nodes=limited_dot_nodes)

    # Row 24, 25
    dot_nodes = ()
    empty_nodes = ()
    walls = (1, 2, 4, 5, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 19, 20, 22, 23, 25, 26)
    power_ups = ()
    empty_tiles = ()
    row_24 = construct_row(dot_nodes, walls, power_ups, empty_tiles, empty_nodes)
    row_25 = construct_row(dot_nodes, walls, power_ups, empty_tiles, empty_nodes)


    grid_array = [
        empty_row,
        empty_row,
        empty_row,
        wall_row_top,
        row_1,
        row_2,
        row_3,
        row_4,
        row_5,
        row_6,
        row_7,
        row_8,
        row_9,
        row_10,
        row_11,
        row_12,
        row_13,
        row_14,
        row_15,
        row_16,
        row_17, 
        row_18,
        row_19,
        row_20,
        row_21,
        row_22,
        row_23,
        row_24,
        row_25,
        row_26,
        row_27,
        row_28,
        row_29,
        wall_row_bottom,
    ]
    return grid_array