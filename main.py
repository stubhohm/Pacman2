from GameData.Keys.Keys import quit_game
from GameData.Constructor.Constructor import init
from GameData.Objects.Vector2.Vector2 import Vector2
from GameData.Objects.Pacman.Pacman import Pacman
pacman = Pacman()
def main():
    game = init()
    playing = True
    while playing:
        input = game.user_input()
        if input:
            print(input)
        if input == quit_game:
            playing = False
            continue
        game.map.move_player(input)
        game.draw_map()
        game.window.update_display()

main()