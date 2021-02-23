import pygame
import hashlib
import game_files.globals as g
import game_files.all_blocks as o
import game_files.all_sprites as s

# returns position on screen for certain index
def index_to_position(x, y, z, size_x, size_y, size_z):
    mid_x = g.WINDOW_X / 2
    mid_y = g.WINDOW_Y / 2
    high_left = (mid_x - size_x / 2 * g.BLOCK_SIZE, mid_y - size_y / 2 * g.BLOCK_SIZE)

    return high_left[0] + g.BLOCK_SIZE * x + (z - size_z / 2) * g.LAYER_X_OFFSET, high_left[1] + g.BLOCK_SIZE * y - (
            z - size_z / 2) * g.LAYER_Y_OFFSET


def key_to_direction(key):
    if key in [pygame.K_d, pygame.K_RIGHT]:
        return 0
    if key in [pygame.K_w, pygame.K_UP]:
        return 1
    if key in [pygame.K_a, pygame.K_LEFT]:
        return 2
    if key in [pygame.K_s, pygame.K_DOWN]:
        return 3
    return None


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
    if key == '>':
        return 0
    if key == '^':
        return 1
    if key == '<':
        return 2
    if key == 'v':
        return 3
    return None


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


def prevents_win(blo):
    if type(blo) in o.preventing_win:
        return True
    if type(blo) == o.block_lamp and not blo.on:
        return True
    return False

def background_of_level(level_index):
    level_set, level = level_index
    if level_set == 201 and level == 0:
        return s.sprites["kono_dio_da"]
    if level_set == 401 and level == 0:
        return s.sprites["swamp"]
    if g.DUDA_CHUJ:
        return s.sprites["duda_chuj"]
    return s.sprites["background"]

def hash_string(string):
    hasher = hashlib.sha256()
    hasher.update(bytes(string, "utf-16"))
    return hasher.digest()

