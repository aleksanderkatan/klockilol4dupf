import pygame
import game_files.globals as g
import game_files.all_blocks as o
import game_files.all_sprites as s

# returns position on screen for certain index
def index_to_position(x, y, z, size_x, size_y, size_z):
    midx = g.WINDOW_X / 2
    midy = g.WINDOW_Y / 2
    highleft = (midx - size_x / 2 * g.BLOCK_SIZE, midy - size_y / 2 * g.BLOCK_SIZE)

    return highleft[0] + g.BLOCK_SIZE * x + (z - size_z / 2) * g.LAYER_X_OFFSET, highleft[1] + g.BLOCK_SIZE * y - (
            z - size_z / 2) * g.LAYER_Y_OFFSET


def key_to_direction(key):
    if key == pygame.K_d:
        return 0
    if key == pygame.K_w:
        return 1
    if key == pygame.K_a:
        return 2
    if key == pygame.K_s:
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


def new_single_layer(current_single_layer, key):
    new_single_layer_index = -2137
    for i in range(1, 10):
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
    if g.DUDA_CHUJ:
        return s.sprites["duda_chuj"]
    return s.sprites["background"]
