from GameData.Objects.Tile.TileTypes import Tile, Wall, Path, Node
from GameData.Objects.Map.Map import Map
from GameData.Objects.Dot.PowerUp import PowerUp, Dot

tile = Tile()
wall = Wall()
path = Path()
node = Node()
test_x = [tile, wall, path, node]
test_y = [test_x, test_x, test_x, test_x]
map_grid = test_y



power_dot = PowerUp()
content = power_dot.eat()

print(content)

dot = Dot()
content = dot.eat()

print(content)

test_map = Map()
test_map.set_grid(map_grid)