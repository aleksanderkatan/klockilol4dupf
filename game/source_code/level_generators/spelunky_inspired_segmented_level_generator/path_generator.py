def _all_full_paths(stack, x_max, y_max):
    if len(stack) == x_max * y_max:
        yield stack
        return

    x, y = stack[-1]

    all_steps = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    in_border_steps = [(new_x, new_y) for new_x, new_y in all_steps if 0 <= new_x < x_max and 0 <= new_y < y_max]
    valid_steps = [pos for pos in in_border_steps if pos not in stack]

    for pos in valid_steps:
        for path in _all_full_paths(stack + [pos], x_max, y_max):
            yield path


def generate_paths(x_max, y_max):
    for x in range(x_max):
        for y in range(y_max):
            for path in _all_full_paths([(x, y)], x_max, y_max):
                yield path
