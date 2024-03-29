import traceback

import src.imports.globals as g
from src.imports.log import log
from src.logic.state_filler.configure_options import configure_options
from src.logic.state_filler.fill_blocks import fill_blocks
from src.logic.state_filler.find_starting_point import find_starting_point
from src.logic.state_filler.linify_level_string import linify_level_string
from src.logic.state_filler.preprocess_level import preprocess_level
from src.logic.state_filler.read_level_string import read_level_string
from src.logic.state_filler.state_load_exception import state_load_exception


def fill(s, level_index, last_level_index=None, preset_spawn=None):
    try:
        level_string = read_level_string(level_index)
        level_lines = linify_level_string(level_string)
        prepped_level = preprocess_level(level_lines)
        blocks = fill_blocks(s, prepped_level)
        options = prepped_level.options
        configure_options(s, options, blocks)
        find_starting_point(s, last_level_index, options, preset_spawn)
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
