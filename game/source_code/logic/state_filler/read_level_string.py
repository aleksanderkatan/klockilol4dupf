import os

import source_code.imports.levels as l
from source_code.logic.state_filler.state_load_exception import state_load_exception


def read_level_string(level_index):
    path = l.level_path(level_index)
    if not os.path.exists(path):
        raise state_load_exception("No such file! Check the level index.")
    with open(path) as f:
        return f.read() + "\n"
