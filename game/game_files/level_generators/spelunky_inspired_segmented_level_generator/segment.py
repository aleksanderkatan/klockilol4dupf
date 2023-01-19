from game_files.logic.direction import direction

RIGHT = direction.RIGHT
UP = direction.UP
LEFT = direction.LEFT
DOWN = direction.DOWN


# string_lines are like ["11O11", {"ones": "^<v>"}, "..S..", ...]
# weight is how often you'd like to see the segment in a level
class segment:
    def __init__(self, string_lines=None, lines=None, ins=None, outs=None, flippable="hv", start=False, end=False, weight=None):
        if outs is None:
            outs = []
        if ins is None:
            ins = []

        if lines is not None:
            self.lines = lines
        else:
            if string_lines is None:
                raise RuntimeError("At least one of lines and string_lines should be provided")
            self.lines = [(line, options) for line, options in zip(string_lines[::2], string_lines[1::2])]
        self.ins = ins
        self.outs = outs
        self.flippable = flippable
        self.start = start
        self.end = end
        occurrences = max(1, len(ins))*max(1, len(outs)) * (2 ** len(flippable))
        self.actual_weight = 1 / occurrences * (1 if weight is None else weight)


    def get_all_invertions(self):
        result = [self]
        if "h" in self.flippable:
            new_results = []
            for res in result:
                new_results.append(res.get_inverted_horizontally())
            result = result + new_results
        if "v" in self.flippable:
            new_results = []
            for res in result:
                new_results.append(res.get_inverted_vertically())
            result = result + new_results
        if "r" in self.flippable:
            new_results = []
            for res in result:
                new_results.append(res.get_rotated())
            result = result + new_results
        return result

    def get_with_modified_weight(self, modifier):
        return segment(
            None,
            self.lines,
            self.ins,
            self.outs,
            self.flippable,
            self.start,
            self.end,
            self.actual_weight * modifier
        )

    def get_inverted_horizontally(self):
        lines = []
        for line, options in self.lines:
            new_line = replace_all_string(line[::-1], horizontal_inv_options)
            new_options = {}
            for key, value in options.items():
                split = value.split(" ")
                new_value = " ".join([split[0]] + split[::-1][:-1])
                new_options[key] = replace_all_string(new_value, horizontal_inv_options)
            lines.append((new_line, new_options))
        return segment(
            None,
            lines,
            swap_all_directions(self.ins, horizontal_inv_directions),
            swap_all_directions(self.outs, horizontal_inv_directions),
            self.flippable,
            self.start,
            self.end,
            self.actual_weight
        )

    def get_inverted_vertically(self):
        lines = []
        for line, options in self.lines[::-1]:
            new_line = replace_all_string(line, vertical_inv_options)
            new_options = {}
            for key, value in options.items():
                new_options[key] = replace_all_string(value, vertical_inv_options)
            lines.append((new_line, new_options))
        return segment(
            None,
            lines,
            swap_all_directions(self.ins, vertical_inv_directions),
            swap_all_directions(self.outs, vertical_inv_directions),
            self.flippable,
            self.start,
            self.end,
            self.actual_weight
        )

    def get_rotated(self):
        if len(self.lines) != len(self.lines[0][0]):
            raise RuntimeError("Rotation not supported for non square segments")
        for _, options in self.lines:
            if len(options) > 0:
                raise RuntimeError("Rotation not supported for options")

        dim = len(self.lines)
        lines_without_options = [""] * dim
        for y in range(dim):
            for x in range(dim):
                origin_x, origin_y = rotate_cw_pos(x, y, dim)
                character = self.lines[origin_y][0][origin_x]
                lines_without_options[y] = lines_without_options[y] + character

        return segment(
            None,
            [(replace_all_string(line, rotate_ccw_options), {}) for line in lines_without_options],
            swap_all_directions(self.ins, rotate_ccw_directions),
            swap_all_directions(self.outs, rotate_ccw_directions),
            self.flippable,
            self.start,
            self.end,
            self.actual_weight
        )


# !! THIS DOES NOT WORK PROPERLY, FIX IT
def replace_all_string(s, d):
    for key, value in d.items():
        s = s.replace(key, value)
    return s


def swap_all_directions(directions, d):
    return [d[dir] for dir in directions]


horizontal_inv_directions = {
    RIGHT: LEFT,
    UP: UP,
    LEFT: RIGHT,
    DOWN: DOWN,
}

horizontal_inv_options = {
    ">": "<",
    "^": "^",
    "<": ">",
    "v": "v",
}

vertical_inv_directions = {
    RIGHT: RIGHT,
    UP: DOWN,
    LEFT: LEFT,
    DOWN: UP,
}

vertical_inv_options = {
    ">": ">",
    "^": "v",
    "<": "<",
    "v": "^",
}

rotate_ccw_directions = {
    RIGHT: UP,
    UP: LEFT,
    LEFT: DOWN,
    DOWN: RIGHT,
}

rotate_ccw_options = {
    ">": "^",
    "^": "<",
    "<": "v",
    "v": ">",
}


def rotate_cw_pos(x, y, dim):
    return dim-1-y, x

