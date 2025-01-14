import source_code.imports.globals as g
from source_code.speedruns.speedrun import speedrun
import source_code.imports.levels as l


class speedrun_pm(speedrun):
    def get_starting_stage_and_pos(self):
        return (209, 1), (8, 2, 0)

    def is_condition_met(self):
        return g.save_state.get_set_status(209) == l.level_status.COMPLETED

    def get_name(self):
        return "Platform Maze"
