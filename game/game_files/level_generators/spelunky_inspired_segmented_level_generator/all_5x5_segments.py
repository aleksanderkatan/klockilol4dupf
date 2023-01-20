from game_files.level_generators.spelunky_inspired_segmented_level_generator.segment import segment
from game_files.logic.direction import direction

RIGHT = direction.RIGHT
UP = direction.UP
LEFT = direction.LEFT
DOWN = direction.DOWN
ALL = [RIGHT, UP, LEFT, DOWN]


# with the following, segment from _1_segment will be chosen 50% of times
# {
#   (_1_segment, 1),
#   (_2_segments, 0.5),
# }
def _get_weighted(pairs: list[(list[segment], float)]):
    result = []
    for segments, weight_modifier in pairs:
        for seg in segments:
            result.append(seg.get_with_modified_weight(weight_modifier))
    return result


# Those are necessary as a fallback if no segments of certain type are provided
_base_segments = [
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
]


_hard_only_numeric_segments = [
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
    ], ins=[LEFT], outs=[DOWN, UP, RIGHT], flippable="hr", weight_base=0.2),
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
    ], ins=[LEFT], outs=[UP], flippable="hvr", weight_base=0.2),
]

_hard_bridge_segments = [
    # starts
    segment([
        ".....", {},
        ".....", {},
        "..M1.", {},
        "..1S.", {},
        ".....", {},
    ], outs=[LEFT, UP], flippable="hvr", start=True),
    segment([
        "..S..", {},
        "..M..", {},
        ".....", {},
        ".1.1.", {},
        ".232.", {},
    ], outs=[UP, DOWN], flippable="vr", start=True),
    segment([
        ".....", {},
        ".....", {},
        "..M1.", {},
        "..121", {},
        "...1S", {},
    ], outs=[UP, LEFT], flippable="vh", start=True),
    # ends
    segment([
        "221..", {},
        "2M...", {},
        "1.E..", {},
        ".11..", {},
        ".11..", {},
    ], ins=[UP, LEFT], end=True, flippable="vhr"),
    segment([
        ".....", {},
        ".1.M1", {},
        ".1E.2", {},
        "....2", {},
        "..122", {},
    ], ins=[DOWN, RIGHT], end=True, flippable="vhr"),
    segment([
        "22221", {},
        "2....", {},
        "E....", {},
        "22.21", {},
        ".222M", {},
    ], ins=[LEFT, UP, DOWN], end=True, flippable="vhr"),
    # normals
    segment([
        ".....", {},
        ".010.", {},
        "12M1.", {},
        ".010.", {},
        ".....", {},
    ], ins=[LEFT], outs=ALL, flippable="hr", weight_base=0.1),
    segment([
        "2221.", {},
        "2..M.", {},
        "2...1", {},
        "1M..2", {},
        "..122", {},
    ], ins=[UP], outs=[RIGHT, DOWN], flippable="hvr"),
    segment([
        "111..", {},
        "111..", {},
        "11..1", {},
        "11..1", {},
        "1M.M1", {},
    ], ins=[LEFT, UP], outs=[RIGHT], flippable="hvr", weight_base=0.5),
    segment([
        "111..", {},
        "111..", {},
        "11..1", {},
        "11..1", {},
        "1M.M1", {},
    ], ins=[RIGHT], outs=[LEFT, UP], flippable="hvr", weight_base=0.5),
    segment([
        ".....", {},
        ".11..", {},
        "12M..", {},
        ".11..", {},
        ".....", {},
    ], ins=[LEFT], outs=[UP, DOWN], flippable="hr"),
    segment([
        ".....", {},
        ".010.", {},
        "12M21", {},
        ".010.", {},
        ".....", {},
    ], ins=[LEFT], outs=[UP, DOWN, RIGHT], flippable="hr", weight_base=0.1),
    segment([
        "...1.", {},
        "...M.", {},
        "12111", {},
        ".11M1", {},
        "...11", {},
    ], ins=[LEFT], outs=[UP], flippable="hvr"),
    segment([
        "1111.", {},
        "1111.", {},
        "1M11.", {},
        ".....", {},
        ".....", {},
    ], ins=[LEFT], outs=[UP], flippable="hvr", weight_base=0.5),
    segment([
        "1111.", {},
        "1111.", {},
        "11M1.", {},
        ".....", {},
        ".....", {},
    ], ins=[LEFT], outs=[DOWN], flippable="hvr", weight_base=0.5),
    segment([
        "M11..", {},
        "12111", {},
        "11..1", {},
        ".1111", {},
        ".....", {},
    ], ins=[LEFT], outs=[UP], flippable="hvr"),
    segment([
        "010..", {},
        "2M211", {},
        "010.1", {},
        ".....", {},
        ".....", {},
    ], ins=[RIGHT], outs=[LEFT, UP], flippable="hvr", weight_base=0.05),
    segment([
        "010..", {},
        "2M211", {},
        "010.1", {},
        ".....", {},
        ".....", {},
    ], ins=[LEFT, UP], outs=[RIGHT], flippable="hvr", weight_base=0.05),
    segment([
        ".11..", {},
        ".1M..", {},
        "1....", {},
        "1M1..", {},
        "122..", {},
    ], ins=[DOWN], outs=[RIGHT], flippable="hvr"),
]

_test_segments = [
    segment([
        ">v0<^", {},
        "^>0v<", {},
        "00000", {},
        "..0>v", {},
        "..0^>", {},
    ], ins=ALL, outs=ALL, flippable="hvr"),
    segment([
        "..01.", {},
        "..0..", {},
        "00000", {},
        "..0..", {},
        "..0..", {},
    ], ins=ALL, outs=ALL, flippable="vrh"),
    segment([
        "..1..", {},
        "..1..", {},
        "..O..", {"ones": "v"},
        "..O..", {"ones": "^"},
        "..1..", {},
    ], ins=[UP], outs=[DOWN], flippable="v"),
    segment([
        ".....", {},
        ".....", {},
        "1OO11", {"ones": "> <"},
        ".....", {},
        ".....", {},
    ], ins=[LEFT], outs=[RIGHT], flippable="h"),
    segment([
        "..1..", {},
        "..1..", {},
        ".....", {},
        "..O..", {"ones": "^"},
        "..1..", {},
    ], ins=[DOWN], outs=[UP], flippable="v"),
    segment([
        ".....", {},
        ".....", {},
        "O.111", {"ones": ">"},
        ".....", {},
        ".....", {},
    ], ins=[LEFT], outs=[RIGHT], flippable="h"),
]



preset_hard_numeric = _get_weighted([
    (_base_segments, 0.0001),
    (_hard_only_numeric_segments, 1),
])

preset_harder = _get_weighted([
    (_base_segments, 0.0001),
    (_hard_only_numeric_segments, 0.25),
    (_hard_bridge_segments, 1),
])


