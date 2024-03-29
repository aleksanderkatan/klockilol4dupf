import hashlib

import pygame

from src.imports.log import log
from src.imports.view_constants import global_view_constants as v
from src.logic.direction import direction as d


# returns position on screen for certain index
def index_to_position(x, y, z, size_x, size_y, size_z, middle=False):
    mid_x = v.WINDOW_X / 2
    mid_y = v.WINDOW_Y / 2
    high_left = (mid_x - size_x / 2 * v.BLOCK_X_SIZE, mid_y - size_y / 2 * v.BLOCK_Y_SIZE)

    size_z = size_z - 1
    x, y = high_left[0] + v.BLOCK_X_SIZE * x + (z - size_z / 2) * v.LAYER_X_OFFSET, \
           high_left[1] + v.BLOCK_Y_SIZE * y - (z - size_z / 2) * v.LAYER_Y_OFFSET

    if middle:
        return x + v.BLOCK_X_SIZE // 2, y + v.BLOCK_Y_SIZE // 2
    return x, y


def out_of_range_3(pos, pos_max):
    for i in range(3):
        if not 0 <= pos[i] < pos_max[i]:
            return True
    return False


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
        if player_z - v.VISIBLE_LAYERS_DOWN <= layer_z <= player_z:
            return layer_z - player_z
    elif layer_z > player_z:
        if player_z <= layer_z <= player_z + v.VISIBLE_LAYERS_UP:
            return layer_z - player_z
    else:
        return 0


def char_to_direction(key):
    if key in ['>', ']']:
        return d.RIGHT
    if key in ['^', '-']:
        return d.UP
    if key in ['<', '[']:
        return d.LEFT
    if key in ['v', '_']:
        return d.DOWN
    return d.NONE


def reverse_direction(direction):
    if direction == d.LEFT:
        return d.RIGHT
    if direction == d.UP:
        return d.DOWN
    if direction == d.RIGHT:
        return d.LEFT
    if direction == d.DOWN:
        return d.UP
    return d.NONE  # direction may not be in [4]


def new_single_layer(current_single_layer, key, total_layers):
    if total_layers == 1:
        return None

    new_single_layer_index = -2137
    for i in range(1, total_layers + 1):
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

    if direction == d.NONE:
        return pos
    else:
        if direction == d.RIGHT:
            x += move_length
        elif direction == d.UP:
            y -= move_length
        elif direction == d.LEFT:
            x -= move_length
        elif direction == d.DOWN:
            y += move_length
        elif direction == d.ASCEND:
            z += move_length
        elif direction == d.DESCEND:
            z -= move_length
        elif direction == d.FORCED_SKIP:
            log.trace("Forced move skip")

    return x, y, z


def extend(number, length):
    if len(str(number)) >= length:
        return str(number)
    ans = ""
    for i in range(length):
        ans += str((number % pow(10, length - i)) // pow(10, length - i - 1))
    return ans


def ticks_to_time(ticks):
    milliseconds = int(ticks * (1 / v.FRAME_RATE) * 1000)
    seconds = milliseconds // 1000
    milliseconds %= 1000
    minutes = seconds // 60
    seconds %= 60
    hours = minutes // 60
    minutes %= 60

    ans = f"{extend(hours, 2)}:{extend(minutes, 2)}:{extend(seconds, 2)}:{extend(milliseconds, 3)}"
    return ans


def check_if_int(x, min_val=None, max_val=None):
    try:
        val = int(x)
    except ValueError:
        return False
    if min_val is None:
        min_val = val
    if max_val is None:
        max_val = val
    return min_val <= val <= max_val


def get_translation(pos1, pos2):
    return pos2[0] - pos1[0], pos2[1] - pos1[1], pos2[2] - pos1[2]
