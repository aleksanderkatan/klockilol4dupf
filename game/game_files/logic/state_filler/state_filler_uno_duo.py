import traceback
from game_files.imports.log import log
from game_files.logic.state_filler.state_load_exception import state_load_exception

from game_files.logic.state_filler.read_level_string import read_level_string
from game_files.logic.state_filler.linify_level_string import linify_level_string
from game_files.logic.state_filler.preprocess_level import preprocess_level
from game_files.logic.state_filler.fill_blocks import fill_blocks
from game_files.logic.state_filler.configure_options import configure_options
from game_files.logic.state_filler.find_starting_point import find_starting_point

import game_files.imports.globals as g


def fill(s, level_index, last_level_index=None):
    try:
        level_string = read_level_string(level_index)
        level_lines = linify_level_string(level_string)
        prepped_level = preprocess_level(level_lines)
        blocks = fill_blocks(s, prepped_level)
        configure_options(s, prepped_level.options, blocks)
        find_starting_point(s, last_level_index)
        return True
    except state_load_exception as error:
        log.error(f"An error occurred during filling level {level_index}")
        log.error(error)
        g.LAST_ERROR = f"Error in stage {level_index}: {error}"
    except Exception as e:
        log.error(f"Unknown exception occurred.")
        log.error(e)
        traceback.print_exc()
        g.LAST_ERROR = f"Unknown error in stage {level_index}."
    return False
