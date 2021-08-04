import pygame
import sys
from game_files.imports.log import log
import game_files.imports.levels as l
import game_files.imports.globals as g
import game_files.imports.utils as u
from game_files.imports.save_state import global_save_state
from game_files.imports.view_constants import global_view_constants as v


public_commands = {}

def command_reset_all(game_logic, command):
    log.warning("Eradicating save file")
    global_save_state.reset()
    game_logic.level_index = None
    game_logic.set_stage((400, 1))

def command_quit(game_logic, command):
    log.info("Quitting")
    pygame.quit()
    sys.exit(0)

def command_switch_timer(game_logic, command):
    log.info("Switching timer")
    g.TIMER = not g.TIMER

def command_switch_witch(game_logic, command):
    log.info("Switching witch")
    g.WITCH = not g.WITCH

def command_help_public(game_logic, command):
    message = "Public commands:\n"
    message += u.list_of_commands(public_commands)
    log.print(message)

def command_completion(game_logic, command):
    message = "Completion: "
    message += str(global_save_state.get_completion())
    log.print(message)

def command_enable_cheats(game_logic, command):
    if g.CHEATS:
        log.info("Cheats already enabled")
        return
    log.info("Attempting to enable cheats")
    if len(command) != 2:
        log.info("No password given")
        return
    pw_hash = u.hash_string(command[1].upper())
    if pw_hash != g.PASSWORD_HASH:
        log.info("WRONG PASSWORD!")
    else:
        log.info("Cheats enabled")
        g.CHEATS = True


public_commands["reset_all"] = command_reset_all

public_commands["q"] = command_quit
public_commands["exit"] = command_quit
public_commands["quit"] = command_quit
public_commands["poweroff"] = command_quit
public_commands["shutdown"] = command_quit
public_commands["halt"] = command_quit

public_commands["timer"] = command_switch_timer

public_commands["witch"] = command_switch_witch

public_commands["help"] = command_help_public

public_commands["completion"] = command_completion

public_commands["enable_cheats"] = command_enable_cheats


# second section

root_commands = {}

def command_lv(game_logic, command):
    if len(command) == 2:
        log.info("Changing level to: 0 " + command[1])
        game_logic.set_stage((0, int(command[1])))
    else:
        log.info("Changing level to: " + command[1] + " " + command[2])
        game_logic.set_stage((int(command[1]), int(command[2])))

def command_previous(game_logic, command):
    log.info("Previous level")
    game_logic.set_stage(l.previous_level(game_logic.stage.level_index))

def command_next(game_logic, command):
    log.info("Completing current level")
    game_logic.complete()

def command_duda_chuj(game_logic, command):
    log.info("Swapping background")
    g.DUDA_CHUJ = not g.DUDA_CHUJ

def command_y_offset(game_logic, command):
    log.info("Changing y offset")
    v.LAYER_Y_OFFSET = int(command[1])

def command_x_offset(game_logic, command):
    log.info("Changing x offset")
    v.LAYER_X_OFFSET = int(command[1])

def command_reset_timer(game_logic, command):
    log.info("Resetting timer")
    global_save_state.reset_timer()

def command_reset_events(game_logic, command):
    log.info("Resetting events")
    global_save_state.reset_events()

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
    log.print(message)

def command_help_root(game_logic, command):
    message = "Public commands:\n"
    message += u.list_of_commands(public_commands)
    message += "\nRoot commands:\n"
    message += u.list_of_commands(root_commands)
    log.print(message)

def command_disable_cheats(game_logic, command):
    log.info("Disabling cheats")
    g.CHEATS = False

def command_position(game_logic, command):
    pos = game_logic.stage.latest_state().player.pos
    log.print("Player position: " + str(pos) + ", level: " + str(game_logic.stage.level_index))


root_commands["lv"] = command_lv
root_commands["cd"] = command_lv

root_commands["p"] = command_previous
root_commands["previous"] = command_previous

root_commands["n"] = command_next
root_commands["c"] = command_next
root_commands["next"] = command_next
root_commands["complete"] = command_next

root_commands["duda"] = command_duda_chuj
root_commands["duda_chuj"] = command_duda_chuj

root_commands["yoffset"] = command_y_offset
root_commands["y_offset"] = command_y_offset

root_commands["xoffset"] = command_x_offset
root_commands["x_offset"] = command_x_offset

root_commands["reset_timer"] = command_reset_timer

root_commands["reset_events"] = command_reset_events

root_commands["complete_all"] = command_complete_all

root_commands["r"] = command_refresh
root_commands["refresh"] = command_refresh
root_commands["reset"] = command_refresh

root_commands["load_all"] = command_load_all

root_commands["ls"] = command_ls
root_commands["list"] = command_ls

root_commands["help"] = command_help_root

root_commands["disable_cheats"] = command_disable_cheats
root_commands["dc"] = command_disable_cheats

root_commands["pos"] = command_position
root_commands["position"] = command_position
