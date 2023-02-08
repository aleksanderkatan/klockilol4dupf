from game_files.logic.layer import layer
from game_files.logic.player import player
from game_files.imports.charmap import charmap
from game_files.logic.state_filler.state_load_exception import state_load_exception
from game_files.logic.state_filler.option_maps import char_optionable_blocks
import game_files.imports.all_blocks as o


def fill_blocks(s, level):
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
                    block_class = charmap[char]     # get the constructor
                except KeyError:
                    raise state_load_exception(f"Unknown character [{char}] at position x={x_}, y={y_}, z={z_}.")

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
    return blocks
