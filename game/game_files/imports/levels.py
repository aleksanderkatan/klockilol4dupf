from game_files.imports.log import log
import game_files.imports.globals as g

# !! levels of level_set 0 are for debugging
# 1 <= normal zones < 100
# 100 < random zones < 200
# 200 < hidden zones < 300
# 300 < hard zones < 400
# 400 - lobbies
# 500 <= - extra

# where to go after pressing escape? The default is 0 level of the same set
hierarchy = {}
hierarchy[(1, 0)] = (400, 1)
hierarchy[(2, 0)] = (400, 2)
hierarchy[(3, 0)] = (400, 2)
hierarchy[(4, 0)] = (400, 3)
hierarchy[(5, 0)] = (400, 3)
hierarchy[(6, 0)] = (400, 3)
hierarchy[(7, 0)] = (400, 4)
hierarchy[(8, 0)] = (400, 4)
hierarchy[(9, 0)] = (400, 4)
hierarchy[(10, 0)] = (400, 5)
hierarchy[(11, 0)] = (400, 5)
hierarchy[(205, 0)] = (400, 6)
hierarchy[(209, 0)] = (400, 6)


hierarchy[(101, 0)] = (400, 2)
hierarchy[(102, 0)] = (400, 3)
hierarchy[(103, 0)] = (400, 4)

hierarchy[(201, 0)] = (400, 1)
hierarchy[(202, 0)] = (8, 0)
hierarchy[(203, 0)] = (400, 2)
hierarchy[(204, 0)] = (501, 0)
hierarchy[(277, 0)] = (400, 1)

hierarchy[(301, 0)] = (400, 2)
hierarchy[(302, 0)] = (400, 3)
hierarchy[(303, 0)] = (400, 4)

# lobbies lead to themselves
for i in range(1, 6+1):
    hierarchy[(400, i)] = (400, i)

hierarchy[(500, 0)] = (400, 5)
hierarchy[(501, 0)] = (400, 4)

# The Maze
for i in range(1, 16+1):
    hierarchy[(206, i)] = (500, 0)

# hubs = {}
# hubs[1] = [1, 201]
# hubs[2] = [301, 2, 3, 101, 203]
# hubs[3] = [302, 4, 5, 6, 102]
# hubs[4] = [303, 7, 8, 9, 501]
# hubs[5] = [500]

levs = {}
levs[0] = 50
levs[1] = 20
levs[2] = 16
levs[3] = 17
levs[4] = 17
levs[5] = 19
levs[6] = 19
levs[7] = 23
levs[8] = 30
levs[9] = 20
levs[10] = 24

levs[11] = 10

levs[101] = 0
levs[102] = 0
levs[103] = 0

levs[201] = 0  # jojo reference
levs[202] = 5  # undertale
levs[203] = 5  # light
levs[204] = 5  # giszowiec
levs[205] = 20  # birdy
levs[206] = 16  # maze
levs[207] = 15  # moving arrow
levs[208] = 20  # what even is this
levs[209] = 20  # platform maze
levs[277] = 20  # extra levels without zone assigned (yet)
levs[278] = 20  # discarded levels
levs[301] = 5
levs[302] = 5
levs[303] = 5

levs[400] = 6

levs[500] = 2  # non hub, non lobby, non level stages

level_error_path = 'game_files/levels/0/0.lv'

level_error = (0, 0)

# all last-of-a-zone levels are automatically also back-in-hierarchy levels
back_in_hierarchy_levels = {
    (202, 4),
    (101, 0),
    (102, 0),
    (103, 0),
    (8, 20)
}


def is_valid_stage(level_index):
    level_set, level = level_index
    if level_set not in levs:
        return False
    if not 0 <= level <= levs[level_set]:
        return False
    if level_index in [(400, 0)]:
        return False
    return True


def level_path(level_index):
    if not is_valid_stage(level_index):
        log.error("Wrong level index " + str(level_index))
        return level_error_path
    level_set, level = level_index
    return 'game_files/levels/' + str(level_set) + '/' + str(level) + '.lv'


def next_level(level_index):
    level_set, level = level_index
    if level_set not in levs:
        return level_error
    if level_set >= 300:
        return level_set, 0
    if level_index in back_in_hierarchy_levels:
        return up_in_hierarchy(level_index)
    if levs[level_set] == level:
        return level_set, 0
    return level_set, level + 1


def previous_level(level_index):
    level_set, level = level_index
    if level_set not in levs:
        return level_error
    if level == 0:
        return level_set, levs[level_set]
    return level_set, level - 1


def is_hub(level_index):
    level_set, level = level_index
    if level_set == 400:
        return True
    return False


def is_zone(level_index):
    level_set, level = level_index
    if not is_hub(level_index):
        if level == 0 and not (100 < level_set < 200) and not level_set == 500:
            return True
    return False


def is_level(level_index):
    if is_hub(level_index):
        return False
    if is_zone(level_index):
        return False
    if level_index[0] == 500:
        return False
    return True


def all_levels_iterator():
    for key, value in levs.items():
        for i in range(value + 1):
            if i == 0 and key == 400:
                continue
            yield key, i


def levels_ls():
    ans = "Levels\n"
    for level_set, levels in levs.items():
        ans += str(level_set)
        ans += " : "
        for i in range(0 if level_set != 400 else 1, levels + 1):
            ans += str(i)
            ans += ", "
        ans = ans[:-2]
        ans += "\n"
    return ans


def up_in_hierarchy(level_index):
    level_set, level = level_index
    if level_index in hierarchy:
        return hierarchy[level_index]

    if level != 0:  # the default
        return level_set, 0
    return level_error


def level_name(level_index):
    level_set, level = level_index

    if level_set == 0:
        return "Debug " + str(level)

    if level_index == (500, 0):
        return "The Swamp"

    if level_set == 204 or level_index == (500, 1):
        return "Giszowiec"

    if level_set == 206:
        return "The Maze"

    if 0 < level_set < 100:
        return str(level_set) + ("" if level == 0 else "-" + str(level))

    if 100 < level_set < 200:
        return "Randomized level"

    if 200 < level_set < 300:
        return "?" + ("" if level == 0 else "-" + str(level))

    if 300 < level_set < 400:
        return "extra " + str(level_set - 300) + ("" if level == 0 else "-" + str(level))

    if level_set == 400:
        return "Lobby " + str(level)

    if level_index in [(500, 2)]:
        return ""

    return "How did you get here?"


background_index = {
    (500, 0): "background_swamp",
    (500, 1): "background_giszowiec_1",
    (500, 2): "background_kono_dio_da",
    (204, 0): "background_giszowiec_2",
    (4, 2): "background_kidney",
}

background_set = {
    204: "background_giszowiec_3",
}


def background_of_level(level_index):
    level_set, level = level_index
    if level_index in background_index:
        return background_index[level_index]

    if level_set in background_set:
        return background_set[level_set]

    if g.PAPOR:
        return "background_2137"
    return "background_default"
