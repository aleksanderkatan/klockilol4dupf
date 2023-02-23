import src.imports.globals as g
from src.speedruns.speedrun import speedrun


class speedrun_birdy(speedrun):
    def get_starting_stage_and_pos(self):
        return (205, 1), (6, 0, 0)

    def is_condition_met(self):
        return g.global_save_state.is_set_completed(205)

    def get_name(self):
        return "Birdy's Rainy Day Skipathon"
