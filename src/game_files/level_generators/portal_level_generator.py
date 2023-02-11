import random
import game_files.imports.utils as u
from game_files.imports.log import log
from game_files.level_generators.less_simple_level_generator import better_level_generator


# that's programming art

def random_positions(x, y, amount):
    positions = []
    for i in range(x):
        for j in range(y):
            positions.append((i, j))
    random.shuffle(positions)
    answer = positions[0:amount]

    # sort
    def key(a):
        return a[1] + a[0] * y

    return sorted(answer, key=key)


def paired_permutation(n):
    pairs = [i for i in range(n)]
    random.shuffle(pairs)

    res = [-1 for _ in range(n)]
    for i, k in zip(pairs[0::2], pairs[1::2]):
        res[i] = k
        res[k] = i

    return res


def find_premutation(n, no_fixed_points=True, paired=True):
    if n % 2 == 0 and paired:
        return paired_permutation(n)

    res = [i for i in range(n)]

    while True:
        random.shuffle(res)

        if not no_fixed_points:
            break

        has_fixed_point = False
        for i in range(n):
            if res[i] == i:
                has_fixed_point = True

        if not has_fixed_point:
            break

    return res


class block:
    def __init__(self):
        self.steps = 0
        self.type = "."
        self.portal_index = 21372137


def try_generate(x, y, portals, min_portals, pair_portals, length, redirect):
    x, y = y, x  # art

    portal_destinations = find_premutation(portals, pair_portals)
    grid = [[block() for _ in range(y)] for _ in range(x)]
    positions = random_positions(x, y, portals)

    for index, position in enumerate(positions):
        _x, _y = position
        grid[_x][_y].type = "P"
        grid[_x][_y].portal_index = index

    # chose starting point

    player_pos = None
    player_direction = random.randint(0, 3)
    for _ in range(100):
        player_pos = (random.randint(0, x - 1), random.randint(0, y - 1))
        if grid[player_pos[0]][player_pos[1]].type == ".":
            break

    if player_pos is None:
        log.info("FAIL: couldn't find a starting point")
        return None

    # set starting point

    grid[player_pos[0]][player_pos[1]].type = "S"

    # for convenience

    def move(pos, direction, increase):
        if increase:
            grid[pos[0]][pos[1]].steps += 1

        pos = better_level_generator.next_pos(pos, direction)

        if not u.out_of_range(pos[0], pos[1], x, y) and grid[pos[0]][pos[1]].type == "P":
            if increase:
                grid[pos[0]][pos[1]].steps += 1
            destination_index = portal_destinations[grid[pos[0]][pos[1]].portal_index]
            pos = positions[destination_index]
            return move(pos, direction, increase)
        return pos

    # begin walking loop

    for _ in range(length):
        new_player_direction = None

        # select new player direction

        for _ in range(30):
            if random.randint(0, redirect - 1) == 0 or (
                    player_pos[0] == 0 or player_pos[1] == 0 or player_pos[0] == x or player_pos[1] == y):
                new_player_direction = random.randint(0, 3)
            else:
                new_player_direction = player_direction

            new_player_pos = move(player_pos, new_player_direction, False)
            if not u.out_of_range(new_player_pos[0], new_player_pos[1], x, y):
                break
            new_player_direction = None

        if new_player_direction is None:
            log.info("FAIL: no valid moves")
            return None
        player_direction = new_player_direction

        player_pos = move(player_pos, player_direction, True)

    # check if last position is legit

    if grid[player_pos[0]][player_pos[1]].type not in ["."]:
        log.info("FAIL: ending point not empty")
        return None

    grid[player_pos[0]][player_pos[1]].type = "E"

    # filter non-stepped on portals

    mask = []

    for position in positions:
        _x, _y = position
        blo = grid[_x][_y]
        mask.append(blo.steps != 0)

    counter = 0
    new_indexes = []

    for real in mask:
        if real:
            new_indexes.append(counter)
            counter += 1
        else:
            new_indexes.append(-1)

    new_destinations = []
    new_positions = []
    for old_destination, old_position in zip(portal_destinations, positions):
        if new_indexes[old_destination] != -1:
            new_destinations.append(new_indexes[old_destination])
            new_positions.append(positions)

    portal_destinations = new_destinations
    positions = new_positions

    for i in range(x):
        for j in range(y):
            blo = grid[i][j]
            if blo.steps == 0 and blo.type == "P":
                blo.type = "."

    # count portals

    actual_portals = 0
    portal_steps = 0

    for i in range(x):
        for j in range(y):
            blo = grid[i][j]
            if blo.type == "P":
                actual_portals += 1
                portal_steps += blo.steps

    # filter

    if actual_portals < min_portals:
        log.info("FAIL: not enough portals")
        return None

    if actual_portals > 0:
        # encourage multi-stepped portals
        avg_steps = portal_steps / actual_portals
        if random.random() + 1 < avg_steps:
            log.info("FAIL: not enough portal steps")
            return None

    # translate into level string

    level_string = str(x) + "\n" + str(y) + "\n" + str(1) + "\n"

    for i in range(x):
        for j in range(y):
            blo = grid[i][j]

            char = "."
            if blo.type == ".":
                if blo.steps > 5:
                    char = "0"
                elif blo.steps > 0:
                    char = str(blo.steps)
            else:
                char = blo.type

            level_string += char
        level_string += "\n"

    level_string += "\n"
    level_string += "portals " + str(portal_destinations).replace(",", "")[1:-1]
    level_string += "\n"

    return level_string


def generate(index, x, y, portals, min_portals, pair_portals, length, redirect):
    for _ in range(100):
        level_string = try_generate(x, y, portals, min_portals, pair_portals, length, redirect)
        if level_string is not None:
            path = "game_files/levels/" + str(index[0]) + "/" + str(index[1]) + ".lv"
            f = open(path, "w")
            f.write(level_string)
            f.close()
            log.info("SUCCESS: level successfully generated")

            return True
    log.error("FAIL: level failed to generate")
    return False

# generate(index=(103, 0), x=10, y=10, portals=4, length=30, redirect=4)
