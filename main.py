from GameData.Keys.Keys import quit_game
from GameData.Constructor.Constructor import init
from GameData.Dependecies.Dependencies import time

def make_timer(name:str):
    timer = {"name": name,
             "start" : 0,
             "total" : 0}
    return timer

def start_time(timer:dict):
    start = time.time()
    timer["start"] = start
    return timer

def sum_time(segment:dict):
    new_total = time.time() - segment.get("start")
    segment["total"] += new_total
    return segment

def end_time(segment:dict):
    print(f"{segment.get("name")} took {segment.get("total")} seconds")
    segment["total"] = 0
    return segment

def main():
    game = init()
    playing = True
    pause = False
    player_timer = make_timer("Player timer")
    ghost_timer = make_timer("Ghost timer")
    collision_timer = make_timer("Collision timer")
    map_draw_timer = make_timer("Make Map timer")
    update_timer = make_timer("Update timer")
    total_run_timer = make_timer("Total run timer")
    loop_count = 0
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
        map_draw_timer = start_time(map_draw_timer)
        game.draw_map()
        map_draw_timer = sum_time(map_draw_timer)
        update_timer = start_time(update_timer)
        game.window.update_display()
        update_timer = sum_time(update_timer)
        
        loop_count += 1
        if loop_count % 240 == 0:
            loop_count = 1
            total_run_timer = sum_time(total_run_timer)
            print()
            total_run_timer = end_time(total_run_timer)
            map_draw_timer = end_time(map_draw_timer)
            update_timer = end_time(update_timer)

main()