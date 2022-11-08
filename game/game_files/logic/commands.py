import pygame
import sys
import os
from game_files.imports.log import log
import game_files.imports.levels as l
import game_files.imports.globals as g
import game_files.imports.utils as u
from game_files.imports.save_state import global_save_state, completed_levels
from game_files.imports.view_constants import global_view_constants as v
from game_files.imports.platform_maze_passwords import passwords
from game_files.imports.all_speedruns import speedruns
from game_files.speedruns.settings import settings as speedrun_settings

public_commands = {}


def command_reset_all(game_logic, command):
    log.warning("Eradicating save file")
    global_save_state.hard_erase_all()
    game_logic.level_index = None
    game_logic.set_stage((400, 1))


def command_quit(game_logic, command):
    log.info("Quitting")
    exit_game()


def command_switch_timer(game_logic, command):
    log.info("Switching timer")
    g.TIMER = not g.TIMER


def command_switch_witch(game_logic, command):
    log.info("Switching witch")
    g.WITCH = not g.WITCH


def command_help_public(game_logic, command):
    message = "Public commands:\n"
    message += list_of_commands(public_commands)
    log.write(message)


def command_completion(game_logic, command):
    message = "Completion: "
    message += str(global_save_state.get_completion())
    log.write(message)


def command_logged_keys(game_logic, command):
    message = global_save_state.get_logged_keys()
    log.write(message)


def command_password(game_logic, command):
    if command[1] in passwords:
        level = passwords[command[1]]
        log.info(f"Changing level to: 209, {level}")
        game_logic.set_stage((209, level))
    else:
        log.error("Incorrect password!")


def command_speedrun(game_logic, command):
    if len(command) < 2:
        log.error("Enter name of a speedrun")
        return

    command, options = extract_options(command)
    name = (' '.join(command[1:])).lower()
    if name not in speedruns:
        log.error("No such speedrun")
        return

    settings = speedrun_settings(does_death_reset=("-d" not in options))
    speedrun = speedruns[name](settings)
    log.write(f"Starting speedrun {speedrun.get_name()}")
    g.TIMER = True
    g.CHEATS = False
    global_save_state.hard_erase_all()
    stage, pos = speedrun.get_starting_stage_and_pos()
    game_logic.set_stage((1, 1))
    game_logic.set_stage(stage)
    game_logic.stage.latest_state().teleport_player(pos, activate_step_in=False)
    game_logic.speedrun = speedrun


def command_shrek(game_logic, command):
    global_save_state.hard_save("shrek", True)


def command_enable_cheats(game_logic, command):
    if g.CHEATS:
        log.info("Cheats already enabled\nIf you want to disable them, use another command")
        return
    log.info("Attempting to enable cheats")
    if len(command) != 2:
        log.info("No password given")
        return
    pw_hash = u.hash_string(command[1].upper())
    if pw_hash != g.PASSWORD_HASH:
        log.info("WRONG PASSWORD!")
    else:
        g.CHEATS = True
        game_logic.speedrun = None
        log.info("Cheats enabled. If there was a speedrun running, it is now erased.")


public_commands["reset_all"] = command_reset_all

public_commands["q"] = command_quit
public_commands["exit"] = command_quit
public_commands["quit"] = command_quit
public_commands["poweroff"] = command_quit
public_commands["power-off"] = command_quit
public_commands["shutdown"] = command_quit
public_commands["halt"] = command_quit

public_commands["timer"] = command_switch_timer

public_commands["witch"] = command_switch_witch

public_commands["help"] = command_help_public

public_commands["completion"] = command_completion

public_commands["logged_keys"] = command_logged_keys
public_commands["lk"] = command_logged_keys

public_commands["password"] = command_password

public_commands["speed_run"] = command_speedrun
public_commands["speedrun"] = command_speedrun
public_commands["sr"] = command_speedrun
public_commands["s"] = command_speedrun

public_commands["shrek"] = command_shrek

public_commands["enable_cheats"] = command_enable_cheats
public_commands["ec"] = command_enable_cheats

# second section (root needed)

root_commands = {}


def command_lv(game_logic, command):
    for arg in command[1:]:
        if not u.check_if_int(arg):
            log.error("Arguments not integer")
            return
    if len(command) == 2:
        log.info("Changing level to: 0 " + command[1])
        game_logic.set_stage((0, int(command[1])))
    elif len(command) == 3:
        log.info("Changing level to: " + command[1] + " " + command[2])
        game_logic.set_stage((int(command[1]), int(command[2])))


def command_previous(game_logic, command):
    log.info("Previous level")
    level_index = game_logic.stage.level_index
    prev_index = l.previous_level(level_index)
    game_logic.set_stage(prev_index)


def command_next(game_logic, command):
    log.info("Next level")
    level_index = game_logic.stage.level_index
    next_index = l.next_level(level_index)
    if level_index[1] != 0:
        log.info("Completing current level")
        game_logic.complete()
    else:
        log.info("Jumping to", next_index)
        game_logic.set_stage(next_index)


def command_swap(game_logic, command):  # !! I don't like this command, but it's useful
    log.info("Swapping current level")
    if len(command) < 2 or command[1] not in ["next", "prev"]:
        log.error("Usage: \"swap next\" or \"swap prev\"")
        return

    mode = 1 if command[1] == "prev" else 0

    level_index = game_logic.level_index

    if mode == 1:
        if level_index[1] > 1:
            other = (level_index[0], level_index[1] - 1)
        else:
            log.error("No previous level!")
            return
    else:
        if level_index[1] < l.levs[level_index[0]]:
            other = (level_index[0], level_index[1] + 1)
        else:
            log.error("No next level!")
            return

    log.info("Swapping levels:", level_index, other)
    swap_levels(level_index, other)

    if mode == 1:
        execute_command(game_logic, "p")
    else:
        execute_command(game_logic, "c")


def command_2137(game_logic, command):
    log.info("Swapping background")
    g.PAPOR = not g.PAPOR


def command_y_offset(game_logic, command):
    log.info("Changing y offset")
    v.LAYER_Y_OFFSET = int(command[1])


def command_x_offset(game_logic, command):
    log.info("Changing x offset")
    v.LAYER_X_OFFSET = int(command[1])


def command_reset_timer(game_logic, command):
    log.info("Resetting timer")
    global_save_state.hard_save("time", 0)


def command_reset_events(game_logic, command):
    log.info("Resetting events")
    global_save_state.hard_save("events", set())


def command_reset_completed(game_logic, command):
    log.info("Resetting completed levels")
    global_save_state.hard_save("completed", completed_levels())


def command_complete_zone(game_logic, command):
    for arg in command[1:]:
        if not u.check_if_int(arg):
            log.error("Argument not integer")
            return
        log.info("Completing zone", arg)
        global_save_state.complete_zone(int(arg), True)


def command_complete_all(game_logic, command):
    log.info("Completing all levels")
    global_save_state.complete_all()


def command_refresh(game_logic, command):
    log.info("Resetting and refreshing current level")
    game_logic.set_stage(game_logic.level_index)


def command_load_all(game_logic, command):
    old_level_index = game_logic.level_index
    old_stage = game_logic.stage
    problems = []
    for level_index in l.all_levels_iterator():
        if not game_logic.set_stage(level_index):
            problems.append(level_index)
    game_logic.stage = old_stage
    game_logic.level_index = old_level_index
    if len(problems) > 0:
        log.error("Errors in stages: " + str(problems))
    else:
        log.info("No errors!")


def command_ls(game_logic, command):
    message = l.levels_ls()
    log.write(message)


def command_help_root(game_logic, command):
    message = "Public commands:\n"
    message += list_of_commands(public_commands)
    message += "\nRoot commands:\n"
    message += list_of_commands(root_commands)
    log.write(message)


def command_disable_cheats(game_logic, command):
    log.info("Disabling cheats")
    g.CHEATS = False


def command_position(game_logic, command):
    pos = game_logic.stage.latest_state().player.pos
    log.write("Player position: " + str(pos) + ", level: " + str(game_logic.stage.level_index))


def command_raise_exception(game_logic, command):
    log.info("Raising runtime exception")
    raise RuntimeError


def command_teleport(game_logic, command):
    if command[1] == "up":
        return command_teleport_up(game_logic, ["up"])
    if len(command) != 4:
        log.error("Wrong command length")
        return
    for arg in command[1:]:
        if not u.check_if_int(arg):
            log.error("Arguments not integer")
            return
    state = game_logic.stage.latest_state()
    state.teleport_player((int(command[1]), int(command[2]), int(command[3])), False)


def command_teleport_up(game_logic, command):
    amount = 1 if len(command) == 1 else int(command[1])

    state = game_logic.stage.latest_state()
    x, y, z = state.player.pos
    z += amount
    state.teleport_player((x, y, z), False)
    return


def command_all_stats(game_logic, command):
    message = global_save_state.get_all_stats()
    log.write(message)


def command_resume_timer(game_logic, command):
    log.info("Resuming timer")
    global_save_state.hard_save("is_timer_stopped", False)


def command_stop_timer(game_logic, command):
    log.info("Stopping timer")
    global_save_state.hard_save("is_timer_stopped", True)


root_commands["lv"] = command_lv
root_commands["cd"] = command_lv

root_commands["p"] = command_previous
root_commands["previous"] = command_previous

root_commands["swap"] = command_swap

root_commands["n"] = command_next
root_commands["c"] = command_next
root_commands["next"] = command_next
root_commands["complete"] = command_next

root_commands["2137"] = command_2137
root_commands["21:37"] = command_2137
root_commands["jp2gmd"] = command_2137

root_commands["yoffset"] = command_y_offset
root_commands["y_offset"] = command_y_offset

root_commands["xoffset"] = command_x_offset
root_commands["x_offset"] = command_x_offset

root_commands["reset_timer"] = command_reset_timer

root_commands["reset_events"] = command_reset_events

root_commands["reset_completed"] = command_reset_completed

root_commands["complete_zone"] = command_complete_zone
root_commands["cz"] = command_complete_zone

root_commands["complete_all"] = command_complete_all
root_commands["ca"] = command_complete_all

root_commands["r"] = command_refresh
root_commands["refresh"] = command_refresh
root_commands["reset"] = command_refresh

root_commands["load_all"] = command_load_all
root_commands["la"] = command_load_all

root_commands["ls"] = command_ls
root_commands["list"] = command_ls

root_commands["help"] = command_help_root

root_commands["disable_cheats"] = command_disable_cheats
root_commands["dc"] = command_disable_cheats

root_commands["pos"] = command_position
root_commands["position"] = command_position

root_commands["raise_exception"] = command_raise_exception
root_commands["runtime_exception"] = command_raise_exception
root_commands["re"] = command_raise_exception

root_commands["teleport"] = command_teleport
root_commands["tp"] = command_teleport

root_commands["up"] = command_teleport_up

root_commands["all_stats"] = command_all_stats
root_commands["as"] = command_all_stats

root_commands["resume_timer"] = command_resume_timer

root_commands["stop_timer"] = command_stop_timer


# helpful functions

def extract_options(command):
    options = set()
    rest = []

    for word in command:
        if word[0] == '-':
            options.add(word)
        else:
            rest.append(word)
    return rest, options


def exit_game():
    # called: quit command entered, window closed by x, process killed from manager (SIGKILL?)
    # not called: exception was raised (game works in one thread), stop button in pycharm (SIGTERM?), exited from launcher
    # do those signals even exist on Windows?
    # does my game even work on Linux?
    # who are we? where are we going

    log.info("Saving before exiting")
    global_save_state.hard_save_all()
    log.info("Exiting gracefully")
    pygame.quit()
    sys.exit(0)


def list_of_commands(commands):
    assert type(commands) is dict
    d = {}
    for command, function in commands.items():
        if function not in d:
            d[function] = []
        d[function].append(command)
    ans = ""
    for function, commands in d.items():
        for command in commands:
            ans += command
            ans += ", "
        ans = ans[:-2]
        if function == command_speedrun:
            ans += "\tWARNING: this command wipes your savefile!"
        ans += "\n"

    return ans


def swap_levels(level_1, level_2):  # !! performs no checks
    def level_path(level):
        return "game_files/levels/" + str(level[0]) + "/" + str(level[1]) + ".lv"

    temp_path = "game_files/levels/temp/0.lv"
    path_1 = level_path(level_1)
    path_2 = level_path(level_2)
    os.rename(path_1, temp_path)
    os.rename(path_2, path_1)
    os.rename(temp_path, path_2)


def execute_command(game_logic, command):
    if command == '':
        return

    command = [word.lower() for word in command.strip().split(' ')]

    if not g.CHEATS:
        if command[0] in public_commands:
            log.info("executing: " + command[0])
            public_commands[command[0]](game_logic, command)
        else:
            log.info("No such command. For list of available commands type \"help\"")
    else:
        if command[0] in root_commands:
            root_commands[command[0]](game_logic, command)
        elif command[0] in public_commands:
            public_commands[command[0]](game_logic, command)  # intentional, command overloading
        else:
            log.info("No such command. For list of available commands type \"help\"")
