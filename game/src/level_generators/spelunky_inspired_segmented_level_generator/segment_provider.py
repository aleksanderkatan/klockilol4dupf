import random
from src.logic.direction import get_cardinal
from src.level_generators.spelunky_inspired_segmented_level_generator.segment import segment


class segment_provider:
    def __init__(self, base_segments: list[segment]):
        self.segments = base_segments
        self.starts = {}
        self.ends = {}
        self.normal = {}

        for first in get_cardinal():
            self.starts[first] = []
            self.ends[first] = []
            self.normal[first] = {}
            for second in get_cardinal():
                self.normal[first][second] = []

        for base in base_segments:
            for seg in base.get_all_invertions():
                if seg.start:
                    for out_dir in seg.outs:
                        self.starts[out_dir].append(seg)
                elif seg.end:
                    for in_dir in seg.ins:
                        self.ends[in_dir].append(seg)
                else:
                    for in_dir in seg.ins:
                        for out_dir in seg.outs:
                            self.normal[in_dir][out_dir].append(seg)


    def get(self, in_dir, out_dir):
        return _roll(self.normal[in_dir][out_dir])

    def get_start(self, out_dir):
        return _roll(self.starts[out_dir])

    def get_end(self, in_dir):
        return _roll(self.ends[in_dir])


def _roll(segment_list: list[segment]):
    if len(segment_list) == 0:
        raise RuntimeError("No such segments!")
    total = 0
    for seg in segment_list:
        total += seg.actual_weight
    roll = random.random()*total
    current_sum = 0
    for seg in segment_list:
        if current_sum <= roll <= current_sum + seg.actual_weight:
            return seg
        current_sum += seg.actual_weight
    raise RuntimeError("This should be unreachable")





