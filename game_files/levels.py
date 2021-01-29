from game_files.save_state import global_save_state
# !! levels of level_set 0 are for debugging
# 1 <= normal zones < 100
# 100 < random zones < 200
# 200 < hidden zones < 300
# 300 < hard zones < 400
# 400 - lobbies

hubs = {}
hubs[0] = [1]
hubs[1] = [301, 2, 3, 101]
hubs[2] = [302, 4, 5, 6, 7, 102]

levs = {}
levs[0] = 19
levs[1] = 13
levs[2] = 10
levs[3] = 7
levs[4] = 9
levs[5] = 10
levs[6] = 12
levs[7] = 14
levs[101] = 136
levs[301] = 3
levs[302] = 3
levs[400] = 2136


level_error_path = 'game_files/levels/0/1.txt'

level_error = (0, 0)
level_zero = (0, 0)
level_infinity = (0, 0)


def levels(level_index):
    print(level_index)
    level_set, level = level_index
    if level_set not in levs or not 0 <= level <= levs[level_set]:
        return level_error_path
    return 'game_files/levels/' + str(level_set) + '/' + str(level) + '.txt'


def next_level(level_index):
    level_set, level = level_index
    if level_set not in levs:
        return level_error
    if level_set >= 300:
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
    if level_set == 400:
        return 400, 0
    for hub, sets in hubs.items():
        if level_set in sets:
            return 400, hub
    return level_error

def is_hub(level_index):
    level_set, level = level_index
    if level_set == 400:
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

def level_name(level_index):
    level_set, level = level_index
    if level_set < 100:
        if level == 0:
            return "Zone " + str(level_set)
        return "Zone " + str(level_set) + " level " + str(level)

    if 100 < level_set < 200:
        if level != 0:
            return "Zone random " + str(level_set-100) + " level " + str(level)
        return "Zone random " + str(level_set-100)

    if 200 < level_set < 300:
        return "???"

    if 300 < level_set < 400:
        if level != 0:
            return "Zone extra " + str(level_set - 300) + " level " + str(level)
        return "Zone extra " + str(level_set - 300)

    if level_set == 400:
        return "Hub " + str(level+1)

    return "error"
