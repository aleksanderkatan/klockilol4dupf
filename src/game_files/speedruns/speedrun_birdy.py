from game_files.speedruns.speedrun import speedrun
from game_files.imports.save_state import global_save_state


class speedrun_birdy(speedrun):
    def get_starting_stage_and_pos(self):
        return (205, 1), (6, 0, 0)

    def is_condition_met(self):
        return global_save_state.is_set_completed(205)

    def get_name(self):
        return "Birdy's Rainy Day Skipathon"
