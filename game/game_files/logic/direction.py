from enum import Enum


class direction(Enum):
    NONE = -1
    RIGHT = 0
    UP = 1
    LEFT = 2
    DOWN = 3
    ASCEND = 4
    DESCEND = 5
    FORCED_SKIP = 6

    def is_cardinal(self):
        return self.value in [0, 1, 2, 3]

    def get_cardinal():
        return [direction.RIGHT, direction.UP, direction.LEFT, direction.DOWN]

    def __eq__(self, other):
        if self.value == other.value:
            return True

    def __gt__(self, other):
        return self.value > other.value
