from game_files.imports.log import log
from game_files.logic.state_filler.option_maps import option_map
import game_files.imports.all_sprites as sprites
from game_files.other.chav import chav
from game_files.other.bomb import bomb
from game_files.other.decoration import decoration
from game_files.logic.state_filler.state_load_exception import state_load_exception


def configure_options(s, options, blocks):
    for key, value in blocks.items():
        if key in option_map:
            log.trace("Configuring: " + option_map[key])

            if option_map[key] not in options:
                raise state_load_exception("No " + option_map[key] + " options")

            current_options = options[option_map[key]]

            if len(current_options) < len(value):
                raise state_load_exception(f"Too few {option_map[key]} options, [{len(current_options)}] instead of [{len(value)}].")
            if len(current_options) > len(value):
                log.warning(f"Too many {option_map[key]} options, [{len(current_options)}] instead of [{len(value)}].")

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

