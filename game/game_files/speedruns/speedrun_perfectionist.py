from game.game_files.speedruns.speedrun import speedrun
from game.game_files.imports.save_state import global_save_state

class speedrun_perfectionist(speedrun):
    def get_starting_stage_and_pos(self):
        return (400, 1), (5, 4, 0)

    def is_condition_met(self):
        return global_save_state.get_completion(True) == 1

    def get_name(self):
        return "Shrek%"

