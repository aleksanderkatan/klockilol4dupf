import src.imports.globals as g
from src.speedruns.speedrun import speedrun


class speedrun_pm(speedrun):
    def get_starting_stage_and_pos(self):
        return (209, 1), (8, 2, 0)

    def is_condition_met(self):
        return g.save_state.is_set_completed(209)

    def get_name(self):
        return "Platform Maze"
