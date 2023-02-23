import src.imports.globals as g
from src.speedruns.speedrun import speedrun


class speedrun_perfectionist(speedrun):
    def get_starting_stage_and_pos(self):
        return (400, 1), (5, 4, 0)

    def is_condition_met(self):
        return g.global_save_state.get_completion(True) == 1

    def get_name(self):
        return "100%"
