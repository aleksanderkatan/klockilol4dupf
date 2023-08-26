import src.imports.all_blocks as o
from src.imports.log import log


def _extract_forced_spawn(options):
    if 'forced_spawn' not in options:
        return None
    cords = options['forced_spawn'][0].split("/")
    return int(cords[0]), int(cords[1]), int(cords[2])


def find_starting_point(s, last_level_index, options, preset_spawn):
    # preset spawn has priority, then options spawn, then first exit, then first standable.
    if preset_spawn is not None:
        s.teleport_player(preset_spawn, False)
        return


    starting_point = s.find_level_entrance(last_level_index)
    forced_spawn = _extract_forced_spawn(options)

    if starting_point is None and forced_spawn is not None:
        starting_point = forced_spawn

    if starting_point is not None:
        s.teleport_player(starting_point, False)

    if type(s.get_block(s.player.pos)) not in o.standables:
        log.info("Player is not standing, finding a standable block...")
        for blo in s.block_iterator():
            typ = type(blo)
            if typ in o.standables and typ != o.block_invisible:
                s.teleport_player(blo.pos, False)
                break
