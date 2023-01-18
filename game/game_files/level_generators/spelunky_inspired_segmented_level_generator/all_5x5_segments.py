from game_files.level_generators.spelunky_inspired_segmented_level_generator.segment import segment
from game_files.logic.direction import direction

RIGHT = direction.RIGHT
UP = direction.UP
LEFT = direction.LEFT
DOWN = direction.DOWN
ALL = [RIGHT, UP, LEFT, DOWN]


segments = [
    # necessary start here
    segment([
        "..1..", {},
        "..1..", {},
        "..S..", {},
        ".....", {},
        ".....", {},
    ], outs=[UP], start=True, flippable="vr"),
    segment([
        "..1..", {},
        "..1..", {},
        "..E..", {},
        ".....", {},
        ".....", {},
    ], ins=[UP], end=True, flippable="vr"),
    segment([
        ".....", {},
        ".....", {},
        "111..", {},
        "..1..", {},
        "..1..", {},
    ], ins=[LEFT], outs=[DOWN], flippable="hvr"),
    segment([
        ".....", {},
        ".....", {},
        "11111", {},
        ".....", {},
        ".....", {},
    ], ins=[LEFT], outs=[RIGHT], flippable="hvr"),
    # necessary end here
    # segment([
    #     "111..", {},
    #     "1.1..", {},
    #     "1.1.1", {},
    #     ".1211", {},
    #     ".11..", {},
    # ], ins=[LEFT], outs=[RIGHT], flippable="hv"),
    # segment([
    #     "..1..", {},
    #     "..11.", {},
    #     ".111.", {},
    #     ".11..", {},
    #     "..1..", {},
    # ], ins=[UP], outs=[DOWN], flippable="hv"),
]
