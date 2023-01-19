from game_files.level_generators.spelunky_inspired_segmented_level_generator.segment import segment
from game_files.logic.direction import direction

RIGHT = direction.RIGHT
UP = direction.UP
LEFT = direction.LEFT
DOWN = direction.DOWN
ALL = [RIGHT, UP, LEFT, DOWN]


# Those are necessary as a fallback if no segments of certain type are provided
base_segments = [
    segment([
        "..1..", {},
        "..1..", {},
        "..S..", {},
        ".....", {},
        ".....", {},
    ], outs=[UP], start=True, flippable="vr", weight=0.0001),
    segment([
        "..1..", {},
        "..1..", {},
        "..E..", {},
        ".....", {},
        ".....", {},
    ], ins=[UP], end=True, flippable="vr", weight=0.0001),
    segment([
        ".....", {},
        ".....", {},
        "111..", {},
        "..1..", {},
        "..1..", {},
    ], ins=[LEFT], outs=[DOWN], flippable="hvr", weight=0.0001),
    segment([
        ".....", {},
        ".....", {},
        "11111", {},
        ".....", {},
        ".....", {},
    ], ins=[LEFT], outs=[RIGHT], flippable="hvr", weight=0.0001),
]


hard_5x5_segments = base_segments + [
    # starts
    segment([
        "111..", {},
        "1.1..", {},
        "11S11", {},
        "..1.1", {},
        "..111", {},
    ], outs=ALL, start=True, flippable="v"),
    segment([
        ".11..", {},
        ".1111", {},
        ".1S11", {},
        ".11..", {},
        ".11..", {},
    ], outs=[DOWN, UP, RIGHT], start=True, flippable="vhr"),
    segment([
        ".....", {},
        ".....", {},
        "11211", {},
        "1.1.1", {},
        "11S11", {},
    ], outs=[LEFT, DOWN, RIGHT], start=True, flippable="vr"),
    # ends
    segment([
        "..1..", {},
        ".12..", {},
        "12E..", {},
        ".....", {},
        ".....", {},
    ], ins=[UP, LEFT], end=True, flippable="hv"),
    segment([
        "..1..", {},
        ".E32.", {},
        "12121", {},
        ".....", {},
        ".....", {},
    ], ins=[UP, LEFT, RIGHT], end=True, flippable="hvr"),
    segment([
        "E1111", {},
        "11111", {},
        "11111", {},
        ".....", {},
        ".....", {},
    ], ins=[UP, LEFT, RIGHT], end=True, flippable="vr"),
    # normals
    segment([
        "1111.", {},
        "1.11.", {},
        "1.1.1", {},
        ".1211", {},
        ".11..", {},
    ], ins=[LEFT], outs=[RIGHT], flippable="hvr"),
    segment([
        "..21.", {},
        "..111", {},
        ".1111", {},
        ".11..", {},
        "..1..", {},
    ], ins=[UP], outs=[DOWN], flippable="hvr"),
    segment([
        "..111", {},
        ".1111", {},
        "11111", {},
        "111.1", {},
        "11111", {},
    ], ins=[LEFT], outs=[DOWN, UP, RIGHT], flippable="hr", weight=0.2),
    segment([
        "..111", {},
        "..111", {},
        "11111", {},
        ".....", {},
        ".....", {},
    ], ins=[LEFT], outs=[UP, RIGHT], flippable="hvr"),
    segment([
        "..111", {},
        "....1", {},
        "1...1", {},
        "1...1", {},
        "11111", {},
    ], ins=[LEFT], outs=[UP], flippable="hvr", weight=0.2),
]
