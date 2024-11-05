from GameData.Objects.Vector2.Vector2 import Vector2

start_height = 900
start_width = 700

DEBUG = False

PI = 3.1415

ROWS = 36
COLUMNS = 28

HEIGHT = start_height - (start_height % ROWS)
WIDTH = start_width - (start_width % COLUMNS)

TILE_WIDTH = int(WIDTH / COLUMNS)
TILE_HEIGHT = int(HEIGHT / ROWS)

FPS = 120

CENTER = Vector2(int(WIDTH / 2), int(HEIGHT / 2))