import os

levels_path = "../game_files/levels/"
temp_path = levels_path + "temp/0.lv"

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
# swap_levels((5, 2), (5, 3))
# insert_before((1, 19), (1, 2))
# swap_levels((1, 6), (1, 5))
# insert_before((1, 18), (1, 12))
# swap_levels((1, 16), (1, 15))
# insert_before((1, 19), (1, 16))
# swap_levels((1, 17), (1, 18))
# insert_before((1, 14), (1, 17))
# swap_levels((1, 16), (1, 15))
# swap_levels((1, 11), (1, 12))
# insert_before((2, 14), (2, 2))
# insert_before((2, 6), (2, 3))
# insert_before((2, 7), (2, 4))
# insert_before((2, 9), (2, 5))
# insert_before((2, 12), (2, 6))
# insert_before((2, 13), (2, 7))
# insert_before((2, 14), (2, 8))
# insert_before((3, 15), (3, 7))
# insert_before((4, 5), (4, 17))
# insert_before((4, 7), (4, 17))
# swap_levels((4, 13), (4, 14))
# insert_before((4, 16), (4, 5))
# swap_levels((4, 5), (4, 16))
# insert_before((4, 8), (4, 5))
# insert_before((4, 9), (4, 6))


