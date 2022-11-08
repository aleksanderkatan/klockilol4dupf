from game_files.imports.log import log
import game_files.imports.all_blocks as o


def find_starting_point(s, last_level_index):
    starting_point = s.find_level_entrance(last_level_index)
    if starting_point is not None:
        s.teleport_player(starting_point, False)

    if type(s.get_block(s.player.pos)) not in o.standables:
        log.trace("Player is not standing, finding a standable block...")
        for blo in s.block_iterator():
            typ = type(blo)
            if typ in o.standables and typ != o.block_invisible:
                s.teleport_player(blo.pos, False)
                break
