from GameData.Keys.Keys import quit_game
from GameData.Constructor.Constructor import init


def main():
    game = init()
    playing = True
    pause = False
    while playing:
        input = game.user_input()
        if input:
            print(input)
        if input == quit_game:
            playing = False
            continue
        if input == "space":
            pause = not pause
        if pause:
            continue
        game.map.move_player(input)
        game.map.move_ghosts()
        game.check_interactions()
        game.draw_map()
        game.window.update_display()
        
main()