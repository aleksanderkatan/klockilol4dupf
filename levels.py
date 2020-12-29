#!! levels of level_set 0 are for debugging

hubs = {}
hubs[0] = [1000, 1, 2, 3]
hubs[1] = [4, 5, 6, 7]

levs = {}
levs[0] = 18
levs[1] = 10
levs[2] = 10
levs[3] = 7
levs[4] = 9
levs[5] = 10
levs[6] = 12
levs[7] = 10
levs[1000] = 3
levs[2138] = 2136

level_error_path = 'levels/0/1.txt'

level_error = (0, 0)
level_zero = (0, 0)
level_infinity = (0, 0)


def levels(level_index):
    print(level_index)
    level_set, level = level_index
    if level_set not in levs or not 0 <= level <= levs[level_set]:
        return level_error_path
    return 'levels/' + str(level_set) + '/' + str(level) + '.txt'


def next_level(level_index):
    level_set, level = level_index
    if level_set not in levs:
        return level_error
    if level_set >= 1000:
        return level_set, 0
    if levs[level_set] == level:
        return level_set, 0
    return level_set, level + 1


def previous_level(level_index):
    level_set, level = level_index
    if level_set not in levs:
        return level_error
    if level == 0:
        return level_set, 0
    return level_set, level - 1

def hub_of_set(level_set):
    print("SET", level_set)
    if level_set == 2138:
        return 2138, 0
    for hub, sets in hubs.items():
        if level_set in sets:
            return 2138, hub
    return None

def is_hub(level_index):
    level_set, level = level_index
    if level_set == 2138:
        return True
    return False

def is_zone(level_index):
    level_set, level = level_index
    if not is_hub(level_index):
        if level == 0:
            return True
    return False

def is_level(level_index):
    if is_hub(level_index):
        return False
    if is_zone(level_index):
        return False
    return True
