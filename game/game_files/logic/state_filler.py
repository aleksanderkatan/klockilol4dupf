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


def _preprocess_level(level_index):
    path = l.level_path(level_index)
    if not os.path.exists(path):
        log.error("No such file " + path)
        return None

    with open(path) as f:
        level = f.read().split('\n')

    level_filtered = []
    for line in level:
        if len(line) > 0 and line[0] == '#':
            continue
        level_filtered.append(line)

    if level_filtered[-1] != "":
        level_filtered.append("")

    return level_filtered


def _fill(s, level, last_level_index):
    try:
        ite = iter(level)

        s.x = int(next(ite))
        s.y = int(next(ite))
        s.z = int(next(ite))
        s.player = player((0, 0, 0), s.screen, s.stage, s.state_index)

        blocks = {}

        for i in range(s.z):
            new_layer = layer(s.x, s.y, s.screen, s.stage, s.state_index)

            for j in range(s.y):
                line = next(ite)
                while line[-1] in ['\n', ' ']:
                    line = line[:-1]
                if len(line) != s.x:
                    log.error("Missing or excessive chars in level file")
                    return False

                for k in range(s.x):
                    char = line[k]
                    try:
                        obj = charmap[char]
                    except KeyError:
                        log.error("Key error: " + str(char))
                        return False

                    blo = obj(s.screen, s.stage, s.state_index, (k, j, i))

                    if issubclass(obj, o.block_start):
                        s.teleport_player((k, j, i), False)
                    if issubclass(obj, o.block_numeric):
                        blo.options(str(char))
                    if issubclass(obj, o.block_arrow):
                        blo.options(str(char))
                    if issubclass(obj, o.block_birdy_arrow):
                        blo.options(str(char))
                    if issubclass(obj, o.block_jump):
                        blo.options(2)
                    if issubclass(obj, o.block_numeric_dark):
                        blo.options(str(char))
                    if issubclass(obj, o.block_lamp):
                        if char == 'B':
                            blo.change_state()
                    if issubclass(obj, o.block_swapping):
                        blo.options(str(char))

                    if obj not in blocks:
                        blocks[obj] = []
                    blocks[obj].append(blo)

                    new_layer.update(k, j, blo)

            s.layers.append(new_layer)
            next(ite)

        options = {}

        try:
            while True:
                line = next(ite)
                if len(line) < 2:
                    break
                line = line.split()
                if line[0] not in options:
                    options[line[0]] = []
                options[line[0]].extend(line[1:])
        except StopIteration:
            pass

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
                    for i in range(len(value)):
                        value[i].options(str(i) + " " + current_options[i])
                else:
                    for i in range(len(value)):
                        value[i].options(current_options[i])

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
        return True
    except:
        log.error("Undefined error while loading stage\n")
        traceback.print_exc()
        return False


def fill(s, level_index, last_level_index=None):
    preprocessed_level = _preprocess_level(level_index)
    if preprocessed_level is None:
        return False
    return _fill(s, preprocessed_level, last_level_index)
