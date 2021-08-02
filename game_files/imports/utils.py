import pygame
import hashlib
import game_files.imports.globals as g
from game_files.imports.log import log
from game_files.imports.view_constants import global_view_constants as v

# returns position on screen for certain index
def index_to_position(x, y, z, size_x, size_y, size_z):
    mid_x = v.WINDOW_X / 2
    mid_y = v.WINDOW_Y / 2
    high_left = (mid_x - size_x / 2 * v.BLOCK_X_SIZE, mid_y - size_y / 2 * v.BLOCK_Y_SIZE)

    return high_left[0] + v.BLOCK_X_SIZE * x + (z - size_z / 2) * v.LAYER_X_OFFSET, high_left[1] + v.BLOCK_Y_SIZE * y - (
            z - size_z / 2) * v.LAYER_Y_OFFSET


def out_of_range(x, y, x_max, y_max):
    if x < 0:
        return True
    if y < 0:
        return True
    if x >= x_max:
        return True
    if y >= y_max:
        return True
    return False


def relative_to_player(layer_z, player_z):
    if layer_z < player_z:
        if player_z - g.VISIBLE_LAYERS_DOWN <= layer_z <= player_z:
            return layer_z - player_z
    elif layer_z > player_z:
        if player_z <= layer_z <= player_z + g.VISIBLE_LAYERS_UP:
            return layer_z - player_z
    else:
        return 0

    return None


def char_to_direction(key):
    if key in ['>', ']']:
        return 0
    if key in ['^', '-']:
        return 1
    if key in ['<', '[']:
        return 2
    if key in ['v', '_']:
        return 3
    return None

def reverse_direction(direction):
    if direction == 0:
        return 2
    if direction == 1:
        return 3
    if direction == 2:
        return 0
    if direction == 3:
        return 1
    return None     # direction may not be in [4]

def new_single_layer(current_single_layer, key, total_layers):
    new_single_layer_index = -2137
    for i in range(1, total_layers+1):
        if pygame.key.name(key) == str(i):
            new_single_layer_index = i - 1
    if new_single_layer_index == -2137:
        return current_single_layer

    ans = None
    if current_single_layer != new_single_layer_index:
        ans = new_single_layer_index
    return ans

def hash_string(string):
    hasher = hashlib.sha256()
    hasher.update(bytes(string, "utf-16"))
    return hasher.digest()

def move_pos(pos, direction, move_length=1):
    x, y, z = pos

    if direction is None:
        log.warning("Moving in None direction")
        return pos
    if direction == 5:
        return pos
    else:
        if direction == 0:
            x += move_length
        elif direction == 1:
            y -= move_length
        elif direction == 2:
            x -= move_length
        elif direction == 3:
            y += move_length
        else:
            z -= 1

    return x, y, z

def extend(number, length):
    if len(str(number)) >= length:
        return str(number)
    ans = ""
    for i in range(length):
        ans += str((number % pow(10, length-i))//pow(10, length-i-1))
    return ans


def ticks_to_time(ticks):
    milliseconds = int(ticks * (1/g.FRAMERATE) * 1000)
    seconds = milliseconds // 1000
    milliseconds %= 1000
    minutes = seconds // 60
    seconds %= 60
    hours = minutes // 60
    minutes %= 60

    ans = extend(hours, 2) + ":" + extend(minutes, 2) + ":" + extend(seconds, 2) + ":" + extend(milliseconds, 3)
    return ans


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
        ans += "\n"
    return ans

