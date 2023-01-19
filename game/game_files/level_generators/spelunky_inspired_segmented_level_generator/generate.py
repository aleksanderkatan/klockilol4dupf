import random
from game_files.level_generators.spelunky_inspired_segmented_level_generator.path_generator import generate_paths
from game_files.level_generators.spelunky_inspired_segmented_level_generator.segment_provider import segment_provider
from game_files.logic.direction import direction

RIGHT = direction.RIGHT
UP = direction.UP
LEFT = direction.LEFT
DOWN = direction.DOWN



def generate(segments, x, y):
    path = random.choice([elem for elem in generate_paths(x, y)])
    provider = segment_provider(segments)

    chosen_segments = [[None for _ in range(y)] for _ in range(x)]
    start_x, start_y = path[0]
    chosen_segments[start_x][start_y] = provider.get_start(_get_direction(path[0], path[1]))
    end_x, end_y = path[-1]
    chosen_segments[end_x][end_y] = provider.get_end(_get_direction(path[-1], path[-2]))

    for prev, current, next in zip(path[:-2], path[1:-1], path[2:]):
        in_dir = _get_direction(current, prev)
        out_dir = _get_direction(current, next)
        chosen_segments[current[0]][current[1]] = provider.get(in_dir, out_dir)

    lines = ["20", "15", "1"]
    options = {}

    for segment_y in range(y):
        for line_in_y in range(5):
            line = ""
            for segment_x in range(x):
                current_segment = chosen_segments[segment_x][segment_y]
                line_part, options_part = current_segment.lines[line_in_y]
                line = line + line_part
                _add_options(options, options_part)
            lines.append(line)

    lines.append("")

    for key, value in options.items():
        lines.append(f"{key} {value}")
    return lines


def _get_direction(pos1, pos2):
    x, y = pos1
    d = {
        (x+1, y): RIGHT,
        (x, y-1): UP,
        (x-1, y): LEFT,
        (x, y+1): DOWN,
    }
    if pos2 not in d:
        raise RuntimeError("Not a consecutive set of positions")
    return d[pos2]


def _add_options(opt1, opt2):
    for key, value in opt2.items():
        if key not in opt1:
            opt1[key] = ""
        opt1[key] = opt1[key] + " " + opt2[key]

