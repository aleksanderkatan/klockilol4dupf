from enum import Enum

class direction(Enum):
    PASS = None
    RIGHT = 0
    UP = 1
    LEFT = 2
    DOWN = 3
    ASCEND = 4
    DESCEND = 5
    FORCED_SKIP = 6

    def is_cardinal(dir):
        return dir.value in [0, 1, 2, 3]
