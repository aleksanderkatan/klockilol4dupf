import traceback
import os
from game_files.imports.log import log
from game_files.logic.layer import layer
from game_files.other.bomb import bomb
from game_files.logic.player import player
from game_files.imports.charmap import charmap
from game_files.other.chav import chav
import game_files.imports.all_blocks as o
import game_files.imports.levels as l
import game_files.imports.all_sprites as sprites
from game_files.other.decoration import decoration


class state_load_exception(BaseException):
    pass


def _read_level_string(level_index):
    path = l.level_path(level_index)
    if not os.path.exists(path):
        raise state_load_exception("No such file! Check the level index.")
    with open(path) as f:
        return f.read() + "\n"


def _linify_level(level_string):
    level_lines = level_string.split("\n")
    commentless_lines = [(0, "")]
    for index, line in enumerate(level_lines):
        pos = line.find("#")
        if pos != -1:
            line = line[:pos]
        if pos != 0:
            commentless_lines.append((index+1, line.strip()))
    return commentless_lines


class preprocessed_level:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.t = [[[0 for _ in range(z)] for _ in range(y)] for _ in range(x)]
        self.options = {}


option_map = {
    o.block_portal: 'portals',
    o.block_jump: 'jumps',
    o.block_entrance: 'entrances',
    o.block_map_bridge: 'map_bridges',
    o.block_ones: 'ones',
    o.block_piston: 'pistons',
    o.block_dual_arrow: 'dual_arrows',
    o.block_moving_arrow: 'moving_arrows',
    o.block_entrance_random: 'entrances_random',
    o.block_pm_arrow: 'pm_arrows',
    o.block_pm_numeric: 'pm_numeric',
    o.block_pm_control_switcher: 'pm_control_switchers',
}

valid_options = {value for value in option_map.values()}
valid_options.add("chavs")
valid_options.add("bombs")
valid_options.add("decorations")


def _preprocess_level(level_lines):
    try:
        x = int(level_lines[1][1])
        y = int(level_lines[2][1])
        z = int(level_lines[3][1])
    except IndexError | ValueError:
        raise state_load_exception("Levels are expected to have 3 dimensions in first three lines.")
    level = preprocessed_level(x, y, z)

    for z_ in range(z):
        for y_ in range(y):
            line_index = 4 + z_ * (y + 1) + y_
            index, line = level_lines[line_index]
            if len(line) != x:
                raise state_load_exception(f"Line index {index} [{line}] has incorrect size {len(line)} instead of {x}.")

            for x_ in range(x):
                level.t[x_][y_][z_] = line[x_]
        line_index = 4 + z_ * (y + 1) + y
        index, line = level_lines[line_index]
        if len(line) != 0:
            raise state_load_exception(f"Line index {index} [{line}] should be empty")

    options_lines = level_lines[4 + z * (y + 1):]
    options = {}

    for index, line in options_lines:
        words = line.split()
        if len(line) == 0:
            continue
        opt = words[0]
        if opt not in valid_options:
            raise state_load_exception(f"Line index {index} [{line}] has an invalid option {opt}. Check spelling.")
        if opt not in options:
            options[opt] = []
        options[opt].extend(words[1:])

    level.options = options
    return level


char_optionable_blocks = {
    o.block_numeric,
    o.block_arrow,
    o.block_birdy_arrow,
    o.block_lamp,
    o.block_swapping,
}


def _fill_blocks(s, level, last_level_index):
    x = s.x = level.x
    y = s.y = level.y
    z = s.z = level.z
    s.player = player((0, 0, 0), s.screen, s.stage, s.state_index)

    blocks = {}

    for z_ in range(z):
        new_layer = layer(x, y, s.screen, s.stage, s.state_index)

        for y_ in range(y):
            for x_ in range(x):
                char = level.t[x_][y_][z_]
                try:
                    block_class = charmap[char]
                except KeyError:
                    raise state_load_exception(f"Unknown character [{char}] at position x={x}, y={y}, z={z}")

                blo = block_class(s.screen, s.stage, s.state_index, (x_, y_, z_))

                for optionable in char_optionable_blocks:
                    if issubclass(block_class, optionable):
                        blo.options(str(char))

                if issubclass(block_class, o.block_start):
                    s.teleport_player((x_, y_, z_), False)

                if block_class not in blocks:
                    blocks[block_class] = []
                blocks[block_class].append(blo)

                new_layer.update(x_, y_, blo)

        s.layers.append(new_layer)

    options = level.options

    for key, value in blocks.items():
        if key in option_map:
            log.info("Configuring: " + option_map[key])

            if option_map[key] not in options:
                log.warning("No " + option_map[key] + " options")
                continue

            current_options = options[option_map[key]]

            if len(current_options) != len(value):
                log.warning("Wrong length " + option_map[key] + " options")

            if option_map[key] == 'portals':
                for z_ in range(len(value)):
                    value[z_].options(str(z_) + " " + current_options[z_])
            else:
                for z_ in range(len(value)):
                    value[z_].options(current_options[z_])

    s.chavs = []
    if 'chavs' in options:
        for option in options['chavs']:
            pos = option.split('/')
            x = int(pos[0])
            y = int(pos[1])
            z = int(pos[2])
            s.chavs.append(chav(s.screen, s.stage, s.state_index, (x, y, z)))

    s.bombs = []
    if 'bombs' in options:
        for option in options['bombs']:
            option = option.split('/')
            x = int(option[0])
            y = int(option[1])
            z = int(option[2])
            ticks = int(option[3])
            s.bombs.append(bomb(s.screen, s.stage, s.state_index, (x, y, z), ticks))

    s.decorations = []
    if 'decorations' in options:
        for option in options['decorations']:
            option = option.split('/')  # 0/3/3/decoration_1x2_tree/mid/low
            x = float(option[0])
            y = float(option[1])
            z = float(option[2])
            sprite = sprites.sprites[option[3]]
            h_align = option[4]
            v_align = option[5]
            s.decorations.append(decoration(s.screen, s.stage, s.state_index, (x, y, z), sprite, h_align, v_align))

    starting_point = s.find_level_entrance(last_level_index)
    if starting_point is not None:
        s.teleport_player(starting_point, False)

    if type(s.get_block(s.player.pos)) not in o.standables:
        log.warning("Player is not standing, finding nearest standable...")
        for blo in s.block_iterator():
            typ = type(blo)
            if typ in o.standables and typ != o.block_invisible:
                s.teleport_player(blo.pos, False)
                break


def fill(s, level_index, last_level_index=None):
    try:
        level_string = _read_level_string(level_index)
        level_lines = _linify_level(level_string)
        prepped_level = _preprocess_level(level_lines)
        _fill_blocks(s, prepped_level, last_level_index)
        return True
    except state_load_exception as error:
        log.error(f"An error occurred during filling level {level_index}")
        log.error(error)
    except Exception as e:
        log.error(f"Unknown exception occurred.")
        log.error(e)
        traceback.print_exc()
    return False
