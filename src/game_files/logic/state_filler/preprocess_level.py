from game_files.logic.state_filler.option_maps import valid_options
from game_files.logic.state_filler.preprocessed_level import preprocessed_level
from game_files.logic.state_filler.state_load_exception import state_load_exception


def preprocess_level(level_lines):
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
                raise state_load_exception(f"Line {index} [{line}] has incorrect size {len(line)} instead of {x}.")

            for x_ in range(x):
                level.t[x_][y_][z_] = line[x_]
        line_index = 4 + z_ * (y + 1) + y
        index, line = level_lines[line_index]
        if len(line) != 0:
            raise state_load_exception(f"Line {index} [{line}] should be empty.")

    options_lines = level_lines[4 + z * (y + 1):]
    options = {}

    for index, line in options_lines:
        words = line.split()
        if len(line) == 0:
            continue
        opt = words[0]
        if opt not in valid_options:
            raise state_load_exception(f"Line {index} [{line}] has an invalid option {opt}. Check spelling.")
        if opt not in options:
            options[opt] = []
        options[opt].extend(words[1:])

    level.options = options
    return level
