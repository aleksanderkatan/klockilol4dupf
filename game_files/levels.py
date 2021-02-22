from game_files.log import log
# !! levels of level_set 0 are for debugging
# 1 <= normal zones < 100
# 100 < random zones < 200
# 200 < hidden zones < 300
# 300 < hard zones < 400
# 400 - lobbies

hubs = {}
hubs[1] = [1, 201]
hubs[2] = [301, 2, 3, 101, 203]
hubs[3] = [302, 4, 5, 6, 102]
hubs[4] = [303, 7, 8, 9]

levs = {}
levs[0] = 30
levs[1] = 15
levs[2] = 10
levs[3] = 7
levs[4] = 9
levs[5] = 11
levs[6] = 12
levs[7] = 21
levs[8] = 14
levs[9] = 14

levs[101] = 136
levs[102] = 136

levs[201] = 0   # hub 1 to the left
levs[202] = 5   # 8/0 second gap
levs[203] = 5   # bub 2 bottom of the random zone

levs[301] = 3
levs[302] = 4
levs[303] = 5

levs[400] = 5
levs[401] = 0

level_error_path = 'game_files/levels/0/1.txt'

level_error = (0, 0)
level_zero = (0, 0)
level_infinity = (0, 0)

back_to_hub_levels = [(202, 4)]

def levels(level_index):
    level_set, level = level_index
    if level_set not in levs or not 0 <= level <= levs[level_set]:
        log.warning("Wrong level index " + str(level_index))
        return level_error_path
    if level_set == 400 and level_index == 0:
        return level_error_path
    return 'game_files/levels/' + str(level_set) + '/' + str(level) + '.txt'


def next_level(level_index):
    level_set, level = level_index
    if level_set not in levs:
        return level_error
    if level_set >= 300:
        return level_set, 0
    if levs[level_set] == level or level_index in back_to_hub_levels:
        return level_set, 0
    return level_set, level + 1


def previous_level(level_index):
    level_set, level = level_index
    if level_set not in levs:
        return level_error
    if level == 0:
        return level_set, 0
    return level_set, level - 1

def up_in_hierarchy(level_index):
    level_set, level = level_index
    if level_set == 400:
        return 400, 1
    if level != 0:
        return level_set, 0
    if level_set == 202:    # special case for undertale zone
        return 8, 0
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
        return "Hub " + str(level)

    if level_set == 401:
        return ""
    return "error"

def all_levels_iterator():
    for key, value in levs.items():
        for i in range(value+1):
            if i == 0 and key == 400:
                continue
            yield key, i
