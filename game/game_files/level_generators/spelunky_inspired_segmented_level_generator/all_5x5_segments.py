from game_files.level_generators.spelunky_inspired_segmented_level_generator.segment import segment
from game_files.logic.direction import direction

RIGHT = direction.RIGHT
UP = direction.UP
LEFT = direction.LEFT
DOWN = direction.DOWN
ALL = [RIGHT, UP, LEFT, DOWN]


# remember that they are not rotatable, the code works for non-square segments!
segments = [
    segment([
        "..1..", {},
        "..1..", {},
        "..S..", {},
        ".....", {},
        ".....", {},
    ], outs=[UP], start=True, flippable="v"),
    segment([
        ".....", {},
        ".....", {},
        "11S..", {},
        ".....", {},
        ".....", {},
    ], outs=[LEFT], start=True, flippable="h"),
    segment([
        "..1..", {},
        "..1..", {},
        "..E..", {},
        ".....", {},
        ".....", {},
    ], ins=[UP], end=True, flippable="v"),
    segment([
        ".....", {},
        ".....", {},
        "11E..", {},
        ".....", {},
        ".....", {},
    ], ins=[LEFT], end=True, flippable="h"),
    segment([
        "111..", {},
        "1.1..", {},
        "1.1.1", {},
        ".1211", {},
        ".11..", {},
    ], ins=[LEFT], outs=[RIGHT], flippable="hv"),
    segment([
        "..1..", {},
        "..11.", {},
        ".111.", {},
        ".11..", {},
        "..1..", {},
    ], ins=[UP], outs=[DOWN], flippable="hv"),
    segment([
        ".....", {},
        ".....", {},
        "111..", {},
        "..1..", {},
        "..1..", {},
    ], ins=[LEFT], outs=[DOWN], flippable="hv"),
    segment([
        ".....", {},
        ".....", {},
        "111..", {},
        "..1..", {},
        "..1..", {},
    ], ins=[DOWN], outs=[LEFT], flippable="hv"),
]
