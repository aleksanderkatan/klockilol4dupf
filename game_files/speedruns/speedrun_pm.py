from game_files.speedruns.speedrun import speedrun
from game_files.imports.save_state import global_save_state

class speedrun_mp(speedrun):
    def get_starting_stage_and_pos(self):
        return (209, 1), (8, 2, 0)

    def is_condition_met(self):
        # return global_save_state.is_level_completed((209, 1))
        return global_save_state.is_set_completed(209)

    def get_name(self):
        return "Platform Maze"

