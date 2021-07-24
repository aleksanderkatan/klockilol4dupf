import os

levels_path = "../game_files/levels/"
temp_path = levels_path + "-1/0.lv"

def level_path(level):
    return levels_path + str(level[0]) + "/" + str(level[1]) + ".lv"

def swap_levels(level_1, level_2):
    path_1 = level_path(level_1)
    path_2 = level_path(level_2)
    os.rename(path_1, temp_path)
    os.rename(path_2, path_1)
    os.rename(temp_path, path_2)

def insert_before(level_1, level_2):
    if level_1[0] != level_2[0]:
        return

    if level_1[1] < level_2[1]:
        for i in range(level_1[1], level_2[1]-1):
            swap_levels((level_1[0], i), (level_1[0], i+1))
    if level_1[1] > level_2[1]:
        for i in reversed(range(level_2[1], level_1[1])):
            swap_levels((level_1[0], i), (level_1[0], i+1))


# swap_levels((11, 6), (11, 9))
# insert_before((5, 13), (5, 1))
# insert_before((5, 14), (5, 2))
swap_levels((5, 2), (5, 3))
